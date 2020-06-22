import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  //mode: 'history',
  routes: [
    {
      path: '/',
      //alias: '/',
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
      name: 'CompetitorList',
      component: () => import('./keppandi/list.vue')
    },
    {
      path: '/keppandi/:competitorID',
      name: 'CompetitorProfile',
      component: () => import('./keppandi/single.vue')
    },
    {
      path: '/keppandi/:competitorID/:eventID',
      name: 'CompetitorEvent',
      component: () => import('./keppandi/event.vue')
    },
    {
      path: '/islmet',
      beforeEnter(to, from, next) {
        window.location = "http://mot.fri.is/MotFRI/Islandsmet.aspx"
      }
  },
    // {
    //   path: '/islmet',
    //   component: () => import('./islmet/list.vue')
    // },
    {
      path: '*',
      component: () => import('./404.vue')
    }
  ]
})
