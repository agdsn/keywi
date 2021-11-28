<template>
  <div class="home">
    <app-title view-title="Tresor"></app-title>
    <app-nav-bar></app-nav-bar>
    <safe-table safe-data=""></safe-table>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import SafeTable from "@/components/SafeTable.vue";

export default Vue.extend({
    name: 'AllSafesView',

    components: {
      SafeTable,
      AppNavBar,
      AppTitle,
    }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
