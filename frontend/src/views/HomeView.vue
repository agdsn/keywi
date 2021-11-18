<template>
  <div class="home">
    <app-title view-title="Meine Schlüssel"></app-title>
    <app-nav-bar></app-nav-bar>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import AppTitle from "@/components/AppTitle.vue";
  import AppNavBar from "@/components/AppNavBar.vue";

  export default Vue.extend({
    name: 'HomeView',

    components: {
      AppNavBar,
      AppTitle,
    },
  })
</script>

