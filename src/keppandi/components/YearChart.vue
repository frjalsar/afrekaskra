<template>
  <div>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import Highcharts from 'highcharts'

export default {
  props: ["alldata", "legaldata"],
  computed: {
    chartOptions() {
      return {
        credits: {
          enabled: false
        },
        exporting: {
          enabled: true
        },
        title: {
          text: ""
        },
        legend: {
          enabled: true
        },
        yAxis: {
          title: {
            text: "Árangur"
          }
        },
        tooltip: {
          crosshairs: [false, false],
          shared: true,
          formatter: function() {
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
          }
        },
        plotOptions: {
          spline: {
            dataLabels: {
              enabled: true,
              formatter: function() {
                return Highcharts.numberFormat(this.y, 2);
              }
            },
            enableMouseTracking: true
          }
        },
        series: [
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
              lineColor: null // inherit from series
            },
            data: this.legaldata
          },
          {
            name: "Allur árangur",
            connectNulls: false,
            visible: false,
            type: "spline",
            /*             tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            }, */
            marker: {
              enabled: true,
              fillColor: "#FFFFFF",
              lineWidth: 2,
              lineColor: null // inherit from series
            },
            data: this.alldata
          }
        ]
      };
    }
  }
};
</script>