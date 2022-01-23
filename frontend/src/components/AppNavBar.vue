<template>
  <div class="nav-bar">
    <ul class="list left">
      <li>
        <router-link to="/key">
          <v-icon color="white" left>mdi-key-chain</v-icon>
          Schlüssel
        </router-link>
      </li>
      <li>
        <router-link to="/safe">
          <v-icon color="white" left>mdi-safe-square</v-icon>
          Tresore
        </router-link>
      </li>
      <li>
        <router-link to="/lock">
          <v-icon color="white" left>mdi-lock</v-icon>
          Schlösser
        </router-link>
      </li>
      <li>
        <router-link to="/location">
          <v-icon color="white" left>mdi-map-marker</v-icon>
          Orte
        </router-link>
      </li>
      <li>
        <router-link to="/user">
          <v-icon color="white" left>mdi-account-multiple</v-icon>
          Benutzer
        </router-link>
      </li>
      <li>
        <router-link to="/rental">
          <v-icon color="white" left>mdi-key</v-icon>
          Ausleihen
        </router-link>
      </li>
    </ul>
    <ul class="list">
      <li v-if="loggedIn">
        <router-link v-if="user != null" :to="`/user/${user.id}`" class="mr-8" href="#">
          <v-icon color="white" left>mdi-account</v-icon>
          {{ user.login }}
        </router-link>
        <a @click="logout">
          <v-icon color="white" left>mdi-logout</v-icon>
          Logout
        </a>
      </li>
      <li v-else><a @click="$refs.loginDialog.openDialog()">
        <v-icon color="white" left>mdi-login</v-icon>
        Login
      </a></li>
    </ul>
    <form-popup
        ref="loginDialog"
        hide-btn
        form="login-form"
        text="Login"
        @save-form="checkLogin">
    </form-popup>
  </div>
</template>

<script>
import FormPopup from "@/components/FormPopup";
import AuthService from "@/services/AuthService";
import router from "@/router";

export default {
  name: "AppNavBar",
  components: {FormPopup},
  data() {
    return {
      loggedIn: false,
      user: null,
    };
  },
  methods: {
    checkLogin() {
      this.loggedIn = localStorage.getItem('access_token') != null;

      setTimeout(() => {
        this.loggedIn = localStorage.getItem('access_token') != null;
      }, 200);
    },
    logout() {
      AuthService.logout();
      this.checkLogin();
      router.push({
        name: 'start',
      });
    }
  },
  watch: {
    loggedIn() {
      this.user = AuthService.getUser();
    },
    $route(to) {
      if (to.query.login === 'true') {
        this.$refs.loginDialog.openDialog()
      } else {
        this.$refs.loginDialog.closeDialog()
      }
    }
  },
  beforeMount() {
    this.checkLogin();
    window.addEventListener('keywi-auth-change', (event) => {
      this.checkLogin();
    });
  }
}
</script>

<style scoped>
.nav-bar {
  background-color: var(--primary-color);
  padding: 10px 30px;
  display: flex;
  justify-content: space-between;
}

.list {
  display: inline-block;
}

.list li {
  display: inline-block;

}

.list a {
  text-decoration: none;
  color: #ffffff;
}

.left {
  max-width: 80%;
}

.left li {
  margin-right: 50px;
}
</style>