<template>
  <div>
    <div class="card">
      <div class="card-header">
        <div class="row">
          <div class="col-sm">
            <div class="custom-control custom-radio">
              <input
                type="radio"
                id="InndoorRadio"
                name="InndoorOutdoorRadio"
                class="custom-control-input"
                value="1"
                v-on:change="inout_change($event)"
              />
              <label class="custom-control-label" for="InndoorRadio"
                >Innanhús</label
              >
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
              <label class="custom-control-label" for="OutdoorRadio"
                >Utanhús</label
              >
            </div>
          </div>
          <div class="col-sm">
            <div class="custom-control custom-radio">
              <input
                type="radio"
                id="MenRadio"
                name="MenWomenRadio"
                class="custom-control-input"
                value="1"
                v-on:change="gender_change($event)"
              />
              <label class="custom-control-label" for="MenRadio"
                >Karlar / Piltar</label
              >
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
              <label class="custom-control-label" for="WomenRadio"
                >Konur / Stúlkur</label
              >
            </div>
          </div>
          <div class="col-sm">
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
                <div
                  class="dropdown-menu"
                  aria-labelledby="btnGroupDrop1"
                  v-on:click="agegroup_change($event)"
                >
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
                <div class="dropdown-menu" aria-labelledby="btnGroupDrop2" v-on:click="agegroup_change($event)">
                  <a class="dropdown-item" href="#" id="8">30-34 ára</a>
                  <a class="dropdown-item" href="#" id="9">35-39 ára</a>
                  <a class="dropdown-item" href="#" id="10">40-44 ára</a>
                  <a class="dropdown-item" href="#" id="11">45-49 ára</a>
                  <a class="dropdown-item" href="#" id="12">50-54 ára</a>
                  <a class="dropdown-item" href="#" id="13">55-59 ára</a>
                  <a class="dropdown-item" href="#" id="14">60-64 ára</a>
                  <a class="dropdown-item" href="#" id="15">65-69 ára</a>
                  <a class="dropdown-item" href="#" id="16">70-74 ára</a>
                  <a class="dropdown-item" href="#" id="17">75-79 ára</a>
                  <a class="dropdown-item" href="#" id="18">80-84 ára</a>
                  <a class="dropdown-item" href="#" id="19">85-89 ára</a>
                  <a class="dropdown-item" href="#" id="20">90-94 ára</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body">
        <div v-if="loading">
          <hr />
          <pulse-loader
            :loading="loading"
            :color="color"
            :size="size"
          ></pulse-loader>
          <p style="text-align: center">{{ message }}</p>
        </div>
        <br />
        <div v-if="!loading">
          <h2 v-html="header_text"></h2>
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
                <th scope="col" v-show="inout === 0">Vindur</th>
                <!--<th class="d-none d-xl-table-cell" scope="col">Úti/Inni</th>-->
                <th class="d-none d-md-table-cell" scope="col">Dags.</th>
                <!--<th scope="col">Aldursfl.</th>-->
                <th class="d-none d-xl-table-cell" scope="col">Félag</th>
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
                <td v-show="inout === 0">{{ i.Wind }}</td>
                <!--<td class="d-none d-xl-table-cell">{{ inout_text(i.InOut) }}</td>-->
                <td class="d-none d-md-table-cell">{{ i.Date }}</td>
                <!--<td>{{ i.AgeGroup }}</td>-->
                <td class="d-none d-xl-table-cell">{{ i.Club }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
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
      loading_master: true,
      agegroup_value: 0,
      inout: 0,
      org_record_data: [],
      masters_record_data: [],
      gender: 2,
      message: "Næ í gögn ekki stökkva langt 😉",

      men_agegroups: [
        ["KA", "<i class='fas fa-male'></i> Karlar"],
        ["PI22", "<i class='fas fa-male'></i> Piltar 20-22 ára"],
        ["PI19", "<i class='fas fa-male'></i> Piltar 18-19 ára"],
        ["PI17", "<i class='fas fa-male'></i> Piltar 16-17 ára"],
        ["PI15", "<i class='fas fa-male'></i> Piltar 15 ára"],
        ["PI14", "<i class='fas fa-male'></i> Piltar 14 ára"],
        ["PI13", "<i class='fas fa-male'></i> Piltar 13 ára"],
        ["PI12", "<i class='fas fa-male'></i> Piltar 12 ára"],
      ],
      women_agegroups: [
        ["KO", "<i class='fas fa-female'></i> Konur"],
        ["ST22", "<i class='fas fa-female'></i> Stúlkur 20-22 ára"],
        ["ST19", "<i class='fas fa-female'></i> Stúlkur 18-19 ára"],
        ["ST17", "<i class='fas fa-female'></i> Stúlkur 16-17 ára"],
        ["ST15", "<i class='fas fa-female'></i> Stúlkur 15 ára"],
        ["ST14", "<i class='fas fa-female'></i> Stúlkur 14 ára"],
        ["ST13", "<i class='fas fa-female'></i> Stúlkur 13 ára"],
        ["ST12", "<i class='fas fa-female'></i> Stúlkur 12 ára"],
      ],
      master_mengroups: [
        ["KA030-34", "Öldungar - <i class='fas fa-male'></i> Karlar 30-34 ára"],
        ["KA035-39", "Öldungar - <i class='fas fa-male'></i> Karlar 35-39 ára"],
        ["KA040-44", "Öldungar - <i class='fas fa-male'></i> Karlar 40-44 ára"],
        ["KA045-49", "Öldungar - <i class='fas fa-male'></i> Karlar 45-49 ára"],
        ["KA050-54", "Öldungar - <i class='fas fa-male'></i> Karlar 50-54 ára"],
        ["KA055-59", "Öldungar - <i class='fas fa-male'></i> Karlar 55-59 ára"],
        ["KA060-64", "Öldungar - <i class='fas fa-male'></i> Karlar 60-64 ára"],
        ["KA065-69", "Öldungar - <i class='fas fa-male'></i> Karlar 65-69 ára"],
        ["KA070-74", "Öldungar - <i class='fas fa-male'></i> Karlar 70-74 ára"],
        ["KA075-79", "Öldungar - <i class='fas fa-male'></i> Karlar 75-79 ára"],
        ["KA080-84", "Öldungar - <i class='fas fa-male'></i> Karlar 80-84 ára"],
        ["KA085-89", "Öldungar - <i class='fas fa-male'></i> Karlar 85-89 ára"],
        ["KA090-94", "Öldungar - <i class='fas fa-male'></i> Karlar 90-94 ára"],
      ],
      master_womengroups: [
        ["KO030-34", "Öldungar - <i class='fas fa-female'></i> Konur 30-34 ára"],
        ["KO035-39", "Öldungar - <i class='fas fa-female'></i> Konur 35-39 ára"],
        ["KO040-44", "Öldungar - <i class='fas fa-female'></i> Konur 40-44 ára"],
        ["KO045-49", "Öldungar - <i class='fas fa-female'></i> Konur 45-49 ára"],
        ["KO050-54", "Öldungar - <i class='fas fa-female'></i> Konur 50-54 ára"],
        ["KO055-59", "Öldungar - <i class='fas fa-female'></i> Konur 55-59 ára"],
        ["KO060-64", "Öldungar - <i class='fas fa-female'></i> Konur 60-64 ára"],
        ["KO065-69", "Öldungar - <i class='fas fa-female'></i> Konur 65-69 ára"],
        ["KO070-74", "Öldungar - <i class='fas fa-female'></i> Konur 70-74 ára"],
        ["KO075-79", "Öldungar - <i class='fas fa-female'></i> Konur 75-79 ára"],
        ["KO080-84", "Öldungar - <i class='fas fa-female'></i> Konur 80-84 ára"],
        ["KO085-89", "Öldungar - <i class='fas fa-female'></i> Konur 85-89 ára"],
        ["KO090-94", "Öldungar - <i class='fas fa-female'></i> Konur 90-94 ára"],
      ],
    };
  },
  created() {
    this.get_data();
  },
  computed: {
    header_text() {
      return this.agegroup_text + " - " + this.inout_text_long;
    },
    inout_text_long() {
      if (this.inout === 0) {
        return "Utanhús";
      } else {
        return "Innanhús";
      }
    },
    agegroup() {
      if (this.gender === 1) {
        //men
        if (this.agegroup_value < this.men_agegroups.length) {
          return this.men_agegroups[this.agegroup_value][0];
        } else {
          return this.master_mengroups[
            this.agegroup_value - this.men_agegroups.length
          ][0];
        }
      } //women
      else {
        if (this.agegroup_value < this.women_agegroups.length) {
          return this.women_agegroups[this.agegroup_value][0];
        } else {
          return this.master_womengroups[
            this.agegroup_value - this.women_agegroups.length
          ][0];
        }
      }
    },
    agegroup_text() {
      if (this.gender === 1) {
        //men
        if (this.agegroup_value < this.men_agegroups.length) {
          return this.men_agegroups[this.agegroup_value][1];
        } else {
          return this.master_mengroups[
            this.agegroup_value - this.men_agegroups.length
          ][1];
        }
      } //women
      else {
        if (this.agegroup_value < this.women_agegroups.length) {
          return this.women_agegroups[this.agegroup_value][1];
        } else {
          return this.master_womengroups[
            this.agegroup_value - this.women_agegroups.length
          ][1];
        }
      }
    },
    record_data() {
      let record_list = [];
      //v-if="i.AgeGroup == agegroup && i.InOut == inout"
      /*         for (var i = 0; i < this.org_record_data.length; i++)
        {
            if ((this.org_record_data[i].AgeGroup === this.agegroup) && (this.org_record_data[i].InOut === this.inout))
            {
                record_list.push(this.org_record_data[i])
            }
        } */
        if (this.agegroup_value < this.men_agegroups.length) {
            return this.all_record_data;
        } else {
            return this.masters_record_data;
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
      this.agegroup_value = Number(event.originalTarget.id);
      if ((this.agegroup_value >= this.men_agegroups.length) && (this.loading_master == true)) {
          this.loading = true
      }
    },
    get_data: function () {
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.all_record_data = [];
      this.masters_record_data = [];
      //console.log('Getting data')

      var url = "/api/records/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.all_record_data = response[0]["data"];
            console.log("Got data");
          })
        )
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          console.log("Error getting data");
        })
        .finally(() => {
          this.loading = false;
        });

      var url = "/api/records/masters";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.masters_record_data = response[0]["data"];
            console.log("Got masters data");
          })
        )
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          console.log("Error getting data");
        })
        .finally(() => {
          this.loading_master = false;
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