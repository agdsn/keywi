<template>
  <v-dialog max-width="600px" v-model="dialog">
    <template v-slot:activator="{ on: activationEvent }">
      <v-btn text class="primary-color mx-8 my-4" v-on="activationEvent" @click="$emit('button-add-clicked')" v-if="renderBtn">
        {{ text }}
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        <h2>{{ text }}</h2>
      </v-card-title>
      <v-card-text class="pb-10">
        <component
            ref="form"
            v-bind:is="form"
            class="mx-8 my-4"
            @save-form="saveForm"
            @mounted="mountedEvent"/>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>

export default {
  name: "FormPopup",
  props: {
    text: String,
    renderBtn: {
      type: Boolean,
      default: true,
    },
    form: String
  },
  data() {
    return {
      dialog: false
    }
  },
  methods: {
    closeDialog: function() {
      this.dialog = false;
    },

    openDialog() {
      this.dialog = true;
    },

    saveForm: function() {
      this.$emit('save-form');
      this.closeDialog();
    },

    mountedEvent() {
      this.$emit('mounted');
    },

    buttonClicked() {
      console.log('button clicked');
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