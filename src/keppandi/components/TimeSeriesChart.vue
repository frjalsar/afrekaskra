<template>
  <div>
    <highcharts class="stock" :constructor-type="'stockChart'" :options="stockOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
export default {
  props: ["data"],
  //   data() {
  //     return {
  //       isVisible: true,
  //     };
  //   },
  computed: {
    sortDataByDate: function () {
      //Highcharts wants the date sorted in ascending order
      return this.data.sort((a, b) => {
        let modifier = 1;
        if (a["x"] < b["x"]) return -1 * modifier;
        if (a["x"] > b["x"]) return 1 * modifier;
        return 0;
      });
    },
    stockOptions() {
      return {
        exporting: {
          enabled: true,
        },
        navigation: {
          buttonOptions: {
            align: "right",
          },
        },
        legend: {
          enabled: false,
        },
        rangeSelector: {
          selected: "all",
          buttons: [
            {
              type: "month",
              count: 3,
              text: "3m",
            },
            {
              type: "month",
              count: 6,
              text: "6m",
            },
            {
              type: "year",
              count: 1,
              text: "1 ár",
            },
            {
              type: "year",
              count: 3,
              text: "3 ár",
            },
            {
              type: "year",
              count: 6,
              text: "6 ár",
            },
            {
              type: "all",
              text: "Allt",
            },
          ],
        },
        credits: {
          enabled: false,
        },
        title: {
          text: "",
        },
        xAxis: {
          type: "datetime",
        },
        yAxis: {
          title: {
            text: "Árangur",
          },
        },
        series: [
          {
            name: "Árangur",
            visible: true,
            tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2,
            },
            data: this.sortDataByDate, //this.data
          },
        ],
      };
    },
  },
};
</script>