<template>
    <v-form ref="form">
      <v-text-field label="Name" v-model="name" :rules="nameRules" required/>
      <v-select :items="locations" label="Ort" item-text="name" item-value="id" :rules="selectRule" v-model="selectedLocationId"></v-select>
      <v-btn color="validate" @click="save">
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
      selectedLocationId: undefined,

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
        this.selectedLocationId = safeTemplate.location.id;
      } else {
        this.safeId = undefined;
        this.name = '';
        this.selectedLocationId = undefined;
      }

      this.$refs.form.resetValidation();
    },

    async save() {
      if (this.$refs.form.validate() && this.selectedLocationId) {
        const apiStub = await api;

        const safeModel = {
            name: this.name,
            location_id: this.selectedLocationId
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