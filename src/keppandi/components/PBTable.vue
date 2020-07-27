<template>
  <div>
    <h2 class="display-4">Besti árangur</h2>
    <p><i class="far fa-hand-pointer"></i> <small>Veldu grein í töflunni til að sjá meiri upplýsingar um hana.</small></p>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col">Grein</th>
          <th scope="col">PB úti</th>
          <th scope="col">PB inni</th>
          <!--<th scope="col">Fjöldi</th>-->
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(i, index) in event_info"
          v-show="(index < 5) || showAllEvents"
          :key="i.Event"
          @click.prevent="onClick && onClick(i)"
        >
          <!-- v-bind:style="{display: 'none'}" -->
          <th scope="row">{{i.EventShortName}} [{{i.EventUnit}}]</th>
          <td>{{i.PB_out}}</td>
          <td>{{i.PB_in}}</td>
          <!--<td>{{i.count}}</td>-->
        </tr>
      </tbody>
    </table>
    <a href="#" v-on:click.prevent="toggle_showEvents($event)" v-if="showMoreLessButton">Sýna meira/minna</a>
  </div>
</template>

<script>
export default {
  props: ["data", "competitorID"],
  data() {
    return {
      showAllEvents: false
    }
  },
  computed: {
    showMoreLessButton() {
      if (this.event_info.length > 5) {
        return true
      } else {
        return false
      }
    },
    event_info() {
      return this.data;
    },
  },
  methods: {
    onClick(item) {
      //alert(item.EventID);
      //this.$router.push("/keppandi/" + this.competitorID + "/" + item.EventID)
      this.$router.push({
        name: "CompetitorEvent",
        params: { competitorID: this.competitorID, eventID: item.EventID },
      });
    },
    toggle_showEvents: function (event) {
      this.showAllEvents = !this.showAllEvents;
    },
  },
};
</script>

<style scoped>
.table {
    margin-bottom: 0;
}
.td {
  text-align: center;
  vertical-align: middle;
}
</style>