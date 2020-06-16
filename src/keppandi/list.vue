<template>
  <div>
    <input
      :value="searchQ"
      type="text"
      class="form-control text-center"
      placeholder="Leita"
      @input="searchInput"
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
              <th scope="col" class="d-none d-md-table-cell">Félag</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="loading">
              <td colspan="5" align="center">
                <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
                {{message}}
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
              <td class="d-none d-md-table-cell">{{ athlete.Club }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import debounce from 'lodash.debounce'
import PulseLoader from "vue-spinner/src/PulseLoader.vue"

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
      searchQ: '',
      message: ''
    };
  },
  // //created() {},
  methods: {
        onClick (item) {
      this.$router.push('/keppandi/' + item.CompetitorCode)
    },
    searchInput: debounce(function(e) {
      this.searchQ = e.target && e.target.value
      //Only search on 3
      if (this.searchQ.length >= 3) {
        this.search()
      }
    }, 300),
    //     searchInput: function(e) {
    //       this.searchQ = e.target && e.target.value
    //   // Only search on 3
    //   // if (this.search.length >= 3) {
    //   //   this.searchQ = "";
    //   // }
    // },
    search() {
      var url = this.global_API_URL + '/api/keppandi/'

      this.loading = true


      console.log('Searching for ' + this.searchQ)
      axios
        .get(url, {
                              params: {
                        term: this.searchQ
                    }
        })
        .then(response => {
          console.log('RESPONSE')
          console.log(response)
          this.athletes = response["data"]
        })
        .catch(error => {
          console.log('ERROR')
          console.log(error)
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
        })
        .finally(() => {
          console.log('FINALLY')
          this.loading = false;
        });
    }
  }
};
</script>