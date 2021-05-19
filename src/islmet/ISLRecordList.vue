<template>
  <div>
    <div
      class="btn-toolbar"
      role="toolbar"
      aria-label="Tækjastika"
      style="text-align: center; display: block"
    >
      <div
        class="btn-group mr-2"
        role="group"
        aria-label="Innanhús utanhús takkar"
      >
        <button type="button" class="btn btn-secondary">Innanhús</button>
        <button type="button" class="btn btn-secondary">Utanhús</button>
      </div>
      <div class="btn-group mr-2" role="group" aria-label="Karlar konur takkar">
        <button type="button" class="btn btn-secondary">Karlar</button>
        <button type="button" class="btn btn-secondary">Konur</button>
      </div>
      <div
        class="btn-group mr-2"
        role="group"
        aria-label="Valmynd fyrir aldursflokk"
      >
        <button type="button" class="btn btn-primary">
          Allir aldursflokkar
        </button>
        <button
          id="btnGroupDrop1"
          type="button"
          class="btn btn-secondary dropdown-toggle"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          {{ agegroup_text }}
        </button>
        <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
          <a class="dropdown-item" href="#">Fullorðnir</a>
          <a class="dropdown-item" href="#">20-22 ára</a>
          <a class="dropdown-item" href="#">18-19 ára</a>
          <a class="dropdown-item" href="#">16-17 ára</a>
          <a class="dropdown-item" href="#">15 ára</a>
          <a class="dropdown-item" href="#">14 ára</a>
          <a class="dropdown-item" href="#">13 ára</a>
          <a class="dropdown-item" href="#">12 ára</a>
        </div>
      </div>
      <div
        class="btn-group mr-2"
        role="group"
        aria-label="Valmynd fyrir aldursflokk"
      >
        <button
          id="btnGroupDrop2"
          type="button"
          class="btn btn-secondary dropdown-toggle"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          Öldungaflokkar
        </button>
        <div class="dropdown-menu" aria-labelledby="btnGroupDrop2">
          <a class="dropdown-item" href="#">30-34 ára</a>
          <a class="dropdown-item" href="#">35-39 ára</a>
          <a class="dropdown-item" href="#">40-44 ára</a>
          <a class="dropdown-item" href="#">45-49 ára</a>
          <a class="dropdown-item" href="#">50-54 ára</a>
          <a class="dropdown-item" href="#">55-59 ára</a>
          <a class="dropdown-item" href="#">60-64 ára</a>
          <a class="dropdown-item" href="#">65-69 ára</a>
          <a class="dropdown-item" href="#">70-74 ára</a>
          <a class="dropdown-item" href="#">75-79 ára</a>
          <a class="dropdown-item" href="#">80-84 ára</a>
          <a class="dropdown-item" href="#">85-89 ára</a>
          <a class="dropdown-item" href="#">90-94 ára</a>
        </div>
      </div>
    </div>
    <div v-if="loading">
      <hr />
      <pulse-loader
        :loading="loading"
        :color="color"
        :size="size"
      ></pulse-loader>
    </div>
    <br>
    <div v-if="!loading">
      <table
        class="table table-striped table-hover table-responsive-sm table-sm"
      >
        <!--<caption>Listi yfir íslandsmeta</caption>-->
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col">Grein</th>
            <th scope="col">Methafi</th>
            <th scope="col">Árangur</th>
            <th scope="col">Vindur</th>
            <th scope="col">Úti/Inni</th>
            <th scope="col">Dags.</th>
            <th scope="col">Aldursfl.</th>
            <th scope="col">Félag</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in record_data">
            <th scope="row">{{ i.Event }}</th>
            <td>
              <router-link
                :to="{
                  name: 'CompetitorProfile',
                  params: { competitorID: i.CompetitorID },
                }"
              >
                <a>{{ i.Name }}</a>
              </router-link>
            </td>
            <td>
              {{ i.Results_text }}
              <small class="text-muted">{{ i.Units_symbol }}</small>
            </td>
            <td>{{ i.Wind }}</td>
            <td>{{ inout_text(i.Inout) }}</td>
            <td>{{ i.Date }}</td>
            <td>{{ i.AgeGroup }}</td>
            <td>{{ i.Club }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "IslmetList",
  components: {
    PulseLoader,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      loading: true,
      agegroup_text: "Aldursflokkar",
      record_data: []
    };
  },
  created() {
    this.get_data();
  },
  methods: {
    inout_text: function (inout) {
      if (inout === 0) {
        return "Úti";
      } else {
        return "Inni";
      }
    },
    get_data: function () {
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.record_data = [];
      //console.log('Getting data')

      var url = "/api/records/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.record_data = response[0]["data"];
            //console.log("Got data");
          })
        )
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          console.log("Error getting data");
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
  //   mounted() {
  //}
};
</script>

<style scoped>
.table {
  margin-bottom: 0;
}
.td {
  text-align: center;
  vertical-align: middle;
}
.display-4 {
  margin-top: 1rem;
}

/* center spinner */
.v-spinner {
  text-align: center;
}
</style>