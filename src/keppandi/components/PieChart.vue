<template>
  <div>
    <p align="center">
      <i class="fas fa-chart-pie"></i>
      <small>Fjöldi keppna í hverri grein</small>
    </p>
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
              format:
                "<b>{point.name}</b>: {point.z} ({point.percentage:.1f} %)",
            },
            enableMouseTracking: false,
          },
        },
        navigation: {
          buttonOptions: {
            align: "left",
          },
        },
        series: [
          {
            name: "Hlutafall",
            colorByPoint: true,
            data: this.data,
          },
        ],
      };
    },
  },
};
</script>