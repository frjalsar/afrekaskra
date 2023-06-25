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
import VueGtag from "vue-gtag";
import VueMeta from "vue-meta";

Vue.config.productionTip = true

StockModule(Highcharts);
Exporting(Highcharts);
OfflineExporting(Highcharts);
Vue.use(HighchartsVue);

Vue.use(VueMeta)

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

Vue.use(VueGtag, {
  //config: { id: "G-ZHPYDECZRM" }
  config: {id: "G-YPHLKPVRX2"}
}, router);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
