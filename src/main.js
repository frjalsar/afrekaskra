import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import '@fortawesome/fontawesome-free/css/all.css'
import moment from 'moment'
import Highcharts from "highcharts";
import HighchartsVue from "highcharts-vue";
import StockModule from "highcharts/modules/stock";
import Exporting from 'highcharts/modules/exporting';
import OfflineExporting from "highcharts/modules/offline-exporting";
//import VueGtag from "vue-gtag";
//import VueMeta from "vue-meta";

//Vue.config.productionTip = true

StockModule(Highcharts);
Exporting(Highcharts);
OfflineExporting(Highcharts);
//Vue.use(HighchartsVue);

//Vue.use(VueMeta)

moment.locale('is');
/*Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('ll')
  }
})*/

//Vue.use(VueGtag, {
//  config: { id: "G-ZHPYDECZRM" }
//}, router);

const app = createApp(App)
//Vue.configureCompat({ COMPONENT_ASYNC: false, // Datepicker compatibility
//                      RENDER_FUNCTION: false // Remove some warnings
//                    }) 
//app.config.globalProperties.global_api_url_prefix = 'https://sif.fri.is' // For production
//app.config.globalProperties.global_api_url_prefix = 'http://127.0.0.1:8000' // For development
app.config.globalProperties.global_api_url_prefix = '' // For production
app.use(HighchartsVue).use(router).mount('#app')