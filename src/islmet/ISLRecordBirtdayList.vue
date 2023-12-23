<template>
  <div>
    <div v-if="loading">
      <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
      <!--<video autoplay loop muted playsinline width="100%">
        <source src="../assets/iceland.webm" type="video/webm" />
      </video>-->
      <!--<p style="text-align:center">{{message}}</p>-->
    </div>
    <div v-if="!loading">
    <p>Eftirfarandi <router-link :to="{name: 'IcelandicRecords'}">met</router-link> eiga afmæli á næstunni.</p>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <!--<caption>Listi yfir afmæli Íslandsmeta</caption>-->
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col">Grein</th>
          <th scope="col">Methafi</th>
          <th scope="col">Árangur</th>
          <th scope="col">Aldur mets</th>
          <th scope="col">Vindur</th>
          <th scope="col">Úti/Inni</th>
          <th scope="col">Dags.</th>
          <th scope="col">Aldursfl.</th>
          <th scope="col">Félag</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in RecordData">
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
          <td>{{ i.Results_text }} <small class="text-muted">{{ i.Units_symbol }}</small></td>
          <td>{{ i.Age_record }}</td>
          <td>{{ i.Wind }}</td>
          <td>{{ inout_text(i.Inout) }}</td>
          <td>{{ i.Date }}</td>
          <td>{{ i.AgeGroup }}</td>
          <td><img
                class="img-club"
                v-bind:src="'/api/img/club/' + i.Club"
                v-bind:alt="i.Club"
              />
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

export default {
  components: {
    PulseLoader,
  },
  data() {
    return {
      color: "#0275d8",
      size: "15px",
      margin: "2px",
      radius: "100%",

      raw_record_data: [],
      loading: true,
      message: "",
    };
  },
  created() {
    this.get_data();
  },
  computed: {
    RecordData: function () {
      let data = [];
      let dataLen = this.raw_record_data.length;

      this.nrRecords = dataLen;

      for (var i = 0; i < dataLen; i++) {
        data.push(this.create_result_text(this.raw_record_data[i]));
      }

      return data;
    },
  },
  methods: {
    //0, # No units!
    //'metrar': 1, # Meters
    //'sek.': 2, # ss,dd
    //'mín.': 3, # mm:ss
    //'klst.': 4, # hh:mm:ss,dd
    //'stig': 5, # Points
    //'Ungl.stig': 6 # Points junior
    create_result_text: function (data) {
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
    get_data: function () {
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.raw_record_data = [];
      //console.log('Getting data')

      var url = "/api/records/birthdays/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.raw_record_data = response[0]["data"];
            //console.log("Got data");
          })
        )
        .catch((error) => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
          console.log("Error getting data");
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style scoped>
.v-spinner {
  text-align: center;
}

.img-club {
  height: 25px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
