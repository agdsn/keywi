<template>
  <v-app>
    <v-main>
      <app-header></app-header>
      <v-container>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import AppHeader from "@/components/AppHeader.vue";
import AuthService from "@/services/AuthService";

export default Vue.extend({
  name: 'App',
  components: {AppHeader},
  data: () => ({
    //
  }),
  mounted() {
    this.$vuetify.theme.currentTheme.secondary = '#41A6A0';

    if (AuthService.isLoggedIn()) {
      AuthService.refreshUser();
    }
  }
});
</script>

<style type="text/css">
  :root {
    --primary-color: #41A6A0;
  }

  a {
    text-decoration: none;
  }
</style>

<style lang="sass">
@import '../node_modules/@fontsource/roboto/latin.css'
</style>
