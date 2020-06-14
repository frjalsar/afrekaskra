import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@fortawesome/fontawesome-free/css/all.css'

Vue.config.productionTip = false

Vue.mixin({
  data: function() {
    return {
      global_API_URL: ''
    }
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
