<template>
  <div>
<div id="competitor-view" v-if="isReady">
            <div class="card" style="width: 35.5rem;">
  <img class="card-img-top" src="./static/kt_action.jpg" alt="Card image cap">
  <div class="card-header">
    {{competitor_info.FirstName}} {{competitor_info.LastName}}
  </div>
  <div class="card-body">
            <table class="table table-striped table-hover table-responsive-sm table-sm">
          <thead>
            <tr>
              <th scope="col">Grein</th>
              <th scope="col">PB úti</th>
              <th scope="col">PB inni</th>
              <th scope="col">Fjöldi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(i, index) in event_info">
              <th scope="row">{{i.Event}}</th>
              <td>{{i.PB_out}}</td>
              <td>{{i.PB_in}}</td>
              <td>{{i.count}}</td>
            </tr>
          </tbody>
        </table>
    </div>
    <div class="card-footer text-muted text-center">
    Sýna meira.
  </div>
</div>
        </div>
  </div>
</template>

<script>
import axios from "axios";
import PulseLoader from "vue-spinner/src/PulseLoader.vue";

export default {
  name: 'KeppandiSingle',
    components: {
    PulseLoader
  },
        data() {
            return {
                competitor_info: [],
                event_info: [],
                isReady: false,
                competitorID: '',
                message: ''
            }
        },
  created() {
      this.competitorID = this.$route.params.competitorID
      this.get_data()
  },
          methods: {
            get_data: function () {
                this.$parent.loading = true
                this.message = 'Næ í gögn ekki stökkva langt 😉'

                this.data = []

                var url = '/api/keppandi/' + this.competitorID
                axios
                    .all([axios.get(url)]).then(axios.spread((...response) => {
                        this.competitor_info = response[0]['data']['Competitor']
                        this.event_info = response[0]['data']['Events']

                    }))
                    .catch((error) => {
                        this.message = 'Villa frá vefþjóni (' + error + ') 😭'
                    })
                    .finally(() => {
                        this.$parent.loading = false
                        //document.title = this.titleText
                        //this.$parent.do_stuff()
                        this.isReady = true
                    })
            },
        }
}
</script>