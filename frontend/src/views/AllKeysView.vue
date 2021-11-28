<template>
  <div class="home">
    <app-title view-title="Meine Schlüssel"></app-title>
    <app-nav-bar></app-nav-bar>
    <key-table key-data=""></key-table>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import AppTitle from "@/components/AppTitle.vue";
  import AppNavBar from "@/components/AppNavBar.vue";
  import {OpenAPIClientAxios} from "openapi-client-axios";
  import axios from "axios";
  import KeyTable from "@/components/KeyTable.vue";

  export default Vue.extend({
    name: 'AllKeysView',

    components: {
      KeyTable,
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
