<template>
    <v-form ref="form">
      <v-text-field label="Name" v-model="name" :rules="nameRules" required/>
      <v-text-field label="Besitzer" v-model="owner"/>
      <v-select :items="locations" label="Ort" item-text="name" item-value="id" :rules="selectRule" v-model="selectedLocationId"></v-select>
      <v-btn color="validate" @click="save">
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api";

export default {
  name: "EditLockForm",
  data() {
    return {
      name: '',
      owner: undefined,
      locations: [],
      selectedLocationId: undefined,

      nameRules: [
          v => !!v || 'Name erforderlich'
      ],

      selectRule: [
          v => !!v || "Bitte Ort auswählen"
      ]
    }
  },
  mounted() { this.loadLocations(); },
  methods: {
    async save() {
      if (this.$refs.form.validate() && this.selectedLocationId) {
        const apiStub = await api;

        let lockModel = {
          name: this.name,
          owner: this.owner,
          location_id: this.selectedLocationId
        }

        apiStub.lock_createLock(null, lockModel).then(() => {
          this.$refs.form.reset();
          this.$emit('submit');
          this.$parent.$emit('save-form');
        });
      }
    },
    async loadLocations() {
      const apiStub = await api;
      apiStub.location_getLocations().then(response => {
        this.locations = response.data;
      })
    }
  }
}
</script>

<style scoped>
  .v-btn {
    background-color: var(--primary-color) !important;
    color: white;
    position: absolute;
    right: 0;
  }

  .v-form {
    position: relative;
  }
</style>