<template>
  <div>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import moment from "moment";

export default {
  props: ["data", "event_info"],
  computed: {
    strFormat() {
      switch (this.event_info["Units"]) {
        case 3:
          return "{value:%M:%S}"; //%H:%M:%S.%L
          break;
        case 4:
          return "{value:%H:%M:%S}"; //%H:%M:%S.%L
          break;
        default:
          return "{value}";
      }
    },
    chartOptions() {
      var ctx = this;
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
          labels: {
            format: this.strFormat,
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
                switch (ctx.event_info["Units"]) {
                  case 3:
                    return moment.unix(this.y/1000).format("mm:ss,SS");
                    break;
                  case 4:
                    return moment.unix(this.y/1000).format("hh:mm:ss,SS");
                    break;
                  default:
                    return Highcharts.numberFormat(this.y, 2);
                }
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