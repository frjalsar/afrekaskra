<template>
  <div>
    <div v-if="!isReady">
      <pulse-loader :loading="!isReady" :color="color" :size="size"></pulse-loader>
      <p style="text-align:center">{{message}}</p>
    </div>
    <div id="competitor-view" v-if="isReady">
      <div class="card" style="width: 32.5rem;">
        <img class="card-img-top" src="./static/kt_action.jpg" />
        <div class="card-header">
          <div class="row justify-content-start">
            <div class="col-4">
              <img class="card-img-profile" src="./static/kt_profile.jpg" width="150px" />
            </div>
            <div class="col">
              <p>
                {{competitor_info.FirstName}} {{competitor_info.LastName}}
                <br />
                ({{competitor_info.Club}})
              </p>
            </div>
          </div>
        </div>
        <div class="card-body">
          <table class="table table-striped table-hover table-responsive-sm table-sm">
            <col span="1" class="wide" />
            <thead>
              <tr>
                <th scope="col">Grein</th>
                <th scope="col">PB úti</th>
                <th scope="col">PB inni</th>
                <th scope="col">Fjöldi</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(i, index) in event_info"
                v-show="(index < 3) || showAllEvents"
                :key="i.Event"
                @click.prevent="onClick && onClick(i)"
              >
                <!-- v-bind:style="{display: 'none'}" -->
                <th scope="row">{{i.Event}}</th>
                <td>{{i.PB_out}}</td>
                <td>{{i.PB_in}}</td>
                <td>{{i.count}}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="card-footer text-muted text-center">
          <a href="#" v-on:click.prevent="toggle_showEvents($event)">Sýna meira/minna</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: "KeppandiSingle",
  components: {
    PulseLoader
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
      competitorID: "",
      message: "",
      showAllEvents: false
    };
  },
  created() {
    this.competitorID = this.$route.params.competitorID;
    this.get_data();
  },
  methods: {
    onClick(item) {
      alert(item.EventID);
    },
    get_data: function() {
      this.$parent.loading = true;
      this.message = "Næ í gögn ekki stökkva langt 😉";

      this.data = [];

      var url = "/api/keppandi/" + this.competitorID;
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.competitor_info = response[0]["data"]["Competitor"];
            this.event_info = response[0]["data"]["Events"];
          })
        )
        .catch(error => {
          this.message = "Villa frá vefþjóni (" + error + ") 😭";
        })
        .finally(() => {
          //this.$parent.loading = false;
          //document.title = this.titleText
          //this.$parent.do_stuff()
          this.isReady = true;
        });
    },
    toggle_showEvents: function(event) {
      this.showAllEvents = !this.showAllEvents;
    }
  }
};
</script>

<style scoped>
.table {
  table-layout: fixed;
  border-collapse: collapse;
  width: 100%;
}
.td {
  border: 1px solid #000;
}
.wide {
  width: 300px;
}

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