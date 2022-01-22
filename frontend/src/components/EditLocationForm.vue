<template>
    <v-form ref="form">
      <v-text-field prepend-icon="mdi-text" label="Name" v-model="name" :rules="nameRules" required/>
      <v-text-field prepend-icon="mdi-map-marker" label="Adresse" v-model="address"/>
      <v-text-field prepend-icon="mdi-latitude" label="Breitengrad (latitude)" v-model="lat"/>
      <v-text-field prepend-icon="mdi-longitude" label="Längengrad (longitude)" v-model="lon"/>
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
  name: "AddLocationForm",
  data() {
    return {
      name: '',
      address: '',
      lat: undefined,
      lon: undefined,
      locationId: undefined,
      note: '',

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
        this.address = locationTemplate.address;
        this.lat = locationTemplate.latitude;
        this.lon = locationTemplate.longitude;
        this.locationId = locationTemplate.id;
        this.note = locationTemplate.note;
      } else {
        this.name = '';
        this.address = '';
        this.lat = undefined;
        this.lon = undefined;
        this.locationId = undefined;
        this.note = '';
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
          longitude: this.log,
          note: this.note
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
