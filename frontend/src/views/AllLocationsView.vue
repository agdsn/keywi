<template>
  <div class="home pb-5">
    <app-title view-title="Orte"></app-title>
    <app-nav-bar></app-nav-bar>
    <location-table class="mx-8 my-8"></location-table>
    <v-divider class="mx-8"></v-divider>
    <edit-location-form class="mx-8 my-4"></edit-location-form>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import LocationTable from "@/components/LocationTable.vue";
import EditLocationForm from "@/components/EditLocationForm.vue";

export default Vue.extend({
    name: 'AllLocationsView',

    components: {
      EditLocationForm,
      AppNavBar,
      AppTitle,
      LocationTable
    }
  })

</script>

<style scoped>

</style>
