<template>
  <div v-if="showRecordsTable">
    <h2 class="display-4">Íslandsmet</h2>
    <table class="table table-striped table-hover table-responsive-sm table-sm">
      <col span="1" class="wide" />
      <thead>
        <tr>
          <th scope="col" @click="sort('Event')">
            <i class="fas fa-sort"></i> Grein
          </th>
          <th scope="col" @click="sort('Results')">
            <i class="fas fa-sort"></i>
            Árangur
          </th>
          <th scope="col" @click="sort('Wind')">
            <i class="fas fa-sort"></i> Vindur
          </th>
          <th scope="col" @click="sort('Date')">
            <i class="fas fa-sort"></i> Dags.
          </th>
          <th scope="col" @click="sort('Age')">
            <i class="fas fa-sort"></i> Aldur
          </th>
          <th scope="col" @click="sort('AgeGroup')">
            <i class="fas fa-sort"></i> Aldursflokkur
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(i, index) in sortedData" v-show="(index < 5) || showAllRecords">
          <th scope="row">{{i.Event}}</th>
          <td>{{i.Results}}</td>
          <td>{{i.Wind}}</td>
          <td>{{i.Date}}</td>
          <td>{{i.Age}}</td>
          <td>{{i.AgeGroup}}</td>
        </tr>
      </tbody>
    </table>
    <a
      href="#"
      v-on:click.prevent="toggle_showEvents($event)"
      v-if="showMoreLessButton"
    >Sýna meira/minna</a>
    <br>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["competitorID"],
  data() {
    return {
      currentSort: "Age",
      currentSortDir: "desc",
      showAllRecords: false,
      record_data: [],
      showMoreLessButton: false,
      showRecordsTable: false
    };
  },
  created() {
    this.Get_Records_Data();
  },
  computed: {
    sortedData: function () {
      //console.log("Sorting data");
      return this.record_data.sort((a, b) => {
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
  },
  methods: {
    toggle_showEvents: function (event) {
      this.showAllRecords = !this.showAllRecords;
    },
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
    Get_Records_Data: function () {
      this.record_data = [];

      var url = "/api/records/" + this.competitorID + "/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            this.record_data = response[0]["data"];
            //console.log("Got records data");
            //console.log(this.record_data);
          })
        )
        .catch((error) => {
          console.log("Error getting records data.");
          this.showRecordsTable = false
        })
        .finally(() => {
          //console.log("Finally");
          if (this.record_data.length > 0) {
              this.showRecordsTable = true
          }
          if (this.record_data.length > 5) {
            this.showMoreLessButton = true;
          }
        });
    },
  },
};
</script>