<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div v-if="isReady">
      {{competitor_info.FirstName}} {{event_info.ShortName}}
      <div class="card">
        <div class="card-header">
          <ul class="nav nav-tabs card-header-tabs pull-right" id="myTab" role="tablist">
            <li class="nav-item">
              <a
                class="nav-link active"
                id="home-tab"
                data-toggle="tab"
                href="#home"
                role="tab"
                aria-controls="home"
                aria-selected="true"
              ><i class="fas fa-chart-line"></i> Ársbest</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="profile-tab"
                data-toggle="tab"
                href="#profile"
                role="tab"
                aria-controls="profile"
                aria-selected="false"
              ><i class="fas fa-chart-line"></i> Tímaröð</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="contact-tab"
                data-toggle="tab"
                href="#contact"
                role="tab"
                aria-controls="contact"
                aria-selected="false"
              ><i class="fas fa-chart-line"></i> Bætingar</a>
            </li>
          </ul>
        </div>
        <div class="card-body">
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="home"
              role="tabpanel"
              aria-labelledby="home-tab">
              <yearchart :alldata="yearAllData"></yearchart>
              </div>
            <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
              <timeserieschart :data="timeData"></timeserieschart>
            </div>
            <div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
              ...
            </div>
          </div>
        </div>
      </div>
      <table class="table table-striped table-hover table-responsive-sm table-sm">
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col" @click="sort('Results')">
              <i class="fas fa-sort"></i>
              Árangur [{{event_info.Units_symbol}}]
            </th>
            <th scope="col" @click="sort('Wind')" v-bind:class="{'d-none': !hasWind}">
              <i class="fas fa-sort"></i> Vindur
            </th>
            <th scope="col" @click="sort('Date')">
              <i class="fas fa-sort"></i> Dags.
            </th>
            <th scope="col" @click="sort('Age')">
              <i class="fas fa-sort"></i> Aldur
            </th>
            <th scope="col" @click="sort('competition_name')">
              <i class="fas fa-sort"></i> Heiti móts
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in sortedData" v-show="(index < 5) || showAllEvents" :key="i.Event">
            <!-- v-bind:style="{display: 'none'}" -->
            <th scope="row">{{i.Results_text}}</th>
            <td v-bind:class="{'d-none': !hasWind}">{{i.Wind}}</td>
            <td>{{i.Date | formatDate}}</td>
            <td>{{i.Age}}</td>
            <td>
              <a
                v-bind:href="'http://mot.fri.is/MotFRI/SelectedCompetitionResults.aspx?Code=' + i.competition_id"
              >{{i.competition_name}}</a>
            </td>
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
import TimeSeriesChart from "./components/TimeSeriesChart.vue";
import YearChart from "./components/YearChart.vue";

export default {
  name: "KeppandiEvent",
  components: {
    //highcharts: Chart,
    timeserieschart: TimeSeriesChart,
    yearchart: YearChart,
    PulseLoader
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      competitorID: null,
      eventID: null,
      competitor_info: [],
      event_info: [],
      event_data: [],
      event_min: [],
      event_max: [],
      event_years: [],
      event_tooltip: [],
      isReady: false,
      showAllEvents: true,
      currentSort: "Results",
      currentSortDir: "desc",
      message: ""
    };
  },
  created() {
    this.competitorID = this.$route.params.competitorID;
    this.eventID = this.$route.params.eventID;
    this.get_data();
  },
  methods: {
    get_data: function() {
      this.$parent.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      var url = "/api/keppandi/" + this.competitorID + "/" + this.eventID + "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            console.log("Got data");
            console.log(console.log(response[0]["data"]["Max"]));
            this.competitor_info = response[0]["data"]["Competitor"];
            this.event_info = response[0]["data"]["EventInfo"];
            this.event_data = response[0]["data"]["EventData"];
            this.event_years = response[0]["data"]["Years"];
            this.event_min = response[0]["data"]["Min"];
            this.event_max = response[0]["data"]["Max"];
            this.event_tooltip = response[0]["data"]["Tooltip"];

            if (this.event_info.Minimize === true) {
              this.currentSortDir = "asc";
            } else {
              this.currentSortDir = "desc";
            }

            this.event_data = this.add_inndoor_sign(
              response[0]["data"]["EventData"]
            );

            //console.log("Got data 2");

            document.title =
              "Afrekaskrá FRÍ - " +
              this.competitor_info.FirstName +
              " " +
              this.competitor_info.LastName +
              " (" +
              this.competitor_info.Club +
              ")";
          })
        )
        .catch(error => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          document.title = "Afrekaskrá FRÍ";
        })
        .finally(() => {
          //this.$parent.loading = false;
          //document.title = this.titleText
          //this.$parent.do_stuff()
          this.isReady = true;
        });
    },
    add_inndoor_sign: function(my_data) {
      var dataLen = my_data.length;

      for (var i = 0; i < dataLen; i++) {
        if (my_data[i]["OutIn"] === 1) {
          my_data[i]["Results_text"] = my_data[i]["Results"] + " (i)";
        } else {
          my_data[i]["Results_text"] = my_data[i]["Results"];
        }
      }

      return my_data;
    },
    sort: function(s) {
      //if s == current sort, reverse
      if (s === this.currentSort) {
        this.currentSortDir = this.currentSortDir === "asc" ? "desc" : "asc";
      }
      this.currentSort = s;

      //console.log("Sort");
      //console.log(this.currentSort);
      //console.log(this.currentSortDir);
    }
  },
  computed: {
    hasWind: function() {
      if (this.event_info["HasWind"] === 1) {
        return true;
      } else {
        return false;
      }
    },
    // sortDataByDate: function() {
    //   //Highcharts wants the date sorted in ascending order
    //   return this.event_data.sort((a, b) => {
    //     let modifier = 1;
    //     if (moment(a["Date"]).valueOf() < moment(b["Date"]).valueOf())
    //       return -1 * modifier;
    //     if (moment(a["Date"]).valueOf() > moment(b["Date"]).valueOf())
    //       return 1 * modifier;
    //     return 0;
    //   });
    // },
    timeData: function() {
      let data_points = [];
      var dataLen = this.event_data.length;

      for (var i = 0; i < dataLen; i++) {
        data_points.push({
          x: moment(this.event_data[i]["Date"]).valueOf(),
          y: Number(this.event_data[i]["Results"])
        });
      }

      return data_points;
    },
    yearAllData: function() {
      let data_points = [];
      var dataLen = this.event_years.length;

      for (var i = 0; i < dataLen; i++) {
        console.log(this.event_tooltip[i]);
        if (this.event_info.Minimize === true) {
          data_points.push({
            x: this.event_years[i],
            y: this.event_min[i],
            label: this.event_tooltip[i]
          });
        } else {
          data_points.push({
            x: this.event_years[i],
            y: this.event_max[i],
            label: this.event_tooltip[i]
          });
        }
      }

      return data_points;
    },
    sortedData: function() {
      return this.event_data.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === "desc") modifier = -1;
        if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        return 0;
      });
    }
  }
};
</script>

<style scoped>
.v-spinner {
  text-align: center;
}

.td {
  text-align: center;
  vertical-align: middle;
}
</style>