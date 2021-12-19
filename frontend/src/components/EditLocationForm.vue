<template>
    <v-form ref="form">
      <v-text-field label="Name" v-model="name" :rules="nameRules" required/>
      <v-text-field label="Adresse" v-model="address"/>
      <v-text-field label="Breitengrad (latitude)" v-model="lat"/>
      <v-text-field label="Längengrad (longitude)" v-model="lon"/>
      <v-btn color="validate" @click="save">
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api";

export default {
  name: "AddLocationForm",
  data() {
    return {
      name: '',
      address: '',
      lat: undefined,
      lon: undefined,
      locationId: undefined,

      nameRules: [
          v => !!v || 'Name erforderlich'
      ]
    }
  },
  mounted() {
    this.$emit('mounted');
  },
  methods: {
    fillForm(locationTemplate) {
      if(locationTemplate){
        this.name = locationTemplate.name;
        this.address = locationTemplate.addresses;
        this.lat = locationTemplate.lat;
        this.lon = locationTemplate.lon;
      } else {
        this.name = '';
        this.address = '';
        this.lat = undefined;
        this.lon = undefined;
      }

      this.$refs.form.resetValidation();
    },
    
    async save() {
      if (this.$refs.form.validate()) {
        const apiStub = await api;

        let locationModel = {
          name: this.name,
          address: this.address,
          latitude: this.lat,
          longitude: this.log
        }
        
        if(this.locationId) {
          const param = { uuid: this.locationId };

          apiStub.location_editLocation(param, locationModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.location_createLocation(null, locationModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        }
      }
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
