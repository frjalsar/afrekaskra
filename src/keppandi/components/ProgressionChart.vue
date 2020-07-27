<template>
  <div>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";

export default {
  props: ["data"],
  computed: {
    chartOptions() {
      return {
        credits: {
          enabled: false,
        },
        exporting: {
          enabled: true,
        },
        title: {
          text: "",
        },
        legend: {
          enabled: false,
        },
        yAxis: {
          title: {
            text: "Árangur",
          },
        },
        xAxis: {
          type: "datetime",
        },
        tooltip: {
          crosshairs: [false],
          shared: false,
          formatter: function () {
            return this.point.label;
          },
        },
        plotOptions: {
          line: {
            dataLabels: {
              enabled: true,
              formatter: function () {
                return Highcharts.numberFormat(this.y, 2);
              },
            },
            enableMouseTracking: true,
          },
        },
        navigation: {
          buttonOptions: {
            align: "left",
          },
        },
        series: [
          {
            name: "Allur árangur",
            connectNulls: false,
            visible: true,
            type: "line",
            step: "left",
            marker: {
              enabled: true,
              fillColor: "#FFFFFF",
              lineWidth: 2,
              lineColor: null, // inherit from series
            },
            /*             tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            }, */
            data: this.data,
          },
        ],
      };
    },
  },
};
</script>