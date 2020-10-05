<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader
        :loading="!isReady"
        :color="color"
        :size="size"
      ></pulse-loader>
      <p style="text-align: center">{{ message }}</p>
      <img src="../fri-loading.gif" alt="Hleð síðu" width=100%>
    </div>
    <div v-if="isReady">
      <div class="d-flex flex-row">
        <div class="p-2">
          <router-link
            :to="{
              name: 'CompetitorProfile',
              params: { competitorID: competitorID },
            }"
          >
            <img
              class="rounded-circle img-thumbnail img-profile"
              v-bind:src="'/api/img/profile/' + competitorID"
            />
          </router-link>
        </div>
        <div class="p-2 align-self-center">
          <h3 style="font-size: 2.5vw">
            <i
              class="fas"
              v-bind:class="{
                'fa-male': competitor_info.Sex == 1,
                'fa-female': competitor_info.Sex == 2,
              }"
            ></i>
            <b
              >{{ competitor_info.FirstName }} {{ competitor_info.LastName }}</b
            >
            <font style="font-size: 1.75vw" class="text-muted"
              >- {{ competitor_info.Club }} ({{ competitor_info.YOB }})</font
            >
          </h3>
          <h4 style="font-size: 1.75vw">{{ event_info.Name_ISL }}</h4>
        </div>
      </div>
      <div class="d-flex flex-row">
        <h5>
          <router-link
            :to="{
              name: 'CompetitorProfile',
              params: { competitorID: competitorID },
            }"
          >
            <i class="fas fa-user-circle"></i> Fara á prófíl síðu keppanda
          </router-link>
        </h5>
      </div>
      <div class="card">
        <div class="card-header">
          <ul
            class="nav nav-tabs card-header-tabs pull-right"
            id="myTab"
            role="tablist"
          >
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
              >
                <i class="fas fa-chart-line"></i> Ársbest
              </a>
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
              >
                <i class="fas fa-chart-line"></i> Tímaröð
              </a>
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
              >
                <i class="fas fa-chart-line"></i> Bætingar
              </a>
            </li>
            <!--           <li class="nav-item">
              <a
                class="nav-link"
                id="back-tab"
                data-toggle="tab"
                role="tab"
                aria-controls="back"
                aria-selected="false"
                v-on:click="onBackClick"
                v-bind:href="'/keppandi/' + competitorID"
              >
                <i class="fas fa-user-circle"></i> Prófíl
              </a>
            </li>-->
          </ul>
        </div>
        <div class="card-body">
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="bestbyyear"
              role="tabpanel"
              aria-labelledby="bestbyyear-tab"
            >
              <yearchart
                :alldata="yearAllData"
                :legaldata="yearLegalData"
                :event_info="event_info"
                ref="yearChart"
                v-if="showYearChart"
              ></yearchart>
            </div>
            <div
              class="tab-pane fade"
              id="timeseries"
              role="tabpanel"
              aria-labelledby="timeseries-tab"
            >
              <timeserieschart
                :data="timeData"
                :event_info="event_info"
                :competitorID="competitorID"
                :eventID="eventID"
                ref="timeChart"
                v-if="showTimeChart"
              ></timeserieschart>
            </div>
            <div
              class="tab-pane fade"
              id="progression"
              role="tabpanel"
              aria-labelledby="progression-tab"
            >
              <progressionchart
                :data="progressionData"
                :event_info="event_info"
                ref="progressionChart"
                v-if="showProgressionChart"
              ></progressionchart>
            </div>
          </div>
        </div>
      </div>
      <achievementtable
        :event_info="event_info"
        :showAllEvents="showAllEvents"
        :event_data="event_data"
      ></achievementtable>
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
import AchievementTable from "./components/AchievementTable.vue";

export default {
  name: "KeppandiEvent",
  components: {
    //highcharts: Chart,
    timeserieschart: TimeSeriesChart,
    yearchart: YearChart,
    progressionchart: ProgressionChart,
    achievementtable: AchievementTable,
    PulseLoader,
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
      event_tooltip_all_max: [],
      event_tooltip_all_min: [],

      event_min_legal: [],
      event_max_legal: [],
      event_years_legal: [],
      event_tooltip_legal_max: [],
      event_tooltip_legal_min: [],

      progression_dates: [],
      progression_pbs: [],
      progression_tooltips: [],

      isReady: false,
      showAllEvents: true,
      message: "",

      showTimeChart: false,
      showYearChart: true,
      showProgressionChart: false,
    };
  },
  created() {
    this.competitorID = this.$route.params.competitorID;
    this.eventID = this.$route.params.eventID;
    this.get_data();
  },
  methods: {
    onBackClick(event) {
      this.$router.push({ path: `/keppandi/${this.competitorID}` });
    },
    onTabClick(event) {
      //Redraw the graphs on tab click.
      //console.log(event.target.id);

      if (event.target.id == "timeseries-tab") {
        this.showTimeChart = true;

        //this.$refs.timeChart.$refs.chart.chart.xAxis[0].isDirty = true;
        //this.$refs.timeChart.$refs.chart.chart.redraw();
        //this.$refs.timeChart.$refs.chart.chart.update({});
        //this.$refs.timeChart.$refs.chart.chart.reflow();
      } //else {
      //this.showTimeChart = false
      //}

      if (event.target.id == "bestbyyear-tab") {
        this.showYearChart = true;

        //this.$refs.yearChart.$refs.chart.chart.xAxis[0].isDirty = true;
        //this.$refs.yearChart.$refs.chart.chart.redraw();
        //this.$refs.yearChart.$refs.chart.chart.update({});
        //this.$refs.yearChart.$refs.chart.chart.reflow();
      } //else {
      //this.showYearChart = false
      //}

      if (event.target.id == "progression-tab") {
        this.showProgressionChart = true;

        //this.$refs.progressionChart.$refs.chart.chart.xAxis[0].isDirty = true;
        //this.$refs.progressionChart.$refs.chart.chart.redraw();
        //this.$refs.progressionChart.$refs.chart.chart.update({});
        //this.$refs.progressionChart.$refs.chart.chart.reflow();
      } //else {
      //this.showProgressionChart = false
      //}
    },
    get_data: function () {
      this.$parent.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      var url =
        "/api/competitor/" + this.competitorID + "/" + this.eventID + "/";
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
            this.event_tooltip_all_max = response[0]["data"]["Tooltip_all_max"];
            this.event_tooltip_all_min = response[0]["data"]["Tooltip_all_min"];

            this.event_years_legal = response[0]["data"]["Years_legal"];
            this.event_min_legal = response[0]["data"]["Min_legal"];
            this.event_max_legal = response[0]["data"]["Max_legal"];
            this.event_tooltip_legal_max =
              response[0]["data"]["Tooltip_legal_max"];
            this.event_tooltip_legal_min =
              response[0]["data"]["Tooltip_legal_min"];

            this.progression_dates = response[0]["data"]["PB_dates"];
            this.progression_pbs = response[0]["data"]["PBs"];
            this.progression_tooltips = response[0]["data"]["PB_tooltip"];

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
        .catch((error) => {
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
    add_inndoor_sign: function (my_data) {
      var dataLen = my_data.length;
      let strPost = "";

      for (var i = 0; i < dataLen; i++) {
        if (my_data[i]["OutIn"] === 1) {
          strPost = " (i)";
        } else {
          strPost = "";
        }

        if (this.event_info["Units"] == 3) {
          my_data[i]["Results_text"] =
            moment.unix(my_data[i]["Results"]).format("mm:ss,SS") + strPost;
          //my_data[i]["Results"] = my_data[i]["Results"] * 10000; // Convert to ms for highcharts
        } else if (this.event_info["Units"] == 4) {
          my_data[i]["Results_text"] =
            moment.unix(my_data[i]["Results"]).format("hh:mm:ss,SS") + strPost;
        } else {
          my_data[i]["Results_text"] = my_data[i]["Results"] + strPost;
        }
      }

      return my_data;
    },
  },
  computed: {
    timeData: function () {
      let data_points = [];
      var dataLen = this.event_data.length;
      let factor = 1;

      if (this.event_info["Units"] == 3 || this.event_info["Units"] == 4) {
        factor = 1000; // Highcharts wants time axis data in ms
      }

      for (var i = 0; i < dataLen; i++) {
        data_points.push({
          x: moment(this.event_data[i]["Date"]).valueOf(),
          y: Number(this.event_data[i]["Results"]) * factor, //Tryggja að þetta sé tala, annars fer Highcharts í fýlu.
        });
      }

      return data_points;
    },
    progressionData: function () {
      let data_points = [];
      var dataLen = this.progression_dates.length;
      let factor = 1;

      if (this.event_info["Units"] == 3 || this.event_info["Units"] == 4) {
        factor = 1000; // Highcharts wants time axis data in ms
      }

      for (var i = 0; i < dataLen; i++) {
        data_points.push({
          x: moment(this.progression_dates[i]).valueOf(),
          y: this.progression_pbs[i] * factor,
          label: this.progression_tooltips[i],
        });
      }

      //console.log(data_points)

      return data_points;
    },
    yearAllData: function () {
      let data_points = [];
      var dataLen = this.event_years_all.length;
      let factor = 1;

      if (this.event_info["HasWind"] == false) {
        return [];
      }

      if (this.event_info["Units"] == 3 || this.event_info["Units"] == 4) {
        factor = 1000; // Highcharts wants time axis data in ms
      }

      for (var i = 0; i < dataLen; i++) {
        //console.log(this.event_tooltip[i]);
        if (this.event_info.Minimize === true) {
          let c =
            this.event_min_all[i] === null
              ? null
              : this.event_min_all[i] * factor;
          data_points.push({
            x: this.event_years_all[i],
            y: c,
            label: this.event_tooltip_all_min[i],
          });
        } else {
          let c =
            this.event_max_all[i] === null
              ? null
              : this.event_max_all[i] * factor;
          data_points.push({
            x: this.event_years_all[i],
            y: c,
            label: this.event_tooltip_all_max[i],
          });
        }
      }

      return data_points;
    },
    yearLegalData: function () {
      let data_points = [];
      var dataLen = this.event_years_legal.length;
      let factor = 1;

      if (this.event_info["Units"] == 3 || this.event_info["Units"] == 4) {
        factor = 1000; // Highcharts vill tíma ásinn í ms
      }

      for (var i = 0; i < dataLen; i++) {
        //console.log(this.event_tooltip[i]);
        if (this.event_info.Minimize === true) {
          let c =
            this.event_min_legal[i] === null
              ? null
              : this.event_min_legal[i] * factor; // null margfaldað með tölu gefur 0 sem við viljum ekki
          data_points.push({
            x: this.event_years_legal[i],
            y: c,
            label: this.event_tooltip_legal_min[i],
          });
        } else {
          let c =
            this.event_max_legal[i] === null
              ? null
              : this.event_max_legal[i] * factor;
          data_points.push({
            x: this.event_years_legal[i],
            y: c,
            label: this.event_tooltip_legal_max[i],
          });
        }
      }

      return data_points;
    },
  },
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

/* xs */
.img-profile {
  width: 50px;
  height: auto;
}
/* sm */
@media (min-width: 768px) {
  .img-profile {
    width: 75px;
  }
}
/* md */
@media (min-width: 992px) {
  .img-profile {
    width: 100px;
  }
}
/* lg */
@media (min-width: 1200px) {
  .img-profile {
    width: 125px;
  }
}
</style>