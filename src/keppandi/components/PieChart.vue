<template>
  <div>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
//import Highcharts from "highcharts";

export default {
  props: ["data"],
  computed: {
    chartOptions() {
      return {
        chart: {
          type: "pie",
        },
        credits: {
          enabled: false,
        },
        accessibility: {
          point: {
            valueSuffix: "%",
          },
        },
        tooltip: {
          pointFormat: "{series.name}: <b>{point.percentage:.2f}%</b>",
        },
        title: {
          text: "",
        },
        plotOptions: {
          pie: {
            dataLabels: {
              enabled: true,
              connectorShape: "fixedOffset",
              format: "<b>{point.name}</b>: {point.percentage:.1f} %",
            },
            enableMouseTracking: true,
          },
        },
        series: [
          {
            name: "Hlutafall",
            colorByPoint: true,
            data: this.data
          },
        ],
      };
    },
  },
};
</script>