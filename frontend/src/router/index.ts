import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import AllKeysView from '../views/all/AllKeysView.vue'
import AllSafesView from "@/views/all/AllSafesView.vue";
import AllLocksView from "@/views/all/AllLocksView.vue";
import AllLocationsView from "@/views/all/AllLocationsView.vue";
import AllUsersView from "@/views/all/AllUsersView.vue";
import UserView from "@/views/detail/DetailUserView.vue";
import DetailLocationView from"@/views/detail/DetailLocationView.vue";

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/keys/:id?',
      alias: '/',
    name: 'keys',
    component: AllKeysView
  },
  {
    path: '/safe/:id?',
    name: 'safe',
    component: AllSafesView
  },
  {
    path: '/lock/:id?',
    name: 'lock',
    component: AllLocksView
  },
  {
    path: '/location',
    name: 'locationAll',
    component: AllLocationsView
  },
  {
    path: '/location/:id',
    name: 'location',
    component: DetailLocationView
  },
  {
    path: '/user',
    name: 'users',
    component: AllUsersView
  },
  {
    path: '/user/:id',
    name: 'user',
    component: UserView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
