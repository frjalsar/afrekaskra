<template>
  <div>
    <highcharts class="chart" :options="chartOptions"></highcharts>
  </div>
</template>

<script>
export default {
  props: ["alldata"],
  computed: {
    chartOptions() {
      return {
        credits: {
          enabled: false
        },
        title: {
          text: ""
        },
        yAxis: {
          title: {
            text: "Árangur"
          }
        },
        tooltip: {
          formatter: function() {
            return this.point.label;
          }
        },
        plotOptions: {
          line: {
            dataLabels: {
              enabled: true
            },
            enableMouseTracking: true
          }
        },
        series: [
          {
            name: "Allur árangur",
            connectNulls: false,
            /*             tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            }, */
            data: this.alldata
          }
        ]
      };
    }
  }
};
</script>