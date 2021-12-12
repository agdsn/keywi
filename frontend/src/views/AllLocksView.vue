<template>
  <div class="home">
    <app-title view-title="Schlösser"></app-title>
    <app-nav-bar></app-nav-bar>
    <lock-table></lock-table>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Schloss hinzufügen">
      <edit-lock-form class="mx-8 my-4 "></edit-lock-form>
    </form-popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import LockTable from "@/components/LockTable.vue";
import FormPopup from "@/components/FormPopup.vue";
import EditLockForm from "@/components/EditLockForm.vue";

export default Vue.extend({
    name: 'AllLocksView',

    components: {
      AppNavBar,
      AppTitle,
      LockTable,
      FormPopup,
      EditLockForm
    }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
