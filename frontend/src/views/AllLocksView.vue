<template>
  <div class="home">
    <app-title view-title="Schlösser"></app-title>
    <app-nav-bar></app-nav-bar>
    <lock-table lock-data=""></lock-table>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import LockTable from "@/components/LockTable.vue";

export default Vue.extend({
    name: 'AllLocksView',

    components: {
      AppNavBar,
      AppTitle,
      LockTable
    }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
