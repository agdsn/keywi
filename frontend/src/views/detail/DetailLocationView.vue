<template>
  <div class="home pb-5">
    <app-title view-title="Ort"></app-title>
    <app-nav-bar></app-nav-bar>

    <div class="mx-8">
      <h2 class="my-2">Daten</h2>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td>Name</td>
            <td><b>{{ location.name }}</b></td>
          </tr>
          <tr>
            <td>Adresse</td>
            <td>{{ location.address }}</td>
          </tr>
          <tr>
            <td>Anzahl Schlösser</td>
            <td>{{ location.amount_locks }}</td>
          </tr>
          <tr>
            <td>Anzahl Tresore</td>
            <td>{{ location.amount_safes }}</td>
          </tr>
          <tr>
            <td>Notiz</td>
            <td>{{ location.note }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-divider></v-divider>

      <form-popup text="Bearbeiten"
            form="edit-location-form"
            @save-form="loadLocation()"
            ref="popup"
            @mounted="mountedEvent"
            @button-add-clicked="mountedEvent"/>

      <h2 class="mt-10 mb-2">Schlösser</h2>
      <detail-table-locks ref="lockTable"></detail-table-locks>

      <h2 class="mt-3 mb-2">Tresore</h2>
      <detail-table-safes ref="safeTable"></detail-table-safes>
    </div>
  </div>
</template>

<script>
import AppNavBar from "@/components/AppNavBar";
import AppTitle from "@/components/AppTitle";
import api from "@/api/api";
import DetailTableLocks from "@/components/detail/DetailTableLocks";
import DetailTableSafes from "@/components/detail/DetailTableSafes";
import FormPopup from "@/components/FormPopup";

export default {
  name: "LocationView",
  components: {
    DetailTableLocks,
    DetailTableSafes,
    AppNavBar,
    AppTitle,
    FormPopup
  },

  data() {
    return {
      location: {},
      locationId: undefined
    }
  },
  mounted() {
    this.locationId = this.$route.params.id;
    this.loadLocation();
    this.loadLocks();
    this.loadSafes();
  },
  methods: {
    async loadLocation() {
      if(!this.locationId) return;

      const apiStub = await api;
      apiStub.location_getLocation(this.locationId).then(response => {
          this.location = response.data;
      });
    },
    async loadLocks() {
      this.$refs.lockTable.loadDataByLocationId(this.locationId);
    },
    async loadSafes() {
      this.$refs.safeTable.loadDataByLocationId(this.locationId);
    },
    mountedEvent() {
      if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.location);
    }
  }
}
</script>

<style scoped>

</style>