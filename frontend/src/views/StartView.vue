<template>
  <div class="text-center">
    <div>
      <h1>Willkommen bei Keywi, der digitalen Schlüsselverwaltung.</h1>
    </div>
    <div>
      <span class="subtitle-1" v-if="loggedOut">
        Bitte melde dich an, um Keywi zu nutzen.
      </span>
    </div>
  </div>
</template>

<script>
import AuthService from "@/services/AuthService";

export default {
  name: "StartView",
  computed: {
    loggedOut() {
      return !AuthService.isLoggedIn();
    }
  }
}
</script>