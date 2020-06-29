import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@fortawesome/fontawesome-free/css/all.css'
import moment from 'moment'

Vue.config.productionTip = true


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
