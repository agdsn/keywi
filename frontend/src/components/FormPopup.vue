<template>
  <v-dialog max-width="600px" v-model="dialog">
    <template v-slot:activator="{ on }">
      <v-btn text class="primary-color mx-8 my-4" v-on="on">
        {{ text }}
      </v-btn>
    </template>
    <v-card v-on:save-form="closeDialog">
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
  props: [ 'text' ],
  data() {
    return {
      dialog: false
    }
  },
  methods: {
    closeDialog: function() {
      this.dialog = false;
    }
  }

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