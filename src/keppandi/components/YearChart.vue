<template>
  <div>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import moment from "moment";

export default {
  props: ["alldata", "legaldata", "event_info"],
  // data() {
  //   return {
  //     strFormat: "{value:%M:%S}", // "{value:%M:%S}"
  //   };
  // },
  created() {
    // Bæta við seríu með öllum árangri ef grein hefur vind.
    if (this.event_info["HAS_WIND"] == true) {
      this.chartOptions.series[1] = {
        name: "Allir árangrar",
        connectNulls: false,
        visible: false,
        type: "spline",
        /*tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            }, */
        marker: {
          enabled: true,
          fillColor: "#FFFFFF",
          lineWidth: 2,
          lineColor: null, // inherit from series
        },
        data: this.alldata,
      };
    }
  },
  // mounted() {
  //   console.log(this.legaldata);
  // },
  computed: {
    strFormat() {
      switch (this.event_info["UNIT"]) {
        case 3:
          return "{value:%M:%S}"; //%H:%M:%S.%L
          //return "{value}"
          break;
        case 4:
          return "{value:%H:%M:%S}"; //%H:%M:%S.%L
          break;
        default:
          return "{value}";
      }
    },
    strFormatDataLabel() {
      // %M minutes, %S seconds, %L fractions
      switch (this.event_info["UNIT"]) {
        case 3:
          return "{point.y:%M:%S.%L}";
          break;
        case 4:
          return "{point.y:%H:%M:%S.%L}";
          break;
        default:
          return "{point.y}";
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
        navigation: {
          buttonOptions: {
            align: "left",
          },
        },
        //chart: {
        //  plotBackgroundImage: require('../../bg-1.png'),
        //},
        title: {
          text: "",
        },
        legend: {
          enabled: true,
        },
        yAxis: {
          title: {
            text: "Árangur",
          },
          labels: {
            format: this.strFormat,
          },
        },
        tooltip: {
          crosshairs: [false, false],
          shared: true,
          formatter: function () {
            if (this.points.length < 2) {
              return this.points[0].point.label;
            } else {
              return (
                "<b>" +
                this.points[0].series.name +
                ":</b> " +
                this.points[0].point.label +
                "<br>" +
                "<b>" +
                this.points[1].series.name +
                ":</b> " +
                this.points[1].point.label
              );
            }
          },
        },
        plotOptions: {
          spline: {
            dataLabels: {
              enabled: true,
              //format: this.strFormatDataLabel,
              //format: '{point.y:%M:%S.%L}',
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
        series: [
          // Löglegur árangur er alltaf. Við bætum svo við öllum árangri ef grein hefur vind.
          {
            name: "Löglegur árangur",
            connectNulls: false,
            visible: true,
            type: "spline",
            /*             tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            }, */
            marker: {
              enabled: true,
              fillColor: "#FFFFFF",
              lineWidth: 2,
              lineColor: null, // inherit from series
            },
            data: this.legaldata,
          },
        ],
      };
    },
  },
};
</script>