<template>
  <div>
    <hr />
    <h2 class="display-4"><i class="fas fa-trophy"></i> Árangur</h2>
    <p>
      <i class="far fa-hand-pointer"></i>
      <small>Veldu grein í töflunni til að sjá meiri upplýsingar um hana.</small>
    </p>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <!--<caption>Listi yfir árangur</caption>-->
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col">Grein</th>
          <th scope="col">PB úti</th>
          <th scope="col">PB inni</th>
          <th scope="col">SB {{ new Date().getFullYear() }}</th>
          <th scope="col">SB {{ new Date().getFullYear()-1 }}</th>
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
          <th scope="row">
            <router-link :to="{ name: 'CompetitorEvent', params: { competitorID: competitorID, eventID: i.EventID }}">
            {{i.EventShortName}} <small class="text-muted">{{i.EventUnit}}</small>
            </router-link>
            </th>
          <td>{{ i.PB_out}} <small class="text-muted" v-if="i.PB_out !== ''">({{i.PB_out_date}})</small></td>
          <td>{{ i.PB_in}} <small class="text-muted" v-if="i.PB_in !== ''">({{i.PB_in_date}})</small></td>
          <td>{{ i.SB_cur }}</td>
          <td>{{ i.SB_last }}</td>
          <!--<td>{{i.count}}</td>-->
        </tr>
      </tbody>
    </table>
    <a
      href="#"
      v-on:click.prevent="toggle_showEvents($event)"
      v-if="showMoreLessButton"
      class="text-success"
    ><b><span v-html="textMoreLess"></span></b></a>
  </div>
</template>

<script>
export default {
  props: ["event_info", "competitorID"],
  data() {
    return {
      showAllEvents: false,
    };
  },
  computed: {
    textMoreLess: function () {
      if (this.showAllEvents == false) {
        return '<i class="fas fa-caret-down"></i> Sýna fleiri greinar';
      } else {
        return '<i class="fas fa-caret-up"></i> Sýna færri greinar';
      }
    },
    showMoreLessButton() {
      if (this.event_info.length > 5) {
        return true;
      } else {
        return false;
      }
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
    toggle_showEvents: function (event) {
      this.showAllEvents = !this.showAllEvents;
    },
  },
};
</script>

<style scoped>
.table {
  margin-bottom: 0;
  width: 100%;
}
.td {
  text-align: center;
  vertical-align: middle;
}
.display-4 {
  margin-top: 1rem;
}
</style>