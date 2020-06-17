<template>
  <div>
    <p>Ársbest {{ myID }}</p>
    <br />
    <highcharts class="chart" :options="chartOptions"></highcharts>
  </div>
</template>

<script>
import { Chart } from "highcharts-vue";

export default {
  name: "Arsbest",
  components: {
    highcharts: Chart
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "pie"
        },
        series: [
          {
            name: "Brands",
            colorByPoint: true,
            data: [
              {
                name: "Chrome",
                y: 61.41,
                sliced: true,
                selected: true
              },
              {
                name: "Internet Explorer",
                y: 11.84
              },
              {
                name: "Firefox",
                y: 10.85
              },
              {
                name: "Edge",
                y: 4.67
              },
              {
                name: "Safari",
                y: 4.18
              },
              {
                name: "Sogou Explorer",
                y: 1.64
              },
              {
                name: "Opera",
                y: 1.6
              },
              {
                name: "QQ",
                y: 1.2
              },
              {
                name: "Other",
                y: 2.61
              }
            ]
          }
        ]
      },
      myID: "Nothing"
    };
  },
  created() {
    console.log(this.$route.params);
    console.log(this.$route.query);
  }
};
</script>