<template>
  <div>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <!--<caption>Listi yfir árangur</caption>-->
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col" @click="sort('Results')">
            <i class="fas fa-sort"></i>
            &nbsp;Árangur <small class="text-muted">{{event_info.UNIT_SYMBOL}}</small>
          </th>
          <th scope="col" @click="sort('Wind')" v-bind:class="{'d-none': !hasWind}">
            <i class="fas fa-sort"></i>&nbsp;Vindur <small class="text-muted">m/s</small>
          </th>
          <th scope="col" @click="sort('Date')">
            <i class="fas fa-sort"></i>&nbsp;Dags.
          </th>
          <th scope="col" @click="sort('Age')">
            <i class="fas fa-sort"></i>&nbsp;Aldur
          </th>
          <th scope="col" @click="sort('Club')">
            <i class="fas fa-sort"></i>&nbsp;Félag
          </th>
          <th scope="col" @click="sort('competition_name')">
            <i class="fas fa-sort"></i>&nbsp;Heiti&nbsp;móts
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
          <td>{{i.Club}}</td>
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
  created() {
    if (this.event_info['MAX'] === false) {
      this.currentSortDir = "asc";
    } else {
      this.currentSortDir = "desc";
    }
  },
  computed: {
    sortedData: function () {
      return this.event_data.sort((a, b) => {
        let modifier = 1;
        if (this.currentSortDir === "desc") modifier = -1;

        if (
          this.currentSort == "Results" ||
          this.currentSort == "Wind" ||
          this.currentSort == "Age"
        ) {
          if (parseFloat(a[this.currentSort]) < parseFloat(b[this.currentSort]))
            return -1 * modifier;
          if (parseFloat(a[this.currentSort]) > parseFloat(b[this.currentSort]))
            return 1 * modifier;
        } else {
          if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
          if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
        }

        return 0;
      });
    },
    hasWind: function () {
      if (this.event_info["HAS_WIND"] === true) {
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