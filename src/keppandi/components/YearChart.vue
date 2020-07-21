<template>
  <div>
    <highcharts class="chart" :options="chartOptions"></highcharts>
  </div>
</template>

<script>
export default {
  props: ["data"],
  computed: {
    chartOptions() {
      return {
        credits: {
          enabled: false
        },
        title: {
          text: ""
        },
        series: [
          {
            name: "Árangur",
            connectNulls: false,
            tooltip: {
              //valueSuffix: " m",
              valueDecimals: 2
            },
            data: this.data
          }
        ]
      };
    }
  }
};
</script>