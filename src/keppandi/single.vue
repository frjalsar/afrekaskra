<template>
  <div>
    <!-- <div class="search-div">
      <p>Sláðu inn nafn til að leita af öðrum keppanda</p>
      <KeppandiList />
    </div> -->
    <!-- LOADING -->
    <div v-if="!isReady">
      <pulse-loader
        :loading="!isReady"
        :color="color"
        :size="size"
      ></pulse-loader>
      <p style="text-align: center">{{ message }}</p>
      <img src="../fri-loading-1.gif" alt="Hleð síðu" width=100%>
    </div>
    <!-- PROFILE -->
    <div id="competitor-view" v-if="isReady">
      <div class="action-div">
        <img
          class="img-fluid img-action"
          v-bind:src="'/api/img/action/' + competitorID"
        />
        <div class="topleft">
          <h2 style="font-size: 3.5vw">
            <b
              >{{ competitor_info.FirstName }} {{ competitor_info.LastName }}</b
            >
          </h2>
          <h5 style="font-size: 2.5vw">
            {{ competitor_info.Club }} -
            <i
              class="fas"
              v-bind:class="{
                'fa-male': competitor_info.Sex == 1,
                'fa-female': competitor_info.Sex == 2,
              }"
            ></i>
            {{ competitor_info.YOB }}
          </h5>
        </div>
        <div class="bottomleft">
          <img
            class="rounded-circle img-thumbnail img-profile"
            v-bind:src="'/api/img/profile/' + competitorID"
          />
        </div>
        <div class="bottomright">
          <img
            class="img-club"
            v-bind:src="ClubNameUrl"
            @error="ClubLogoError"
            v-if="showClubLogo"
          />
        </div>
      </div>
      <!-- INFO -->
      <div>
        <recordstable :competitorID="competitorID"></recordstable>
        <pbtable
          :event_info="event_info"
          :competitorID="competitorID"
          ref="pbtable"
        ></pbtable>
        <piechart :event_info="event_info" ref="pieChart"></piechart>
        <clubhistory :club_history="club_history"></clubhistory>
      </div>
    </div>
  </div>
  <!--</div>-->
</template>

<script>
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";
import PieChart from "../keppandi/components/PieChart.vue";
import PBTable from "../keppandi/components/PBTable.vue";
import RecordsTable from "../keppandi/components/RecordsTable.vue";
import KeppandiSearch from "./components/Search.vue";
import ClubHistory from "./components/ClubHistory.vue";

export default {
  name: "KeppandiSingle",
  components: {
    piechart: PieChart,
    pbtable: PBTable,
    recordstable: RecordsTable,
    PulseLoader,
    KeppandiSearch,
    clubhistory: ClubHistory,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      competitor_info: [],
      event_info: [],
      club_history: [],
      isReady: false,
      competitorID: null,
      message: "",
      showClubLogo: true,
    };
  },
  created() {
    this.competitorID = this.$route.params.competitorID;
    this.get_data();
  },
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
            this.club_history = response[0]["data"]["Clubs"]
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
          this.isReady = true;
        });
    },
  },
};
</script>

<style scoped>
/* center spinner */
.v-spinner {
  text-align: center;
}

.search-div {
  margin-bottom: 10px;
}

.action-div {
  position: relative;
}

.topleft {
  position: absolute;
  top: 8px;
  left: 16px;
  color: #ffffff;
  text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.75);
}

.bottomleft {
  position: absolute;
  bottom: 8px;
  left: 16px;
}

.bottomright {
  position: absolute;
  bottom: 8px;
  right: 16px;
}

.img-action {
  width: 100%;
  height: auto;
}

/* xs */
.img-club {
  background: transparent;
  width: 50px;
  height: auto;
}
/* sm */
@media (min-width: 768px) {
  .img-club {
    width: 75px;
  }
}
/* md */
@media (min-width: 992px) {
  .img-club {
    width: 100px;
  }
}
/* lg */
@media (min-width: 1200px) {
  .img-club {
    width: 125px;
  }
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