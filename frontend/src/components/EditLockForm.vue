<template>
    <v-form ref="form">
      <v-text-field prepend-icon="mdi-lock" label="Name" v-model="name" :rules="nameRules" required/>
      <v-text-field prepend-icon="mdi-account" label="Besitzer" v-model="owner"/>
      <v-autocomplete prepend-icon="mdi-map-marker" :items="locations" label="Ort" item-text="name" item-value="id" :rules="selectRule" v-model="selectedLocation" return-object></v-autocomplete>
      <v-textarea prepend-icon="mdi-note-text-outline" rows="1" label="Notiz" v-model="note"></v-textarea>
      <v-btn color="validate" @click="save">
        <v-icon>mdi-content-save-outline</v-icon>
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
      selectedLocation: undefined,
      note: '',

      nameRules: [
          v => !!v || 'Name erforderlich'
      ],

      selectRule: [
          v => !!v || "Bitte Ort auswählen"
      ]
    }
  },
  mounted() {
    this.loadLocations();
    this.$emit('mounted');
  },
  methods: {
    fillForm(lockTemplate) {
      if(lockTemplate){
        this.lockId = lockTemplate.id;
        this.name = lockTemplate.name;
        this.owner = lockTemplate.owner;
        this.selectedLocation = lockTemplate.location;
        this.note = lockTemplate.note;
      } else {
        this.lockId = undefined;
        this.name = '';
        this.owner = '';
        this.selectedLocation = undefined;
        this.note = '';
      }

      this.$refs.form.resetValidation();
    },

    async save() {
      if (this.$refs.form.validate() && this.selectedLocation) {
        const apiStub = await api;

        const lockModel = {
            name: this.name,
            owner: this.owner,
            location_id: this.selectedLocation.id,
            note: this.note
          }

        if(this.lockId) {
          const param = { uuid: this.lockId };

          apiStub.lock_editLock(param, lockModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.lock_createLock(null, lockModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        }
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