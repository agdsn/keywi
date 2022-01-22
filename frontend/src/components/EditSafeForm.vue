<template>
    <v-form ref="form">
      <v-text-field prepend-icon="mdi-safe-square-outline" label="Name" v-model="name" :rules="nameRules" required/>
      <v-autocomplete prepend-icon="mdi-map-marker" :items="locations" label="Ort" item-text="name" item-value="id" :rules="selectRule" v-model="selectedLocation" return-object></v-autocomplete>
      <v-textarea prepend-icon="mdi-note-text-outline" rows="1" label="Notiz" v-model="note"></v-textarea>
      <v-btn color="validate" @click="save">
        <v-icon left size="24">mdi-content-save-outline</v-icon>
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api";

export default {
  name: "EditSafeForm",
  data() {
    return {
      safeId : null,
      name: '',
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
    fillForm(safeTemplate) {
      if(safeTemplate){
        this.safeId = safeTemplate.id;
        this.name = safeTemplate.name;
        this.selectedLocation = safeTemplate.location;
        this.note = safeTemplate.note;
      } else {
        this.safeId = undefined;
        this.name = '';
        this.selectedLocation = undefined;
        this.note = '';
      }

      this.$refs.form.resetValidation();
    },

    async save() {
      if (this.$refs.form.validate() && this.selectedLocation) {
        const apiStub = await api;

        const safeModel = {
            name: this.name,
            location_id: this.selectedLocation.id,
            note: this.note
          }

        if(this.safeId) {
          const param = { uuid: this.safeId };

          apiStub.safe_editSafe(param, safeModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.safe_createSafe(null, safeModel).then(() => {
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