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
  data() {
    return {
      window: {
        width: 0,
        height: 0,
      },
      isyvisible: true,
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
      if (this.window.width < 800) {
        this.isyvisible = false;
      } else {
        this.isyvisible = true;
      }
      //console.log(this.isyvisible);
    },
  },
  computed: {
    strFormat() {
      switch (this.event_info["UNIT"]) {
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
          visible: this.isyvisible,
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
                switch (ctx.event_info["UNIT"]) {
                  case 3:
                    return moment.unix(this.y / 1000).format("mm:ss,SS");
                    break;
                  case 4:
                    return moment.unix(this.y / 1000).format("hh:mm:ss,SS");
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