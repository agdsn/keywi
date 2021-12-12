<template>
  <v-dialog max-width="600px">
    <template v-slot:activator="{ on }">
      <v-btn text class="primary-color mx-8 my-4" v-on="on">
        {{ text }}
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <h2>{{ text }}</h2>
      </v-card-title>
      <v-card-text class="pb-10">
        <slot></slot>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "FormPopup",
  props: [ 'text' ]

}
</script>

<style scoped>
  .v-dialog {
    position: relative;
  }

  .v-btn {
    position: absolute;
    right: 0;
  }
</style>