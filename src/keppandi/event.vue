<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div v-if="isReady">
      {{competitorID}} and {{eventID}} and {{competitor_info.FirstName}} and {{event_info.ShortName}}
      <br />
      <table class="table table-striped table-hover table-responsive-sm table-sm">
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col">Árangur [{{event_info.Units_symbol}}]</th>
            <th scope="col">Vindur</th>
            <th scope="col">Dags.</th>
            <th scope="col">Aldur</th>
            <th scope="col">Heiti móts</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in event_data" v-show="(index < 5) || showAllEvents" :key="i.Event">
            <!-- v-bind:style="{display: 'none'}" -->
            <th scope="row">{{i.Results}}</th>
            <td>{{i.Wind}}</td>
            <td>{{i.Date}}</td>
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
import { Chart } from "highcharts-vue";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "KeppandiEvent",
  components: {
    highcharts: Chart,
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
      isReady: false,
      showAllEvents: true,
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

      var url = "/api/keppandi/" + this.competitorID + "/" + this.eventID;
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.competitor_info = response[0]["data"]["Competitor"];
            this.event_info = response[0]["data"]["EventInfo"];
            this.event_data = response[0]["data"]["EventData"];
            console.log("Got data");

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