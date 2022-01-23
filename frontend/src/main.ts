import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import EditLocationForm from './components/EditLocationForm.vue'
import EditKeyForm from "@/components/EditKeyForm.vue";
import EditLockForm from "@/components/EditLockForm.vue";
import EditSafeForm from "@/components/EditSafeForm.vue";
import LoginForm from "@/components/LoginForm.vue";
import RentKeyForm from "@/components/RentKeyForm.vue";
import EditRentalForm from "@/components/EditRentalForm.vue";

Vue.config.productionTip = false

// Die form Komponenten werden dynamisch geladen und werden daher vorher global registriert
Vue.component('edit-location-form', EditLocationForm);
Vue.component('edit-key-form', EditKeyForm);
Vue.component('edit-lock-form', EditLockForm);
Vue.component('edit-safe-form', EditSafeForm);
Vue.component('edit-rental-form', EditRentalForm);
Vue.component('login-form', LoginForm);
Vue.component('rent-key-form', RentKeyForm);

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')