<template>
  <v-card class="home pb-5 pt-1">
    <div class="home pb-5">
      <div class="mx-8">
        <v-alert color="error" v-if="location.deleted">Gelöscht.</v-alert>
        <h2 class="my-2">Ort Daten</h2>
        <v-simple-table>
          <template v-slot:default>
            <tbody>
            <tr>
              <td style="width: 20%;">
                <span>Name</span>
              </td>
              <td><b>{{ location.name }}</b></td>
            </tr>
            <tr>
              <td>
                Adresse
              </td>
              <td>{{ location.address }}</td>
            </tr>
            <tr>
              <td>
                Anzahl Schlösser
              </td>
              <td>{{ location.amount_locks }}</td>
            </tr>
            <tr>
              <td>
                Anzahl Tresore
              </td>
              <td>{{ location.amount_safes }}</td>
            </tr>
            <tr>
              <td>
                Notiz
              </td>
              <td>{{ location.note }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
        <v-divider></v-divider>

        <div class="buttons">
          <form-popup ref="popup"
                      form="edit-location-form"
                      icon="mdi-pencil"
                      text="Bearbeiten"
                      @mounted="mountedEvent"
                      @save-form="loadLocation(); loadLogs();"
                      @button-add-clicked="mountedEvent"/>

          <!--      DELETE BUTTON-->
          <v-dialog v-model="deleteDialog" width="500px">
            <template v-slot:activator="{ on: clickEvent }">
              <div :title="tooltip" class="tooltip">
                <v-btn :disabled="deleteDisabled" color="secondary" class="mx-8 my-4" v-on="clickEvent">
                  <v-icon left size="24">mdi-delete</v-icon>
                  Löschen
                </v-btn>
              </div>
            </template>
            <v-card class="pb-1">
              <v-card-title>Ort {{ location.name }} wirklich löschen?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="secondary" @click="deleteItem">
                  <v-icon left size="24">mdi-delete</v-icon>
                  Bestätigen
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </div>

        <detail-table-locks class="mt-10" ref="lockTable" @empty="locksEmpty=true"></detail-table-locks>

        <detail-table-safes class="mt-10" ref="safeTable" @empty="safesEmpty=true"></detail-table-safes>

        <detail-table-logs class="mt-10" ref="logTable"></detail-table-logs>
      </div>
    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableLocks from "@/components/detail/DetailTableLocks";
import DetailTableSafes from "@/components/detail/DetailTableSafes";
import FormPopup from "@/components/FormPopup";
import DetailTableLogs from "@/components/detail/DetailTableLogs";

export default {
  name: "LocationView",
  components: {
    DetailTableLogs,
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
    this.loadLogs();
  },
  methods: {
    loadLogs() {
      this.$refs.logTable.loadData({ location_id: this.locationId });
    },
    async loadLocation() {
      if (!this.locationId) return;

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
      if (this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.location);
    },
    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.location.id};
      apiStub.location_deleteLocation(param).then(() => {
        this.$router.push('/location');
      });
    }
  },
  computed: {
    deleteDisabled() {
      return !this.safesEmpty;
    },
    tooltip() {
      if (this.deleteDisabled) return "Ort kann nur gelöscht werden, wenn ihm keine Tresore zugewiesen sind";
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
  margin-right: 0 !important;
  margin-left: 16px !important;
  margin-bottom: 0 !important;
}

.buttons .tooltip {
  display: inline-block;
}

.buttons .tooltip .v-btn {
  margin-right: 0 !important;
  margin-left: 16px !important;
  margin-bottom: 0 !important;
}

</style>