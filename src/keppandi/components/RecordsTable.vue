<template>
  <div>
    <div v-if="loading">
      <hr />
      <pulse-loader
        :loading="loading"
        :color="color"
        :size="size"
      ></pulse-loader>
    </div>
    <div v-if="showRecordsTable">
      <hr />
      <h2 class="display-4">
        <!-- Font size er 3.5 rem í Display-4 sem er 56px-->
        <img src="./ISL_Flag.svg" alt="Íslenski fáninn" height="56px" />
        Íslandsmet
      </h2>
      <h4>
        Fjöldi skráðra Íslandsmeta er {{ nrRecords }} þar af eru
        {{ nrActiveRecords }} virk og {{ nrUnActiveRecords }} óvirk.
      </h4>
      <!-- VIRK MET -->
      <div v-show="showActiveRecordsTable">
        <h5>Virk met</h5>
        <table
          class="table table-striped table-hover table-responsive-sm table-sm"
        >
        <!--<caption>Listi yfir virk Íslandsmet</caption>-->
          <col span="1" class="wide" />
          <thead>
            <tr>
              <th scope="col" @click="sort('Event')">
                <i class="fas fa-sort"></i>&nbsp;Grein
              </th>
              <th scope="col" @click="sort('Results')">
                <i class="fas fa-sort"></i>&nbsp;Árangur
              </th>
              <th scope="col" @click="sort('Wind')">
                <i class="fas fa-sort"></i>&nbsp;Vindur
              </th>
              <th scope="col" @click="sort('inout')">
                <i class="fas fa-sort"></i>&nbsp;Úti/Inni
              </th>
              <th scope="col" @click="sort('Date')">
                <i class="fas fa-sort"></i>&nbsp;Dags.
              </th>
              <th scope="col" @click="sort('Age')">
                <i class="fas fa-sort"></i>&nbsp;Aldur
              </th>
              <th scope="col" @click="sort('AgeGroup')">
                <i class="fas fa-sort"></i>&nbsp;Aldursfl.
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(i, index) in sortedDataActive"
              v-show="index < 5 || showAllActiveRecords"
            >
              <th scope="row">{{ i.Event }} <small class="text-muted">{{ i.Units_symbol }}</small></th>
              <td>{{ i.Results_text }}</td>
              <td>{{ i.Wind }}</td>
              <td>{{ inout_text(i.Inout) }}</td>
              <td>{{ i.Date }}</td>
              <td>{{ i.Age }}</td>
              <td>{{ i.AgeGroup }}</td>
            </tr>
          </tbody>
        </table>
        <a
          href="#"
          v-on:click.prevent="toggle_ActiveRecords($event)"
          v-if="showMoreLessButtonActive"
          class="text-success"
          ><b><span v-html="textMoreLessActive"></span></b></a
        >
        <p>
          <br />
        </p>
      </div>
      <!-- ÓVIRK MET -->
      <div v-show="showunActiveRecordsTable">
        <h5>Óvirk met</h5>
        <table
          class="table table-striped table-hover table-responsive-sm table-sm"
        >
        <!--<caption>Listi yfir óvirk Íslandsmet</caption>-->
          <col span="1" class="wide" />
          <thead>
            <tr>
              <th scope="col" @click="sort('Event')">
                <i class="fas fa-sort"></i>&nbsp;Grein
              </th>
              <th scope="col" @click="sort('Results')">
                <i class="fas fa-sort"></i>&nbsp;Árangur
              </th>
              <th scope="col" @click="sort('Wind')">
                <i class="fas fa-sort"></i>&nbsp;Vindur
              </th>
              <th scope="col" @click="sort('inout')">
                <i class="fas fa-sort"></i>&nbsp;Úti/Inni
              </th>
              <th scope="col" @click="sort('Date')">
                <i class="fas fa-sort"></i>&nbsp;Dags.
              </th>
              <th scope="col" @click="sort('Age')">
                <i class="fas fa-sort"></i>&nbsp;Aldur
              </th>
              <th scope="col" @click="sort('AgeGroup')">
                <i class="fas fa-sort"></i>&nbsp;Aldursfl.
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(i, index) in sortedDataunActive"
              v-show="index < 5 || showAllunActiveRecords"
            >
              <th scope="row">{{ i.Event }} <small class="text-muted">{{ i.Units_symbol }}</small></th>
              <td>{{ i.Results_text }}</td>
              <td>{{ i.Wind }}</td>
              <td>{{ inout_text(i.Inout) }}</td>
              <td>{{ i.Date }}</td>
              <td>{{ i.Age }}</td>
              <td>{{ i.AgeGroup }}</td>
            </tr>
          </tbody>
        </table>
        <a
          href="#"
          v-on:click.prevent="toggle_unActiveRecords($event)"
          v-if="showMoreLessButtonunActive"
          class="text-success"
          ><b><span v-html="textMoreLessunActive"></span></b></a
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  props: ["competitorID"],
  components: {
    PulseLoader,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      currentSort: "Age",
      currentSortDir: "desc",
      showAllActiveRecords: false,
      showAllunActiveRecords: false,
      record_data: [],

      showMoreLessButtonActive: false,
      showMoreLessButtonunActive: false,
      showRecordsTable: false,
      showActiveRecordsTable: false,
      showunActiveRecordsTable: false,
      loading: true,

      nrRecords: 0,
      nrActiveRecords: 0,
      nrUnActiveRecords: 0,
    };
  },
  created() {
    this.Get_Records_Data();
  },
  computed: {
    textMoreLessActive: function () {
      if (this.showAllActiveRecords == false) {
        return '<i class="fas fa-caret-down"></i> Sýna fleiri virk met';
      } else {
        return '<i class="fas fa-caret-up"></i> Sýna færri virk met';
      }
    },
    textMoreLessunActive: function () {
      if (this.showAllunActiveRecords == false) {
        return '<i class="fas fa-caret-down"></i> Sýna fleiri óvirk met';
      } else {
        return '<i class="fas fa-caret-up"></i> Sýna færri óvirk met';
      }
    },
    activeRecords: function () {
      let data = [];
      let dataLen = this.record_data.length;

      this.nrRecords = dataLen;

      for (var i = 0; i < dataLen; i++) {
        if (this.record_data[i].isActive == true) {
          data.push(this.create_result_text(this.record_data[i]));
        }
      }

      //console.log(data.length);
      if (data.length > 0) {
        this.showActiveRecordsTable = true;
      }

      if (data.length > 5) {
        this.showMoreLessButtonActive = true;
      }

      this.nrActiveRecords = data.length;
      return data;
    },
    unactiveRecords: function () {
      let data = [];
      let dataLen = this.record_data.length;

      for (var i = 0; i < dataLen; i++) {
        if (this.record_data[i].isActive == false) {
          data.push(this.create_result_text(this.record_data[i]));
        }
      }

      if (data.length > 0) {
        this.showunActiveRecordsTable = true;
      }

      if (data.length > 5) {
        this.showMoreLessButtonunActive = true;
      }

      this.nrUnActiveRecords = data.length;
      return data;
    },
    sortedDataunActive: function () {
      //console.log("Sorting data");
      return this.unactiveRecords.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === "desc") modifier = -1;

        if (
          this.currentSort == "Results" ||
          this.currentSort == "Wind" ||
          this.currentSort == "Age"
        ) {
          if (parseFloat(a[this.currentSort]) < parseFloat(b[this.currentSort]))
            return -1 * modifier;
          if (parseFloat(a[this.currentSort]) > parseFloat(b[this.currentSort]))
            return 1 * modifier;
        } else {
          if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
          if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        }

        return 0;
      });
    },
    sortedDataActive: function () {
      //console.log("Sorting data");
      return this.activeRecords.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === "desc") modifier = -1;

        if (
          this.currentSort == "Results" ||
          this.currentSort == "Wind" ||
          this.currentSort == "Age"
        ) {
          if (parseFloat(a[this.currentSort]) < parseFloat(b[this.currentSort]))
            return -1 * modifier;
          if (parseFloat(a[this.currentSort]) > parseFloat(b[this.currentSort]))
            return 1 * modifier;
        } else {
          if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
          if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        }

        return 0;
      });
    },
  },
  methods: {
    create_result_text: function (data) {
      //0, # No units!
      //'metrar': 1, # Meters
      //'sek.': 2, # ss,dd
      //'mín.': 3, # mm:ss
      //'klst.': 4, # hh:mm:ss,dd
      //'stig': 5, # Points
      //'Ungl.stig': 6 # Points junior
      if (data["Units"] == 3) {
        data["Results_text"] = moment.unix(data["Results"]).format("mm:ss,SS");
      } else if (data["Units"] == 4) {
        data["Results_text"] = moment
          .unix(data["Results"])
          .format("hh:mm:ss,SS");
      } else if (data["Units"] == 5 || data["Units"] == 6) {
        data["Results_text"] = parseFloat(data["Results"]).toFixed(0);
      } else {
        if (data["Electronic_timing"] == 0 && data["Units"] == 2) {
          data["Results_text"] = parseFloat(data["Results"]).toFixed(1);
        } else {
          data["Results_text"] = parseFloat(data["Results"]).toFixed(2);
        }
      }

      return data;
    },
    inout_text: function (inout) {
      if (inout === 0) {
        return "Úti";
      } else {
        return "Inni";
      }
    },
    toggle_ActiveRecords: function (event) {
      this.showAllActiveRecords = !this.showAllActiveRecords;
    },
    toggle_unActiveRecords: function (event) {
      this.showAllunActiveRecords = !this.showAllunActiveRecords;
    },
    sort: function (s) {
      //if s == current sort, reverse
      if (s === this.currentSort) {
        this.currentSortDir = this.currentSortDir === "asc" ? "desc" : "asc";
      }
      this.currentSort = s;

      //console.log("Sort");
      //console.log(this.currentSort);
      //console.log(this.currentSortDir);
    },
    Get_Records_Data: function () {
      this.record_data = [];

      var url = "/api/records/" + this.competitorID + "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.record_data = response[0]["data"];
            //console.log("Got records data");
            //console.log(this.record_data);
          })
        )
        .catch((error) => {
          console.log("Error getting records data.");
          this.showRecordsTable = false;
        })
        .finally(() => {
          //console.log("Finally");
          this.loading = false;
          if (this.record_data.length > 0) {
            this.showRecordsTable = true;
          }
          if (this.record_data.length > 5) {
            this.showMoreLessButton = true;
          }
        });
    },
  },
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