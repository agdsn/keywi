<template>
  <div class="home">
    <app-title view-title="Schlüssel"></app-title>
    <app-nav-bar></app-nav-bar>
    <key-table ref="keyTable"></key-table>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Schlüssel hinzufügen">
      <edit-key-form class="mx-8 my-4" @submit="$refs.keyTable.loadData();"></edit-key-form>
    </form-popup>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import AppTitle from "@/components/AppTitle.vue";
  import AppNavBar from "@/components/AppNavBar.vue";
  import KeyTable from "@/components/KeyTable.vue";
  import FormPopup from "@/components/FormPopup.vue";
  import EditKeyForm from "@/components/EditKeyForm.vue";

  export default Vue.extend({
    name: 'AllKeysView',

    components: {
      KeyTable,
      AppNavBar,
      AppTitle,
      FormPopup,
      EditKeyForm
    }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
