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
      address: undefined,
      lat: undefined,
      lon: undefined,

      nameRules: [
          v => !!v || 'Name erforderlich'
      ]
    }
  },
  methods: {
    async save() {
      if (this.$refs.form.validate()) {
        const apiStub = await api();

        let locationModel = {
          name: this.name,
          address: this.address,
          latitude: this.lat,
          longitude: this.log
        }

        apiStub.location_createLocation(null, locationModel).then(() => {
          this.$refs.form.reset();
          // TODO: add hook to reload table
        });
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