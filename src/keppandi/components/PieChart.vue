<template>
  <div>
    <hr />
    <h2 class="display-4"><i class="fas fa-chart-pie"></i> Skipting</h2>
    <p><small>Heildar fjöldi skráðra afreka í afrekaskrá FRÍ er <b>{{total_count}}</b>. Skipting milli greina er eftirfarandi:</small></p>
    <highcharts class="chart" :options="chartOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
//import Highcharts from "highcharts";

export default {
  props: ["event_info"],
  data() {
    return {
      showPieChart: true,
      total_count: 0,
    };
  },
  computed: {
    pieData: function () {
      //console.log("Process data");
      var dataLen = this.event_info.length;

      let total = 0;
      for (var i = 0; i < dataLen; i++) {
        total = total + this.event_info[i].count;
      }

      this.total_count = total;

      let data_points = [];
      let other = 0;
      let other_count = 0;
      let per = 0;
      for (var i = 0; i < dataLen; i++) {
        per = (this.event_info[i].count / total) * 100;

        if (per < 1.5) {
          other = other + per;
          other_count = other_count + this.event_info[i].count;
        } else {
          data_points.push({
            name: this.event_info[i].EventShortName,
            y: per,
            z: this.event_info[i].count,
          });
        }
      }

      if (other > 0) {
        data_points.push({ name: "Aðrar greinar", y: other, z: other_count });
      }

      //console.log(data_points);
      return data_points;
    },
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
                "<b>{point.name}</b><br />{point.z} ({point.percentage:.1f} %)",
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
            data: this.pieData,
          },
        ],
      };
    },
  },
};
</script>

<style scoped>
.display-4 {
  margin-top: 1rem;
}
</style>