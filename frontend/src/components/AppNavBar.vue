<template>
  <div class="nav-bar">
    <ul class="list left">
      <li><router-link to="/key">
        <v-icon color="white" left>mdi-key-chain</v-icon>
        Schlüssel
      </router-link></li>
      <li><router-link to="/safe">
        <v-icon color="white" left>mdi-safe-square</v-icon>
        Tresore
      </router-link></li>
      <li><router-link to="/lock">
        <v-icon color="white" left>mdi-lock</v-icon>
        Schlösser
      </router-link></li>
      <li><router-link to="/location">
        <v-icon color="white" left>mdi-map-marker</v-icon>
        Orte
      </router-link></li>
    </ul>
    <ul class="list">
      <li v-if="loggedIn">
        <router-link :to="`/user/${user.id}`" v-if="user != null" href="#" class="mr-2">{{ user.login }}</router-link>
        <a @click="logout">Logout</a>
      </li>
      <li v-else ><a @click="$refs.loginDialog.openDialog()">Login</a></li>
    </ul>
    <form-popup
        ref="loginDialog"
        text="Login"
        form="login-form"
        @save-form="checkLogin"
        :render-btn="false">
    </form-popup>
  </div>
</template>

<script>
import FormPopup from "@/components/FormPopup";
import AuthService from "@/services/AuthService";

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
    }
  },
  watch: {
    loggedIn() {
      this.user = AuthService.getUser();
    },
  },
  beforeMount() {
    this.checkLogin();
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