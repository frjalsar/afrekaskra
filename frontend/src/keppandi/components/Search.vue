<template>
  <div>
    <input :value="searchQ" type="text" class="form-control text-center" placeholder="Sláðu inn nafn, félag eða fæðingarár" @input="searchInput" ref="athleteSearch" />
    <!-- -->
    <div class="row" v-show="showSearchQ">
      <div class="col-md-12">
        <table class="table">
          <thead class="thead-light">
            <tr>
              <!--<th scope="col" class="d-none d-lg-table-cell">Númer</th>-->
              <th scope="col">Nafn</th>
              <th scope="col">Félag</th>
              <th scope="col">Fæðingarár</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="showMessage">
              <td colspan="3" align="center">
                <div v-if="loading">
                  <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
                  <p>{{ message }}</p>
                </div>
              </td>
            </tr>
            <tr v-for="athlete in athletes" :key="athlete.CompetitorCode" @click.prevent="onClick && onClick(athlete)">
              <!--<td class="d-none d-lg-table-cell">{{ athlete.CompetitorCode }}</td>-->
              <td>
                <!--<a v-bind:href="'/keppandi/' + athlete.CompetitorCode">{{athlete.Name}}</a>-->
                <router-link :to="{ name: 'CompetitorProfile', params: { competitorID: athlete.CompetitorCode } }">
                  {{ athlete.Name }}
                </router-link>
              </td>
              <td>{{ athlete.Club }}</td>
              <td>{{ athlete.YOB }}</td>
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
  name: "KeppandiSearch",
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
      showMessage: false,
      showSearchQ: false,

      athletes: [],
      searchQ: "",
      message: "",
      api_url_prefix: this.global_api_url_prefix,
      cancelSource: null
    };
  },
  created() {
    var parameters = this.$route.query;
    if ("search" in parameters) {
      this.searchQ = this.$route.query.search;
      if (this.searchQ.length >= 2) {
        this.search()
      }
    }
  },
  methods: {
    onClick(item) {
      //this.$router.push("/keppandi/" + item.CompetitorCode);
      this.$router.push({ name: 'CompetitorProfile', params: { competitorID: item.CompetitorCode } })
    },
    searchInput: debounce(function (e) {
      this.searchQ = e.target && e.target.value;
      this.$router.replace({ query: { search: this.searchQ } });

      // To clear box
      if (this.search.length === 0) {
        this.athletes = [];
        this.showSearchQ = false;
      }

      //Only search on 3
      if (this.searchQ.length >= 2) {
        this.search();
      }
    }, 2250),
    //     searchInput: function(e) {
    //       this.searchQ = e.target && e.target.value
    //   // Only search on 3
    //   // if (this.search.length >= 3) {
    //   //   this.searchQ = "";
    //   // }
    // },
    search() {
      //var url = this.global_API_URL + "/api/competitor?search=";
      var url = this.api_url_prefix + "/api/competitor";

      this.loading = true;
      this.message = "Leita að keppanda...";
      this.showMessage = true;
      this.showSearchQ = true;
      this.athletes = [];

      //this.cancelSearch();
      this.cancelSource = axios.CancelToken.source();

      //console.log("Searching for " + this.searchQ);
      axios
        .get(url, {
          cancelToken: this.cancelSource.token,
          params: { search: this.searchQ }
        })
        .then(response => {

          this.athletes = response["data"];
          this.cancelSource = null;
          this.loading = false;
          this.showMessage = false;

          if (this.athletes.length == 0) {
            this.message = "Enginn keppandi fannst";
            this.showMessage = true;
          }
        })
        .catch(error => {
          //console.log("ERROR");
          //console.log(error);
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          this.showMessage = true;
          this.athletes = [];
        })
        .finally(() => {
          //console.log("FINALLY");
          //this.loading = false;
        });
    },
    cancelSearch() {
      if (this.cancelSource) {
        this.cancelSource.cancel('Start new search, stop active search');
        //console.log('cancel request done');
      }
    }
  }
};
</script>

<!--
<style scoped>
.search-div {
  position: absolute;
  z-index: 1;
  background: white;
  width: 100%;
}
</style>
-->
