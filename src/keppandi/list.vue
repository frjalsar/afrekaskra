<template>
  <div>
    <input
      :value="searchQ"
      type="text"
      class="form-control text-center"
      placeholder="Leita (t.d. Kristinn FH)"
      @input="searchInput"
      ref="athleteSearch"
    />
    <!-- -->
    <div class="row">
      <div class="col-md-12">
        <table class="table">
          <thead class="thead-light">
            <tr>
              <th scope="col" class="d-none d-lg-table-cell">Númer</th>
              <th scope="col">Nafn</th>
              <th scope="col" class="d-none d-md-table-cell">Fæðingarár</th>
              <th scope="col">Félag</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="loading">
              <td colspan="4" align="center">
                <div v_if="loading">
                <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
                <p>{{message}}<p>
                <div>
              </td>
            </tr>
            <tr
              v-for="athlete in athletes"
              :key="athlete.CompetitorCode"
              @click.prevent="onClick && onClick(athlete)"
            >
              <td class="d-none d-lg-table-cell">{{ athlete.CompetitorCode }}</td>
              <td>{{ athlete.Name }}</td>
              <td class="d-none d-md-table-cell">{{ athlete.YOB }}</td>
              <td>{{ athlete.Club }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import debounce from "lodash.debounce";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "KeppandiList",
  components: {
    PulseLoader
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",
      loading: false,

      athletes: [],
      searchQ: "",
      message: "",
      cancelSource: null
    };
  },
  created() {
    var parameters = this.$route.query;
    if ("search" in parameters) {
      this.searchQ = this.$route.query.search;
      if (this.searchQ.length >= 3) {
        this.search()
      }
    }
  },
  methods: {
    onClick(item) {
      //this.$router.push("/keppandi/" + item.CompetitorCode);
      this.$router.push({name: 'CompetitorProfile', params: {competitorID: item.CompetitorCode}})
    },
    searchInput: debounce(function(e) {
      this.searchQ = e.target && e.target.value;
      this.$router.replace({ query: { search: this.searchQ } });

      // To clear box
      if (this.search.length === 0) {
        this.athletes = [];
      }

      //Only search on 3
      if (this.searchQ.length >= 3) {
        this.search();
      }
    }, 600),
    //     searchInput: function(e) {
    //       this.searchQ = e.target && e.target.value
    //   // Only search on 3
    //   // if (this.search.length >= 3) {
    //   //   this.searchQ = "";
    //   // }
    // },
    search() {
      var url = this.global_API_URL + "/api/competitor?term=";

      this.loading = true;
      this.athletes = [];

      //this.cancelSearch();
      this.cancelSource = axios.CancelToken.source();

      //console.log("Searching for " + this.searchQ);
      axios
        .get(url + this.searchQ, {
        cancelToken: this.cancelSource.token })
        .then(response => {
          //console.log("RESPONSE");
          //console.log(response);
          this.athletes = response["data"];
          this.cancelSource = null;
          this.loading = false;
          //console.log(this.$refs)
          this.$refs.athleteSearch.scrollIntoView({ scrollBehavior: 'smooth' });
        })
        .catch(error => {
          //console.log("ERROR");
          //console.log(error);
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
        })
        .finally(() => {
          //console.log("FINALLY");
          //this.loading = false;
        });
    },
    cancelSearch () {
      if (this.cancelSource) {
        this.cancelSource.cancel('Start new search, stop active search');
        //console.log('cancel request done');
      }
    }
  }
};
</script>