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
  props: ["safeTemplate"],
  data() {
    return {
      name: '',
      locations: [],
      selectedLocationId: undefined,

      nameRules: [
          v => !!v || 'Name erforderlich'
      ],

      selectRule: [
          v => !!v || "Bitte Ort auswählen"
      ],

      safeId : null
    }
  },
  mounted() {
    this.updateSafeTemplate(this.safeTemplate);
    this.loadLocations();
  },
  methods: {
    updateSafeTemplate(safeTemplate) {
      if(safeTemplate){
        this.safeId = safeTemplate.safe_id;
        this.name = safeTemplate.safe_name;
        this.selectedLocationId = safeTemplate.location_id;
      }
    },

    async save() {
      if (this.$refs.form.validate() && this.selectedLocationId) {
        const apiStub = await api();

        if(this.safeId) {
          const param = { uuid: this.safeId };
          const safeModel = {
            name: this.name,
            location_id: this.selectedLocationId
          }

          apiStub.safe_editSafe(param, safeModel).then(() => {
            this.$refs.form.reset();
            this.$parent.$emit('save-form');
          });
        } else {
          let safeModel = {
            name: this.name,
            location_id: this.selectedLocationId
           }

          apiStub.safe_createSafe(null, safeModel).then(() => {
            this.$refs.form.reset();
            this.$parent.$emit('save-form');
          });
        }
      }
    },
    async loadLocations() {
      const apiStub = await api();
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