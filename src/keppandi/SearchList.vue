<template>
  <div>
    <div>
      <h1 class="text-center mb-4">Iðkendur</h1>
      <SearchPanel
        :clubs="clubs"
        :settings="settings"
        @change="setQueryParams"
      />
    </div>
    <div class="row">
      <div class="col-md-12">
        <table class="table">
          <thead class="thead-light">
            <tr>
              <th scope="col" class="d-none d-lg-table-cell">Númer</th>
              <th scope="col">Nafn</th>
              <th scope="col" class="d-none d-md-table-cell">Fæðingarár</th>
              <th scope="col" class="">Félag</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="busy">
              <td colspan="4" align="center">
                <PulseLoader :loading="busy" color="#007bff" />
              </td>
            </tr>
            <tr
              v-for="athlete in athletes"
              :key="athlete.CompetitorCode"
            >
              <td class="d-none d-lg-table-cell">
                {{ athlete.CompetitorCode }}
              </td>
              <td>
                <router-link
                  :to="{
                    name: 'CompetitorProfile',
                    params: { competitorID: athlete.CompetitorCode },
                  }"
                >
                  {{ athlete.Name }}
                </router-link>
              </td>
              <td class="d-none d-md-table-cell">
                {{ athlete.YOB }}
              </td>
              <td class=""><img
                class="img-club"
                v-bind:src="api_url_prefix + '/api/img/club/' + athlete.Club"
                v-bind:alt="athlete.Club"
              />
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import SearchPanel from "./components/SearchPanel.vue";
import axios from "axios";

export default {
  name: "AthletesList",
  components: {
    PulseLoader,
    SearchPanel,
  },
  data() {
    return {
      busy: false,
      athletes: [],
      clubs: [],
      message: "",
      api_url_prefix: this.global_api_url_prefix,
    };
  },
  computed: {
    settings() {
      return this.$route.query;
    },
  },
  created() {
    var parameters = this.$route.query;
    if ("CompetitorCode" in parameters) {
      this.$router.push("/keppandi/" + this.$route.query.CompetitorCode);
    }
  },
  mounted() {
    var url = this.api_url_prefix + "/api/clubs";
    this.search();

    // agent
    //   .get(process.env.FRI_API_URL + '/api/clubs')
    //   .withCredentials()
    //   .then(res => {
    //     this.clubs = res.body
    //   })
    axios
      .get(url)
      .then((response) => {
        this.clubs = response["data"];
      })
      .catch((error) => {
        this.message = "Villa frá vefþjóni (" + error + ") 😭";
      })
      .finally(() => {
        //console.log("FINALLY");
        //this.loading = false;
      });
  },
  methods: {
    setQueryParams(query) {
      this.$router.replace({ query });
      this.search();
    },
    onClick(item) {
      this.$router.push("/keppandi/" + item.CompetitorCode);
    },
    search() {
      var url = this.api_url_prefix + "/api/competitor";
      this.busy = true;
      this.athletes = [];
      return axios
        .get(url, { params: this.$route.query })
        .then((response) => {
          this.athletes = response["data"];
          this.busy = false;
        })
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
        })
        .finally(() => {
          this.busy = false;
        });
      // return agent
      //   .get(process.env.FRI_API_URL + '/api/athletes')
      //   .query(this.$route.query)
      //   .then(res => {
      //     this.athletes = res.body
      //     this.busy = false
      //   })
    },
  },
};
</script>

<style scoped>
tr:hover td {
  cursor: pointer;
  background-color: #eee;
}

.img-club {
  height: 25px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
