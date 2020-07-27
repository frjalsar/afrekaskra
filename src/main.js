import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@fortawesome/fontawesome-free/css/all.css'
import moment from 'moment'
import Highcharts from "highcharts";
import HighchartsVue from "highcharts-vue";
import StockModule from "highcharts/modules/stock";
import Exporting from 'highcharts/modules/exporting';
import OfflineExporting from "highcharts/modules/offline-exporting";

Vue.config.productionTip = true

StockModule(Highcharts);
Exporting(Highcharts);
OfflineExporting(Highcharts);
Vue.use(HighchartsVue);

moment.locale('is');
Vue.filter('formatDate', function(value) {
  if (value) {
    return moment(String(value)).format('ll')
  }
})

Vue.mixin({
  data: function() {
    return {
      global_API_URL: '',
    }
  }
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
