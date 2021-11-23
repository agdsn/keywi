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
  import api from '@/api/api';
  import axios from "axios";

  export default Vue.extend({
    name: 'HomeView',

    components: {
      AppNavBar,
      AppTitle,
    },
    methods: {
      async getData() {
        const ac = await api;

        ac.key_getKeys().then((rsp) => {
          console.log(rsp);
        });
      }
    },
    mounted() {
      this.getData();

      axios.get('http://localhost:6080/key').then(response => console.log(response.data))
    }
  })


</script>

