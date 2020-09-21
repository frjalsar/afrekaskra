<template>
  <div>
    <highcharts class="stock" :constructor-type="'stockChart'" :options="stockOptions" ref="chart"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import moment from "moment";
import axios from "axios";

export default {
  props: ["data", "event_info", "competitorID", "eventID"],
  //   data() {
  //     return {
  //       isVisible: true,
  //     };
  //   },
  created() {
    this.GetData();
  },
  methods: {
    GetData: function () {
      //console.log("Getting all competitor event data");
      var url =
        "/api/competitor/" + this.competitorID + "/" + this.eventID + "/all/";
      axios
        .all([axios.get(url)])
        .then(
          axios.spread((...response) => {
            //console.log(response[0]["data"]);
          })
        )
        .catch((error) => {
          //console.log("Error getting all competitor event data");
        })
        .finally(() => {
          //this.$parent.loading = false;
          //document.title = this.titleText
          //this.$parent.do_stuff()
          //this.isReady = true;
        });
    },
  },
  computed: {
    sortDataByDate: function () {
      //Highcharts wants the date sorted in ascending order
      return this.data.sort((a, b) => {
        let modifier = 1;
        if (a["x"] < b["x"]) return -1 * modifier;
        if (a["x"] > b["x"]) return 1 * modifier;
        return 0;
      });
    },
    strFormat() {
      switch (this.event_info["Units"]) {
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
    stockOptions() {
      var ctx = this;
      return {
        exporting: {
          enabled: true,
        },
        navigation: {
          buttonOptions: {
            align: "right",
          },
        },
        legend: {
          enabled: false,
        },
        rangeSelector: {
          selected: "all",
          buttons: [
            {
              type: "month",
              count: 3,
              text: "3m",
            },
            {
              type: "month",
              count: 6,
              text: "6m",
            },
            {
              type: "year",
              count: 1,
              text: "1 ár",
            },
            {
              type: "year",
              count: 3,
              text: "3 ár",
            },
            {
              type: "year",
              count: 6,
              text: "6 ár",
            },
            {
              type: "all",
              text: "Allt",
            },
          ],
        },
        credits: {
          enabled: false,
        },
        title: {
          text: "",
        },
        xAxis: {
          type: "datetime",
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
            switch (ctx.event_info["Units"]) {
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
        scrollbar: {
          enabled: false,
        },
        plotOptions: {
          spline: {
            dataLabels: {
              enabled: true,
              //format: '{point.y:%M:%S.%L}',
              formatter: function () {
                switch (ctx.event_info["Units"]) {
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
          {
            name: "Árangur",
            visible: true,
            //step: "center",
            type: "spline",
            // tooltip: {
            //   //valueSuffix: " m",
            //   valueDecimals: 2,
            // },
            marker: {
              enabled: true,
              fillColor: "#FFFFFF",
              lineWidth: 2,
              lineColor: null, // inherit from series
            },
            data: this.sortDataByDate, //this.data
          },
        ],
      };
    },
  },
};
</script>