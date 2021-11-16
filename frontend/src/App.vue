<template>
  <v-app>
    <AppHeader/>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import AppHeader from "@/components/AppHeader.vue";

export default Vue.extend({
  name: 'App',
  components: {AppHeader},
  data: () => ({
    //
  }),
});
</script>

<style type="text/css">
  span {
    background-color: #000000;
  }
</style>