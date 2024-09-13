//import Vue from 'vue'
//import Router from 'vue-router'
import { createRouter, createWebHistory, createWebHashHistory } from 'vue-router'

//import Home from "@/front.vue";

//Vue.use(Router)

//Ef production mode þá notum við history mode, annars hash mode fyrir dev.
/*if (Vue.config.devtools == true) {
  var my_mode = createWebHashHistory();
} else {
  var my_mode = createWebHistory(import.meta.env.BASE_URL);
}*/

//const Home = { template: '<div>Home sweet home</div>' }

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      //alias: '/',
      name: 'Home',
      component: () => import('./front.vue')
      //component: Home
    },
    {
      path: '/top',
      name: 'TopList',
      component: () => import('./top/TopLists.vue')
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
      component: () => import('./keppandi/single.vue'),
      props: true 
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
      component: () => import('./islmet/ISLRecordList.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('./404.vue')
    }
  ]
})

export default router;