<template>
  <div style="margin-top: -75px;">
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div id="competitor-view" v-if="isReady">
      <div class="d-flex flex-column bd-highlight mb-3">
        <div class="p-2 bd-highlight profile-div">
          <img
            class="rounded-circle border img-thumbnail img-fluid"
            v-bind:src="'/api/img/profile/' + competitorID"
            width="150px"
          />
        </div>
        <div class="p-2 bd-highlight profile-text profile-text-name h2">
          <b>{{competitor_info.FirstName}} {{competitor_info.LastName}}</b>
        </div>
        <div class="p-2 bd-highlight profile-text profile-text-other h5">
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
            width="100px"
            @error="ClubLogoError"
            v-show="showClubLogo"
          />
          <div v-show="!showClubLogo">
            <h2 class="club-text">{{competitor_info.Club}}</h2>
          </div>
        </div>
        <img class="card-img-top img-fluid" v-bind:src="'/api/img/action/' + competitorID" />
      </div>
    </div>
  </div>
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

.action-div img {
  width: 100%;
}

.profile-div {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
}

.profile-text {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
  top: 150px;
}

.profile-text-name {
  color: #ffffff;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.75);
}

.profile-text-other {
  color: #ffffff;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.75);
}

.club-info {
  line-height: 0;
  height: 0;
  z-index: 1;
  position: relative;
  top: -50px;
  left: 160px;
}
</style>