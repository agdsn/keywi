<template>
  <div>
    <app-title :view-title="$route.meta.title"></app-title>
    <app-nav-bar></app-nav-bar>
  </div>
</template>

<script>
import AppTitle from "@/components/AppTitle";
import AppNavBar from "@/components/AppNavBar";
export default {
  name: "AppHeader",
  components: {AppNavBar, AppTitle}
}
</script>

<style scoped>

</style>