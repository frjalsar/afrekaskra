<template>
  <div>
    <div v-if="loading">
      <pulse-loader :loading="loading" :color="color" :size="size"></pulse-loader>
    </div>
    <div v-if="!loading">
      <p>Hér sjást bestu afrek ársins. Smelltu á grein í listanum til að sjá topp 100 listann fyrir árið eða frá upphafi. Smelltu á nafn til að sjá upplýsingar um keppandann.</p>
      <!---->
      <h3><i class="fas fa-female"></i> Konur</h3>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <!--<caption>Listi yfir afmæli Íslandsmeta</caption>-->
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col">Grein</th>
          <th scope="col">Nafn</th>
          <th scope="col">Árangur</th>
          <th scope="col">Úti/Inni</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in women_data">
          <th scope="row">
            <router-link v-bind:to="{name: 'TopList', query: {g:'2', e:i.EventID, t:i.EventType} }">{{ i.EventName }}</router-link>
          </th>
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
          <td>{{ i.Results }} <small class="text-muted">{{i.Units_symbol }}</small></td>
          <td>{{ inout_text(i.OutInn) }}</td>
        </tr>
      </tbody>
    </table>
    <!---->
    <br>
      <h3><i class="fas fa-male"></i> Karlar</h3>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <!--<caption>Listi yfir afmæli Íslandsmeta</caption>-->
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col">Grein</th>
          <th scope="col">Nafn</th>
          <th scope="col">Árangur</th>
          <th scope="col">Úti/Inni</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in men_data">
          <th scope="row">
            <router-link v-bind:to="{name: 'TopList', query: {g:'1', e:i.EventID, t:i.EventType} }">{{ i.EventName }}</router-link>
          </th>
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
          <td>{{ i.Results }} <small class="text-muted">{{i.Units_symbol }}</small></td>
          <td>{{ inout_text(i.OutInn) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
import axios from "axios";
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

      loading: true,
      message: "",

      women_data: [],
      men_data: [],
    };
  },
  created() {
    this.get_data();
  },
  computed: {
    //
  },
  methods: {
    inout_text: function (inout) {
      if (inout === 0) {
        return "Úti";
      } else {
        return "Inni";
      }
    },
    get_data: function () {
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.data = [];
      //console.log('Getting data')

      var url = "/api/top_front/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.women_data = response[0]["data"]["Women"];
            this.men_data = response[0]["data"]["Men"];
            //console.log("Got data");
            //console.log(response[0]);
            //console.log("Women data");
            //console.log(this.women_data);
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
</style>
