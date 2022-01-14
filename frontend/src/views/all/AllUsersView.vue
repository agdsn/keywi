<template>
  <div class="home">
    <user-table class="mx-7 mt-7"/>
  </div>
</template>

<script>
import Vue from 'vue'
import UserTable from "@/components/UserTable";

export default Vue.extend({
    name: 'AllUsersView',

    components: {
      UserTable
    }
  })


</script>

<style scoped>

</style>
