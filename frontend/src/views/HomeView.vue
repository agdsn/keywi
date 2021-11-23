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
  import {OpenAPIClientAxios} from "openapi-client-axios";
  import axios from "axios";

  export default Vue.extend({
    name: 'HomeView',

    components: {
      AppNavBar,
      AppTitle,
    },

    mounted() {
      axios.get('http://localhost:6080/key').then(response => console.log(response.data))
    }
  })


</script>

