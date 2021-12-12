<template>
  <div class="home">
    <app-title view-title="Tresor"></app-title>
    <app-nav-bar></app-nav-bar>
    <safe-table></safe-table>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Tresor hinzufügen">
      <edit-safe-form class="mx-8 my-4 "></edit-safe-form>
    </form-popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import SafeTable from "@/components/SafeTable.vue";
import FormPopup from "@/components/FormPopup.vue";
import EditSafeForm from "@/components/EditSafeForm.vue";

export default Vue.extend({
    name: 'AllSafesView',

    components: {
      SafeTable,
      AppNavBar,
      AppTitle,
      FormPopup,
      EditSafeForm
    }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
