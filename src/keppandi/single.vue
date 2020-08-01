<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div id="competitor-view" v-if="isReady">
      <div class="card">
        <img class="card-img-top img-fluid" v-bind:src="'/api/img/action/' + competitorID" />
        <div class="card-header">
          <div class="d-flex">
            <div class="p-2">
              <img
                class="rounded-circle img-thumbnail img-fluid"
                v-bind:src="'/api/img/profile/' + competitorID"
                width="150px"
              />
            </div>
            <div class="p-2 flex-grow-1 align-self-center">
              <i class="fas" v-bind:class="{ 'fa-male': competitor_info.Sex == 1, 'fa-female': competitor_info.Sex == 2 }"></i> <b>{{competitor_info.FirstName}} {{competitor_info.LastName}}</b>
              <br />
              {{competitor_info.Club}}
              <br />
              {{competitor_info.YOB}}
            </div>
          </div>
        </div>
        <div class="card-body">
          <recordstable :competitorID="competitorID"></recordstable>
          <pbtable :event_info="event_info" :competitorID="competitorID" ref="pbtable"></pbtable>
          <piechart :event_info="event_info" ref="pieChart"></piechart>
        </div>
        <!--<div class="card-footer text-muted text-center"></div>-->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
//import { Chart } from "highcharts-vue";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import PieChart from "./components/PieChart.vue";
import PBTable from "./components/PBTable.vue";
import RecordsTable from "./components/RecordsTable.vue";

export default {
  name: "KeppandiSingle",
  components: {
    //highcharts: Chart,
    piechart: PieChart,
    pbtable: PBTable,
    recordstable: RecordsTable,
    PulseLoader,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      competitor_info: [],
      event_info: [],
      isReady: false,
      competitorID: null,
      message: "",
    };
  },
  created() {
    //console.log('Created')
    this.competitorID = this.$route.params.competitorID;
    this.get_data();
  },
  //beforeDestroy() {
  //  document.title = "Afrekaskrá FRÍ";
  //},
  methods: {
    get_data: function () {
      //this.$parent.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.data = [];
      //console.log('Getting data')

      var url = "/api/competitor/" + this.competitorID + "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.competitor_info = response[0]["data"]["Competitor"];
            this.event_info = response[0]["data"]["Events"];
            //console.log("Got data");

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
          console.log("Error getting data");
          document.title = "Afrekaskrá FRÍ";
        })
        .finally(() => {
          //this.$parent.loading = false;
          //document.title = this.titleText
          //this.$parent.do_stuff()
          this.isReady = true;
        });
    },
  },
};
</script>

<style scoped>
/* .table {
  table-layout: fixed;
  border-collapse: collapse;
  width: 100%;
}
.td {
  border: 1px solid #000;
}
.wide {
  width: 300px;
} */

/* center spinner */
.v-spinner {
  text-align: center;
}

/* Center card */
.card {
  margin: 0 auto; /* Added */
  float: none; /* Added */
  margin-bottom: 10px; /* Added */
}
</style>