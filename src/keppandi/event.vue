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
                id="bestbyyear-tab"
                data-toggle="tab"
                href="#bestbyyear"
                role="tab"
                aria-controls="bestbyyear"
                aria-selected="true"
                v-on:click="onTabClick"
              ><i class="fas fa-chart-line"></i> Ársbest</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="timeseries-tab"
                data-toggle="tab"
                href="#timeseries"
                role="tab"
                aria-controls="timeseries"
                aria-selected="false"
                v-on:click="onTabClick"
              ><i class="fas fa-chart-line"></i> Tímaröð</a>
            </li>
            <li class="nav-item">
              <a
                class="nav-link"
                id="progression-tab"
                data-toggle="tab"
                href="#progression"
                role="tab"
                aria-controls="progression"
                aria-selected="false"
                v-on:click="onTabClick"
              ><i class="fas fa-chart-line"></i> Bætingar</a>
            </li>
          </ul>
        </div>
        <div class="card-body">
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="bestbyyear"
              role="tabpanel"
              aria-labelledby="bestbyyear-tab">
              <yearchart :alldata="yearAllData" :legaldata="yearLegalData" ref="yearChart"></yearchart>
              </div>
            <div class="tab-pane fade" id="timeseries" role="tabpanel" aria-labelledby="timeseries-tab">
              <timeserieschart :data="timeData" ref="timeChart"></timeserieschart>
            </div>
            <div class="tab-pane fade" id="progression" role="tabpanel" aria-labelledby="progression-tab">
              <progressionchart :data="progressionData" ref="progressionChart"></progressionchart>
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
import ProgressionChart from "./components/ProgressionChart.vue";

export default {
  name: "KeppandiEvent",
  components: {
    //highcharts: Chart,
    timeserieschart: TimeSeriesChart,
    yearchart: YearChart,
    progressionchart: ProgressionChart,
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
      event_min_all: [],
      event_max_all: [],
      event_years_all: [],
      event_tooltip_all: [],

      event_min_legal: [],
      event_max_legal: [],
      event_years_legal: [],
      event_tooltip_legal: [],

      progression_dates : [],
      progression_pbs: [],
      progression_tooltips: [],

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
    onTabClick(event) {
      //Redraw the graphs on tab click.
      //console.log('TabClick 1')
      this.$refs.yearChart.$refs.chart.chart.xAxis[0].isDirty = true;
      this.$refs.yearChart.$refs.chart.chart.redraw();
      this.$refs.yearChart.$refs.chart.chart.update({});
      this.$refs.yearChart.$refs.chart.chart.reflow();

      this.$refs.timeChart.$refs.chart.chart.xAxis[0].isDirty = true;
      this.$refs.timeChart.$refs.chart.chart.redraw();
      this.$refs.timeChart.$refs.chart.chart.update({});
      this.$refs.timeChart.$refs.chart.chart.reflow();

      this.$refs.progressionChart.$refs.chart.chart.xAxis[0].isDirty = true;
      this.$refs.progressionChart.$refs.chart.chart.redraw();
      this.$refs.progressionChart.$refs.chart.chart.update({});
      this.$refs.progressionChart.$refs.chart.chart.reflow();
      //console.log('TabClick 2')
    },
    get_data: function() {
      this.$parent.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      var url = "/api/keppandi/" + this.competitorID + "/" + this.eventID + "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            //console.log("Got data");
            //console.log(console.log(response[0]["data"]["Max"]));
            this.competitor_info = response[0]["data"]["Competitor"];
            this.event_info = response[0]["data"]["EventInfo"];
            this.event_data = response[0]["data"]["EventData"];

            this.event_years_all = response[0]["data"]["Years_all"];
            this.event_min_all = response[0]["data"]["Min_all"];
            this.event_max_all = response[0]["data"]["Max_all"];
            this.event_tooltip_all = response[0]["data"]["Tooltip_all"];

            this.event_years_legal = response[0]["data"]["Years_legal"];
            this.event_min_legal = response[0]["data"]["Min_legal"];
            this.event_max_legal = response[0]["data"]["Max_legal"];
            this.event_tooltip_legal = response[0]["data"]["Tooltip_legal"];

            this.progression_dates = response[0]["data"]["PB_dates"];
            this.progression_pbs = response[0]["data"]["PBs"];
            this.progression_tooltips = response[0]["data"]["PB_tooltip"];

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
    progressionData: function() {
      let data_points = [];
      var dataLen = this.progression_dates.length;

      for (var i = 0; i < dataLen; i++) {
        data_points.push({
          x: moment(this.progression_dates[i]).valueOf(),
          y: this.progression_pbs[i],
          label: this.progression_tooltips[i]
        });
      }

      console.log(data_points)

      return data_points;
    },
    yearAllData: function() {
      let data_points = [];
      var dataLen = this.event_years_all.length;

      for (var i = 0; i < dataLen; i++) {
        //console.log(this.event_tooltip[i]);
        if (this.event_info.Minimize === true) {
          data_points.push({
            x: this.event_years_all[i],
            y: this.event_min_all[i],
            label: this.event_tooltip_all[i]
          });
        } else {
          data_points.push({
            x: this.event_years_all[i],
            y: this.event_max_all[i],
            label: this.event_tooltip_all[i]
          });
        }
      }

      return data_points;
    },
    yearLegalData: function() {
      let data_points = [];
      var dataLen = this.event_years_legal.length;

      for (var i = 0; i < dataLen; i++) {
        //console.log(this.event_tooltip[i]);
        if (this.event_info.Minimize === true) {
          data_points.push({
            x: this.event_years_legal[i],
            y: this.event_min_legal[i],
            label: this.event_tooltip_legal[i]
          });
        } else {
          data_points.push({
            x: this.event_years_legal[i],
            y: this.event_max_legal[i],
            label: this.event_tooltip_legal[i]
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