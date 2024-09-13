import { createApp } from "vue";
import App from "./App.vue";
import router from "./router.js";
import "@fortawesome/fontawesome-free/css/all.css";
import moment from "moment";
import Highcharts from "highcharts";
import HighchartsVue from "highcharts-vue";
import StockModule from "highcharts/modules/stock";
import Exporting from "highcharts/modules/exporting";
import OfflineExporting from "highcharts/modules/offline-exporting";
import VueGtag from "vue-gtag";

//Vue.config.productionTip = true

StockModule(Highcharts);
Exporting(Highcharts);
OfflineExporting(Highcharts);
//Vue.use(HighchartsVue);

//Vue.use(VueMeta)

moment.locale("is");
/*Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('ll')
  }
})*/

const app = createApp(App);
//Vue.configureCompat({ COMPONENT_ASYNC: false, // Datepicker compatibility
//                      RENDER_FUNCTION: false // Remove some warnings
//                    })

// Check if running in development environment
if (process.env.NODE_ENV === "development") {
  app.config.globalProperties.global_api_url_prefix = "http://127.0.0.1:8000"; // For development
} else {
  app.config.globalProperties.global_api_url_prefix = ""; // For production
  //app.config.globalProperties.global_api_url_prefix = 'https://sif.fri.is' // For production
  // Set g-tag id
  app.use(VueGtag, {
    config: { id: "G-ZHPYDECZRM" },
  });
}

app.config.devtools = true;

app.use(HighchartsVue).use(router).mount("#app");
