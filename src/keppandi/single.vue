<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div id="competitor-view" v-if="isReady">
      <div class="action-div">
        <img
          class="img-fluid"
          style="width:100%;height:auto;"
          v-bind:src="'/api/img/action/' + competitorID"
        />
        <div class="topleft">
          <h2>
            <b>{{competitor_info.FirstName}} {{competitor_info.LastName}}</b>
          </h2>
          <h5>
            {{competitor_info.Club}} -
            <i
              class="fas"
              v-bind:class="{ 'fa-male': competitor_info.Sex == 1, 'fa-female': competitor_info.Sex == 2 }"
            ></i>
            {{competitor_info.YOB}}
          </h5>
        </div>
        <div class="bottomleft">
          <img
            class="rounded-circle border img-thumbnail img-fluid"
            v-bind:src="'/api/img/profile/' + competitorID"
            style="max-width:125px;width:auto;"
          />
          <img
            class="img-fluid img-club"
            v-bind:src="ClubNameUrl"
            @error="ClubLogoError"
            v-if="showClubLogo"
            style="max-width:75px;width:auto;"
          />
        </div>
      </div>
    <!--     <div id="competitor-view" v-if="isReady">
      <img class="card-img-top img-fluid" v-bind:src="'/api/img/action/' + competitorID" />
      <div class="d-flex flex-column bd-highlight mb-3">
        <div class="p-2 bd-highlight profile-div">
          <img
            class="rounded-circle border img-thumbnail img-fluid"
            v-bind:src="'/api/img/profile/' + competitorID"
            style="max-width:125px;width:auto;"
          />
        </div>
        <div class="p-2 bd-highlight profile-text profile-text-name h2">
          <b>{{competitor_info.FirstName}} {{competitor_info.LastName}}</b>
        </div>
        <div class="p-2 bd-highlight profile-text profile-text-other h5">
          {{competitor_info.Club}} -
          <i
            class="fas"
            v-bind:class="{ 'fa-male': competitor_info.Sex == 1, 'fa-female': competitor_info.Sex == 2 }"
          ></i>
          {{competitor_info.YOB}}
        </div>
        <div class="p-2 bd-highlight club-info">
          <img
            class="rounded border img-thumbnail img-fluid img-club"
            v-bind:src="ClubNameUrl"
            @error="ClubLogoError"
            v-if="showClubLogo"
            style="max-width:75px;width:auto;"
          />
        </div>
    </div>-->
    <!-- INFO -->
    <div>
      <recordstable :competitorID="competitorID"></recordstable>
      <pbtable :event_info="event_info" :competitorID="competitorID" ref="pbtable"></pbtable>
      <piechart :event_info="event_info" ref="pieChart"></piechart>
    </div>
    </div>
  </div>
  <!--</div>-->
</template>

<script>
import axios from "axios";
//import { Chart } from "highcharts-vue";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import PieChart from "../keppandi/components/PieChart.vue";
import PBTable from "../keppandi/components/PBTable.vue";
import RecordsTable from "../keppandi/components/RecordsTable.vue";

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
      showClubLogo: true,
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
  computed: {
    ClubNameUrl: function () {
      if (this.isReady === true) {
        return "/api/img/club/" + this.competitor_info.Club;
      } else {
        return "";
      }
    },
  },
  methods: {
    ClubLogoError: function () {
      // Fela Club logo ef við fáum villu á það.
      this.showClubLogo = false;
    },
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

.action-div {
  position: relative;
}

.profile-div {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
  top: -75px;
}

.profile-text {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
  top: -150px;
  left: 25px;
}

.profile-text-name {
  color: #ffffff;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.75);
}

.profile-text-other {
  color: #ffffff;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.75);
}

.topleft {
  position: absolute;
  top: 8px;
  left: 16px;
  font-size: 18px;
  color: #ffffff;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.75);
}

.bottomleft {
  position: absolute;
  bottom: 8px;
  left: 16px;
  font-size: 18px;
}

.club-info {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
  top: -100px;
  left: 160px;
}

.img-club {
  background: transparent;
}
</style>