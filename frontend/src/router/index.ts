import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import AllKeysView from '../views/AllKeysView.vue'
import AllSafesView from "@/views/AllSafesView.vue";
import AllLocksView from "@/views/AllLocksView.vue";

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/keys',
    alias: '/',
    name: 'keys',
    component: AllKeysView
  },
  {
    path: '/safe',
    name: 'safe',
    component: AllSafesView
  },
      {
    path: '/lock',
    name: 'lock',
    component: AllLocksView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
