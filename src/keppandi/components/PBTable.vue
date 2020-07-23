<template>
  <div>
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
          v-show="(index < 5) || showAllEvents"
          :key="i.Event"
          @click.prevent="onClick && onClick(i)"
        >
          <!-- v-bind:style="{display: 'none'}" -->
          <th scope="row">{{i.EventShortName}} [{{i.EventUnit}}]</th>
          <td>{{i.PB_out}}</td>
          <td>{{i.PB_in}}</td>
          <td>{{i.count}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: ["data", "showAllEvents", "competitorID"],
  computed: {
      event_info() {
          return this.data
      }
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
  },
};
</script>