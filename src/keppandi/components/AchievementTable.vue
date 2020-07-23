<template>
  <div>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col" @click="sort('Results')">
            <i class="fas fa-sort"></i>
            Árangur [{{event_info.Units_symbol}}]
          </th>
          <th scope="col" @click="sort('Wind')" v-bind:class="{'d-none': !hasWind}">
            <i class="fas fa-sort"></i> Vindur
          </th>
          <th scope="col" @click="sort('Date')">
            <i class="fas fa-sort"></i> Dags.
          </th>
          <th scope="col" @click="sort('Age')">
            <i class="fas fa-sort"></i> Aldur
          </th>
          <th scope="col" @click="sort('competition_name')">
            <i class="fas fa-sort"></i> Heiti móts
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in sortedData" v-show="(index < 5) || showAllEvents" :key="i.Event">
          <!-- v-bind:style="{display: 'none'}" -->
          <th scope="row">{{i.Results_text}}</th>
          <td v-bind:class="{'d-none': !hasWind}">{{i.Wind}}</td>
          <td>{{i.Date | formatDate}}</td>
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
</template>

<script>
export default {
  props: ["event_info", "showAllEvents", "event_data"],
  data() {
    return {
      currentSort: "Results",
      currentSortDir: "desc",
    };
  },
  watch: {
    event_info: function (val) {
      if (this.val.Minimize === true) {
        currentSortDir = "asc";
      } else {
        currentSortDir = "desc";
      }
    },
  },
  computed: {
    sortedData: function () {
      return this.event_data.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === "desc") modifier = -1;
        if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
        if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        return 0;
      });
    },
    hasWind: function () {
      if (this.event_info["HasWind"] === 1) {
        return true;
      } else {
        return false;
      }
    },
  },
  methods: {
    sort: function (s) {
      //if s == current sort, reverse
      if (s === this.currentSort) {
        this.currentSortDir = this.currentSortDir === "asc" ? "desc" : "asc";
      }
      this.currentSort = s;

      //console.log("Sort");
      //console.log(this.currentSort);
      //console.log(this.currentSortDir);
    },
  },
};
</script>