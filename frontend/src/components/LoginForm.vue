<template>
  <div>
    <v-alert
        v-if="error != null"
        color="red"
        type="success"
    ></v-alert>

    <v-form ref="form">
      <v-text-field label="Nutzername" v-model="username" required/>
      <v-text-field label="Passwort" v-model="password" required/>
      <v-btn color="validate" @click="login">
        Login
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import AuthService from "@/services/AuthService";

export default {
  name: "LoginForm",
  data() {
    return {
      username: null,
      password: null,
      error: null,
    }
  },
  methods: {
    async login() {
      AuthService.login(this.username, this.password).then(() => {
        this.error = null;
        this.$refs.form.reset();
        this.$parent.$emit('save-form');
        this.$emit('submit');
      }).catch((err) => {
        this.error = "Wrong username or password.";
        this.$emit('submit');
      });
    },
  }
}
</script>

<style scoped>
  .v-btn {
    background-color: var(--primary-color) !important;
    color: white;
    position: absolute;
    right: 0;
  }

  .v-form {
    position: relative;
  }
</style>