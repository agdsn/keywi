<template>
  <v-app>
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
  data: () => ({
    //
  }),
});
</script>

<style type="text/css">
  :root {
    --primary-color: #41A6A0;
  }

  span {
    background-color: #000000;
  }
</style>