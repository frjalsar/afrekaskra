<template>
  <div>
    <highcharts class="stock" :constructor-type="'stockChart'" :options="stockOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
export default {
  props: ["data"],
  data() {
      return {
          isVisible: true,
          sometext: 'Árangur'
      }
  },
  computed: {
    stockOptions() {
      return {
        rangeSelector: {
          selected: "all",
          buttons: [
            {
              type: "month",
              count: 3,
              text: "3m"
            },
            {
              type: "month",
              count: 6,
              text: "6m"
            },
            {
              type: "year",
              count: 1,
              text: "1 ár"
            },
            {
              type: "year",
              count: 3,
              text: "3 ár"
            },
            {
              type: "year",
              count: 6,
              text: "6 ár"
            },
            {
              type: "all",
              text: "Allt"
            }
          ]
        },
        credits: {
          enabled: false
        },
        title: {
          text: ""
        },
        xAxis: {
          type: "datetime"
        },
        yAxis: {
          title: {
            text: "Árangur"
          }
        },
        series: [
          {
            name: this.sometext,
            visible: this.isVisible,
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