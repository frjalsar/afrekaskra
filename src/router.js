import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      alias: '/',
      component: () => import('./front.vue')
    },
    {
      path: '/top',
      component: () => import('./top/toplists.vue')
    },
    {
      path: '/arsbest',
      component: () => import('./arsbest/arsbest.vue')
    }
  ]
})
