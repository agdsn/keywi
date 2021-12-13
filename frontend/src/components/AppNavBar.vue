<template>
  <div class="nav-bar">
    <ul class="list left">
      <li><router-link to="/keys">Schlüssel</router-link></li>
      <li><router-link to="/safe">Tresore</router-link></li>
      <li><router-link to="/lock">Schlösser</router-link></li>
      <li><router-link to="/location">Orte</router-link></li>
    </ul>
    <ul class="list">
      <li v-if="loggedIn"><a @click="logout">Logout</a></li>
      <li v-else ><a @click="$refs.loginDialog.openDialog()">Login</a></li>
    </ul>
    <form-popup ref="loginDialog" text="Login" :render-btn="false">
      <LoginForm @submit="this.checkLogin"></LoginForm>
    </form-popup>
  </div>
</template>

<script>
import FormPopup from "@/components/FormPopup";
import LoginForm from "@/components/LoginForm";
import AuthService from "@/services/AuthService";

export default {
  name: "AppNavBar",
  components: {LoginForm, FormPopup},
  data() {
    return {
      loggedIn: false,
    };
  },
  methods: {
    checkLogin() {
      this.loggedIn = localStorage.getItem('access_token') != null;

      setTimeout(() => {
        this.loggedIn = localStorage.getItem('access_token') != null;
      }, 200);


      console.log(this.loggedIn);
      console.log(localStorage.getItem('access_token'));
    },
    logout() {
      AuthService.logout();
      this.checkLogin();
    }
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