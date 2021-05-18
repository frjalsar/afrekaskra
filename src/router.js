import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

//Ef production mode þá notum við history mode, annars hash mode fyrir dev.
if (Vue.config.devtools == true) {
  var my_mode = 'hash'
} else {
  var my_mode = 'history'
}

export default new Router({
  mode: my_mode,
  routes: [
    {
      path: '/',
      //alias: '/',
      component: () => import('./front.vue')
    },
    {
      path: '/top',
      name: 'TopList',
      component: () => import('./top/toplists.vue')
    },
    // {
    //   path: '/arsbest',
    //   component: () => import('./arsbest/arsbest.vue')
    // },
    {
      path: '/keppandi',
      name: 'CompetitorList',
      component: () => import('./keppandi/SearchList.vue')
    },
    {
      path: '/keppandi/:competitorID',
      name: 'CompetitorProfile',
      component: () => import('./keppandi/single.vue')
    },
    {
      path: '/layout/:competitorID',
      name: 'LayoutTest',
      component: () => import('./layout/single.vue')
    },
    {
      path: '/keppandi/:competitorID/:eventID',
      name: 'CompetitorEvent',
      component: () => import('./keppandi/event.vue')
    },
    {
      path: '/islmet',
      name: 'IcelandicRecords',
      component: () => import('./islmet/list.vue')
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