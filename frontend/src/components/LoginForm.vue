<template>
  <div>
    <v-alert
        v-if="error"
        color="red"
        type="error"
    >
      Nutzername oder Passwort falsch!
    </v-alert>

    <v-row>
      <v-col class="text-center">
        <v-btn block color="primary" @click="loginWithOAuth">
          <v-icon left>mdi-key</v-icon>
          Mit AG DSN Konto anmelden
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-divider></v-divider>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-form ref="form">
          <v-text-field v-model="username" :rules="nameRules" label="Nutzername" prepend-icon="mdi-account" required/>
          <v-text-field v-model="password" :rules="passwordRules" label="Passwort" prepend-icon="mdi-key" required
                        @keydown.enter="login" type="password"/>
          <v-row>
            <v-spacer/>
          <v-btn class="mt-3" color="secondary" @click="login">
            Login
          </v-btn>
            </v-row>
        </v-form>
      </v-col>
    </v-row>
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
      error: false,
      nameRules: [
        v => !!v || 'Bitte Nutzernamen eingeben'
      ],
      passwordRules: [
       v => !!v || 'Bitte Password eingeben'
      ],
    }
  },
  methods: {
    async login() {
      if(!this.$refs.form.validate()) return;

      try {
        await AuthService.login(this.username, this.password);
        this.$refs.form.reset();
        this.$emit('save-form');
        this.$emit('submit');
      } catch(err) {
        this.error = true;
      }
    },
    async loginWithOAuth() {
      window.location.href = AuthService.getOAuthUrl(this.$route.query.return_url);
    }
  },
}
</script>

<style scoped>
  .v-form {
    position: relative;
  }
</style>