<template>
  <div class="home pb-5">
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

      <div class="buttons">
        <form-popup text="Bearbeiten"
              form="edit-location-form"
              @save-form="loadLocation()"
              ref="popup"
              @mounted="mountedEvent"
              @button-add-clicked="mountedEvent"/>

  <!--      DELETE BUTTON-->
        <v-dialog width="500px" v-model="deleteDialog">
          <template v-slot:activator="{ on: clickEvent }">
            <div class="tooltip" :title="tooltip">
              <v-btn text class="primary-color mx-8 my-4" v-on="clickEvent" :disabled="deleteDisabled">
                Löschen
              </v-btn>
            </div>
          </template>
          <v-card class="pb-1">
            <v-card-title>Ort {{location.name}} wirklich löschen?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="primary-color" @click="deleteItem">Bestätigen</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>

      <h2 class="mb-2">Schlösser</h2>
      <detail-table-locks ref="lockTable" @empty="locksEmpty=true"></detail-table-locks>

      <h2 class="mt-3 mb-2">Tresore</h2>
      <detail-table-safes ref="safeTable" @empty="safesEmpty=true"></detail-table-safes>
    </div>
  </div>
</template>

<script>
import api from "@/api/api";
import DetailTableLocks from "@/components/detail/DetailTableLocks";
import DetailTableSafes from "@/components/detail/DetailTableSafes";
import FormPopup from "@/components/FormPopup";

export default {
  name: "LocationView",
  components: {
    DetailTableLocks,
    DetailTableSafes,
    FormPopup
  },

  data() {
    return {
      location: {},
      locationId: undefined,
      deleteDialog: false,
      locksEmpty: false,
      safesEmpty: false
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
    },
    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.location.id };
      apiStub.location_deleteLocation(param).then(() => {
        this.$router.push('/location');
      });
    }
  },
  computed: {
    deleteDisabled() {
      return !this.safesEmpty || !this.locksEmpty;
    },
    tooltip() {
      if(this.deleteDisabled) return "Ort kann nur gelöscht werden, wenn ihm keine Schlösser oder Ort zugewiesen sind";
      return "";
    }
  }
}
</script>

<style scoped>
 .buttons {
   text-align: end;
 }

 .buttons >>> .v-btn {
   margin-right: 0!important;
   margin-left: 16px!important;
   margin-bottom: 0 !important;
 }

 .buttons .tooltip {
   display: inline-block;
 }

 .buttons .tooltip .v-btn {
   margin-right: 0!important;
   margin-left: 16px!important;
   margin-bottom: 0 !important;
 }
</style>