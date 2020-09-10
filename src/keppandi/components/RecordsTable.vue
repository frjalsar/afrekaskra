<template>
  <div v-if="showRecordsTable">
    <h2 class="display-4"><img src="./ISL_Flag.svg" alt="Icelandic flag" height="56px"> Íslandsmet</h2> <!-- Font size er 3.5 rem í Display-4 sem er 56px-->
    <!-- VIRK MET -->
    <div v-show="showActiveRecordsTable">
      <h5>Virk met</h5>
      <table class="table table-striped table-hover table-responsive-sm table-sm">
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col" @click="sort('Event')">
              <i class="fas fa-sort"></i>&nbsp;Grein
            </th>
            <th scope="col" @click="sort('Results')">
              <i class="fas fa-sort"></i>&nbsp;Árangur
            </th>
            <th scope="col" @click="sort('Wind')">
              <i class="fas fa-sort"></i>&nbsp;Vindur
            </th>
            <th scope="col" @click="sort('inout')">
              <i class="fas fa-sort"></i>&nbsp;Úti/Inni
            </th>
            <th scope="col" @click="sort('Date')">
              <i class="fas fa-sort"></i>&nbsp;Dags.
            </th>
            <th scope="col" @click="sort('Age')">
              <i class="fas fa-sort"></i>&nbsp;Aldur
            </th>
            <th scope="col" @click="sort('AgeGroup')">
              <i class="fas fa-sort"></i>&nbsp;Aldursfl.
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in sortedDataActive" v-show="(index < 5) || showAllActiveRecords">
            <th scope="row">{{i.Event}}</th>
            <td>{{i.Results.toFixed(2)}}</td>
            <td>{{i.Wind}}</td>
            <td>{{i.Inout}}</td>
            <td>{{i.Date}}</td>
            <td>{{i.Age}}</td>
            <td>{{i.AgeGroup}}</td>
          </tr>
        </tbody>
      </table>
      <a
        href="#"
        v-on:click.prevent="toggle_ActiveRecords($event)"
        v-if="showMoreLessButtonActive"
      >{{textMoreLessActive}}</a>
      <p>
        <br />
      </p>
    </div>
    <!-- ÓVIRK MET -->
    <div v-show="showunActiveRecordsTable">
      <h5>Óvirk met</h5>
      <table class="table table-striped table-hover table-responsive-sm table-sm">
        <col span="1" class="wide" />
        <thead>
          <tr>
            <th scope="col" @click="sort('Event')">
              <i class="fas fa-sort"></i>&nbsp;Grein
            </th>
            <th scope="col" @click="sort('Results')">
              <i class="fas fa-sort"></i>&nbsp;Árangur
            </th>
            <th scope="col" @click="sort('Wind')">
              <i class="fas fa-sort"></i>&nbsp;Vindur
            </th>
            <th scope="col" @click="sort('inout')">
              <i class="fas fa-sort"></i>&nbsp;Úti/Inni
            </th>
            <th scope="col" @click="sort('Date')">
              <i class="fas fa-sort"></i>&nbsp;Dags.
            </th>
            <th scope="col" @click="sort('Age')">
              <i class="fas fa-sort"></i>&nbsp;Aldur
            </th>
            <th scope="col" @click="sort('AgeGroup')">
              <i class="fas fa-sort"></i>&nbsp;Aldursfl.
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(i, index) in sortedDataunActive" v-show="(index < 5) || showAllunActiveRecords">
            <th scope="row">{{i.Event}}</th>
            <td>{{i.Results.toFixed(2)}}</td>
            <td>{{i.Wind}}</td>
            <td>{{i.Inout}}</td>
            <td>{{i.Date}}</td>
            <td>{{i.Age}}</td>
            <td>{{i.AgeGroup}}</td>
          </tr>
        </tbody>
      </table>
      <a
        href="#"
        v-on:click.prevent="toggle_unActiveRecords($event)"
        v-if="showMoreLessButtonunActive"
      >{{textMoreLessunActive}}</a>
    </div>
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
      showAllActiveRecords: false,
      showAllunActiveRecords: false,
      record_data: [],
      showMoreLessButtonActive: false,
      showMoreLessButtonunActive: false,
      showRecordsTable: false,
      showActiveRecordsTable: false,
      showunActiveRecordsTable: false,
    };
  },
  created() {
    this.Get_Records_Data();
  },
  computed: {
    textMoreLessActive: function () {
      if (this.showAllActiveRecords == false) {
        return "Sýna meira";
      } else {
        return "Sýna minna";
      }
    },
    textMoreLessunActive: function () {
      if (this.showAllunActiveRecords == false) {
        return "Sýna meira";
      } else {
        return "Sýna minna";
      }
    },
    activeRecords: function () {
      let data = [];
      let dataLen = this.record_data.length;

      for (var i = 0; i < dataLen; i++) {
        if (this.record_data[i].isActive == true) {
          data.push(this.record_data[i]);
        }
      }

      //console.log(data.length);
      if (data.length > 0) {
        this.showActiveRecordsTable = true;
      }

      if (data.length > 5) {
        this.showMoreLessButtonActive = true;
      }

      return data;
    },
    unactiveRecords: function () {
      let data = [];
      let dataLen = this.record_data.length;

      for (var i = 0; i < dataLen; i++) {
        if (this.record_data[i].isActive == false) {
          data.push(this.record_data[i]);
        }
      }

      if (data.length > 0) {
        this.showunActiveRecordsTable = true;
      }

      if (data.length > 5) {
        this.showMoreLessButtonunActive = true;
      }

      return data;
    },
    sortedDataunActive: function () {
      //console.log("Sorting data");
      return this.unactiveRecords.sort((a, b) => {
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
    sortedDataActive: function () {
      //console.log("Sorting data");
      return this.activeRecords.sort((a, b) => {
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
    toggle_ActiveRecords: function (event) {
      this.showAllActiveRecords = !this.showAllActiveRecords;
    },
    toggle_unActiveRecords: function (event) {
      this.showAllunActiveRecords = !this.showAllunActiveRecords;
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
          this.showRecordsTable = false;
        })
        .finally(() => {
          //console.log("Finally");
          if (this.record_data.length > 0) {
            this.showRecordsTable = true;
          }
          if (this.record_data.length > 5) {
            this.showMoreLessButton = true;
          }
        });
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
.display-4 {
  margin-top: 1rem;
}
</style>