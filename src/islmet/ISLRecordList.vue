<template>
  <div>
    <div class="custom-control custom-radio">
      <input
        type="radio"
        id="InndoorRadio"
        name="InndoorOutdoorRadio"
        class="custom-control-input"
        value="1"
        v-on:change="inout_change($event)"
      />
      <label class="custom-control-label" for="InndoorRadio">Innanhús</label>
    </div>
    <div class="custom-control custom-radio">
      <input
        type="radio"
        id="OutdoorRadio"
        name="InndoorOutdoorRadio"
        class="custom-control-input"
        value="0"
        v-on:change="inout_change($event)"
        checked
      />
      <label class="custom-control-label" for="OutdoorRadio">Utanhús</label>
    </div>
    <br />
    <div class="custom-control custom-radio">
      <input
        type="radio"
        id="MenRadio"
        name="MenWomenRadio"
        class="custom-control-input"
        value="1"
        v-on:change="gender_change($event)"
      />
      <label class="custom-control-label" for="MenRadio">Karlar/Piltar</label>
    </div>
    <div class="custom-control custom-radio">
      <input
        type="radio"
        id="WomenRadio"
        name="MenWomenRadio"
        class="custom-control-input"
        value="2"
        v-on:change="gender_change($event)"
        checked
      />
      <label class="custom-control-label" for="WomenRadio">Konur/Stúlkur</label>
    </div>
    <div
      class="btn-toolbar"
      role="toolbar"
      aria-label="Tækjastika"
      style="text-align: center; display: block"
    >
      <div
        class="btn-group mr-2"
        role="group"
        aria-label="Valmynd fyrir aldursflokk"
      >
        <button
          id="btnGroupDrop1"
          type="button"
          class="btn btn-secondary dropdown-toggle"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          Aldursflokkur
        </button>
        <div class="dropdown-menu" aria-labelledby="btnGroupDrop1" v-on:click="agegroup_change($event)">
          <a class="dropdown-item" href="#" id="0">Fullorðnir</a>
          <a class="dropdown-item" href="#" id="1">20-22 ára</a>
          <a class="dropdown-item" href="#" id="2">18-19 ára</a>
          <a class="dropdown-item" href="#" id="3">16-17 ára</a>
          <a class="dropdown-item" href="#" id="4">15 ára</a>
          <a class="dropdown-item" href="#" id="5">14 ára</a>
          <a class="dropdown-item" href="#" id="6">13 ára</a>
          <a class="dropdown-item" href="#" id="7">12 ára</a>
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
    <br />
    <div v-if="!loading">
      <h1>{{ header_text }}</h1>
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
            <!--<th scope="col">Aldursfl.</th>-->
            <th scope="col">Félag</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(i, index) in record_data"
            v-if="i.AgeGroup == agegroup && i.InOut == inout"
          >
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
              {{ i.Results }}
              <small class="text-muted">{{ i.Units_symbol }}</small>
            </td>
            <td>{{ i.Wind }}</td>
            <td>{{ inout_text(i.InOut) }}</td>
            <td>{{ i.Date }}</td>
            <!--<td>{{ i.AgeGroup }}</td>-->
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
      agegroup_value: 0,
      inout: 0,
      record_data: [],
      gender: 2,

      men_agegroups: [
        ["KA", "Karlar"],
        ["PI22", "Piltar 20-22 ára"],
        ["PI19", "Piltar 18-19 ára"],
        ["PI17", "Piltar 16-17 ára"],
        ["PI15", "Piltar 15 ára"],
        ["PI14", "Piltar 14 ára"],
        ["PI13", "Piltar 13 ára"],
        ["PI12", "Piltar 12 ára"],
      ],
      women_agegroups: [
        ["KO", "Konur"],
        ["ST22", "Stúlkur 20-22 ára"],
        ["ST19", "Stúlkur 18-19 ára"],
        ["ST17", "Stúlkur 16-17 ára"],
        ["ST15", "Stúlkur 15 ára"],
        ["ST14", "Stúlkur 14 ára"],
        ["ST13", "Stúlkur 13 ára"],
        ["ST12", "Stúlkur 12 ára"],
      ],
      master_mengroups: [
        ["KA030-34", "Öldungar Karlar 30-34 ára"],
        ["KA035-39", "Öldungar Karlar 35-39 ára"],
        ["KA040-44", "Öldungar Karlar 40-44 ára"],
        ["KA045-49", "Öldungar Karlar 45-49 ára"],
        ["KA050-54", "Öldungar Karlar 50-54 ára"],
        ["KA055-59", "Öldungar Karlar 55-59 ára"],
        ["KA060-64", "Öldungar Karlar 60-64 ára"],
        ["KA065-69", "Öldungar Karlar 65-69 ára"],
        ["KA070-74", "Öldungar Karlar 70-74 ára"],
        ["KA075-79", "Öldungar Karlar 75-79 ára"],
        ["KA080-84", "Öldungar Karlar 80-84 ára"],
        ["KA085-89", "Öldungar Karlar 85-89 ára"],
        ["KA090-94", "Öldungar Karlar 90-94 ára"],
      ],
      master_womengroups: [
        ["KO030-34", "Öldungar Konur 30-34 ára"],
        ["KO035-39", "Öldungar Konur 35-39 ára"],
        ["KO040-44", "Öldungar Konur 40-44 ára"],
        ["KO045-49", "Öldungar Konur 45-49 ára"],
        ["KO050-54", "Öldungar Konur 50-54 ára"],
        ["KO055-59", "Öldungar Konur 55-59 ára"],
        ["KO060-64", "Öldungar Konur 60-64 ára"],
        ["KO065-69", "Öldungar Konur 65-69 ára"],
        ["KO070-74", "Öldungar Konur 70-74 ára"],
        ["KO075-79", "Öldungar Konur 75-79 ára"],
        ["KO080-84", "Öldungar Konur 80-84 ára"],
        ["KO085-89", "Öldungar Konur 85-89 ára"],
        ["KO090-94", "Öldungar Konur 90-94 ára"],
      ],
    };
  },
  created() {
    this.get_data();
  },
  computed: {
    header_text() {
      return this.agegroup_text + " " + this.inout_text_long;
    },
    inout_text_long() {
      if (this.inout === 0) {
        return "Utanhús";
      } else {
        return "Innanhús";
      }
    },
    agegroup() {
        if (this.gender === 1) { //men
            return this.men_agegroups[this.agegroup_value][0]
        } else //women
        {
            return this.women_agegroups[this.agegroup_value][0]
        }
    },
    agegroup_text() {
        if (this.gender === 1) { //men
            return this.men_agegroups[this.agegroup_value][1]
        } else //women
        {
            return this.women_agegroups[this.agegroup_value][1]
        }
    },
  },
  methods: {
    inout_text: function (inout) {
      if (inout === 0) {
        return "Úti";
      } else {
        return "Inni";
      }
    },
    inout_change: function (event) {
      this.inout = Number(event.target.value);
    },
    gender_change: function (event) {
      this.gender = Number(event.target.value);
    },
    agegroup_change: function (event) {
        console.log(event)
      this.agegroup_value = Number(event.originalTarget.id);
      console.log(this.agegroup_value)
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