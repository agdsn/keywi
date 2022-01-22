import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import AllKeysView from '../views/all/AllKeysView.vue'
import AllSafesView from "@/views/all/AllSafesView.vue";
import AllLocksView from "@/views/all/AllLocksView.vue";
import AllLocationsView from "@/views/all/AllLocationsView.vue";
import AllUsersView from "@/views/all/AllUsersView.vue";
import UserView from "@/views/detail/DetailUserView.vue";
import DetailLocationView from"@/views/detail/DetailLocationView.vue";
import DetailSafeView from"@/views/detail/DetailSafeView.vue";
import DetailLockView from"@/views/detail/DetailLockView.vue";
import DetailKeyView from"@/views/detail/DetailKeyView.vue";
import StartView from "@/views/StartView.vue";
import AuthService from "@/services/AuthService";
import DetailRentalView from "@/views/detail/DetailRentalView.vue";
import AllRentalsView from "@/views/all/AllRentalsView.vue";

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'start',
    component: StartView,
    meta: { title: "Start" }
  },
  {
    path: '/key',
    name: 'keyAll',
    component: AllKeysView,
    meta: { title: "Alle Schlüssel" }
  },
  {
    path: '/key/:id',
    name: 'key',
    component: DetailKeyView,
    meta: { title: "Schlüssel Details" },
  },
  {
    path: '/safe/',
    name: 'safeAll',
    component: AllSafesView,
    meta: { title: "Alle Tresore" }
  },
  {
    path: '/safe/:id',
    name: 'safe',
    component: DetailSafeView,
    meta: { title: "Tresor Details" }
  },
  {
    path: '/lock',
    name: 'lockAll',
    component: AllLocksView,
    meta: { title: "Alle Schlösser" }
  },
  {
    path: '/lock/:id',
    name: 'lock',
    component: DetailLockView,
    meta: { title: "Schloss Details" }
  },
  {
    path: '/location',
    name: 'locationAll',
    component: AllLocationsView,
    meta: { title: "Alle Orte" }
  },
  {
    path: '/location/:id',
    name: 'location',
    component: DetailLocationView,
    meta: { title: "Ort Details" }
  },
  {
    path: '/user',
    name: 'users',
    component: AllUsersView,
    meta: { title: "Alle Benutzer" }
  },
  {
    path: '/user/:id',
    name: 'user',
    component: UserView,
    meta: { title: "Benutzer Details" }
  },
  {
    path: '/rental',
    name: 'rentals',
    component: AllRentalsView,
    meta: { title: "Alle Ausleihen" }
  },
  {
    path: '/rental/:id',
    name: 'rental',
    component: DetailRentalView,
    meta: { title: "Ausleihe Details" }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const accessToken = to.query.access_token;
  const user = AuthService.getUser()

  function pushLogin() {
    router.push({
      name: 'start',
      query: { login: 'true', return_url: window.location.origin + to.fullPath },
    });
  }

  if (user != null) {
    next();
  } else if (accessToken != null && typeof accessToken === 'string') {
    AuthService.setAccessToken(accessToken).then(() => {
      console.log('Successful login!');
      router.push({
        path: to.path,
        query: {},
      });
    }).catch((e) => {
      console.log(e);
      pushLogin();
    });
  } else if (to.query.login === 'true' && to.name == 'start') {
    next();
  } else {
    pushLogin()
  }
});

export default router
