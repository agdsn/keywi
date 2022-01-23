<template>
  <v-card class="home pb-5 pt-1">
    <div class="home pb-5">
      <div class="mx-8">
        <h2 class="my-2">Schloss Daten</h2>
        <v-simple-table>
          <template v-slot:default>
            <tbody>
            <tr>
              <td style="width: 20%;">Name</td>
              <td><b>{{ lock.name }}</b></td>
            </tr>
            <tr>
              <td>Ort</td>
              <td>
                <router-link :to="`/location/${ lock.location.id }`">{{ lock.location.name }}</router-link>
              </td>
            </tr>
            <tr>
              <td>Besitzer</td>
              <td>{{ lock.owner }}</td>
            </tr>
            <tr>
              <td>Anzahl Schlüssel</td>
              <td>{{ lock.amount_keys }} ({{ lock.amount_free_keys }} verfügbar)</td>
            </tr>
            <tr>
              <td>Notiz</td>
              <td>{{ lock.note }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
        <v-divider></v-divider>

        <div class="buttons">
          <form-popup ref="popup_add"
                      form="edit-key-form"
                      icon="mdi-plus"
                      text="Schlüssel hinzufügen"
                      @mounted="addMountedEvent"
                      @save-form="keyAdded()"
                      @button-add-clicked="addMountedEvent"/>

          <form-popup ref="popup"
                      form="edit-lock-form"
                      icon="mdi-pencil"
                      text="Bearbeiten"
                      @mounted="mountedEvent"
                      @save-form="loadLock()"
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
              <v-card-title>Schloss {{ lock.name }} wirklich löschen?</v-card-title>
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

        <h2 class="mb-2">Schlüssel</h2>
        <detail-table-keys ref="keyTable" @empty="keysEmpty=true"
                           @rented="$refs.keyTable.loadDataByLockId(lock.id)"></detail-table-keys>

      </div>
    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableKeys from "@/components/detail/DetailTableKeys";
import FormPopup from "@/components/FormPopup";

export default {
  name: "DetailLockView",
  components: {
    DetailTableKeys,
    FormPopup
  },

  data() {
    return {
      lock: {location: {}},
      lockId: undefined,
      deleteDialog: false,
      keysEmpty: false
    }
  },
  mounted() {
    this.lockId = this.$route.params.id;
    this.loadLock();
    this.loadKeys();
  },
  methods: {
    async loadLock() {
      if (!this.lockId) return;

      const apiStub = await api;
      apiStub.lock_getLock(this.lockId).then(response => {
        this.lock = response.data;
      });
    },

    async loadKeys() {
      this.$refs.keyTable.loadDataByLockId(this.lockId);
    },

    mountedEvent() {
      if (this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.lock);
    },

    addMountedEvent() {
      let payload = { selectedLock: this.lock };
      if (this.$refs.popup_add.$refs.form) this.$refs.popup_add.$refs.form.fillForm(payload);
    },

    keyAdded() {
      let keyId = this.$refs.popup_add.$refs.form.keyId;
      this.$router.push('/key/'+keyId);
    },

    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.lock.id};
      apiStub.lock_deleteLock(param).then(() => {
        this.$router.push('/lock');
      });
    }
  },
  computed: {
    deleteDisabled() {
      return !this.keysEmpty;
    },
    tooltip() {
      if (this.deleteDisabled) return "Schloss kann nur gelöscht werden, wenn ihm keine Schlüssel zugewiesen sind";
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