import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  //mode: 'history',
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
    },
    {
      path: '/keppandi',
      component: () => import('./keppandi/list.vue')
    },
    {
      path: '/keppandi/:competitorID',
      component: () => import('./keppandi/single.vue')
    }//,
    // {
    //   path: '*',
    //   component: () => import('./404.vue')
    // }
  ]
})
