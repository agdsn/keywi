<template>
  <v-card class="home pb-5 pt-1">
    <div class="home pb-5">
      <div class="mx-8">
        <h2 class="my-2">Daten</h2>
        <v-simple-table>
          <template v-slot:default>
            <tbody>
            <tr>
              <td style="width: 20%;">Name</td>
              <td><b>{{ safe.name }}</b></td>
            </tr>
            <tr>
              <td>Ort</td>
              <td>
                <router-link :to="`/location/${ safe.location.id }`">{{ safe.location.name }}</router-link>
              </td>
            </tr>
            <tr>
              <td>Anzahl Schlüssel</td>
              <td>{{ safe.amount_keys }}</td>
            </tr>
            <tr>
              <td>Notiz</td>
              <td>{{ safe.note }}</td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
        <v-divider></v-divider>

        <div class="buttons">
          <form-popup ref="popup"
                      form="edit-safe-form"
                      icon="mdi-pencil"
                      text="Bearbeiten"
                      @mounted="mountedEvent"
                      @save-form="loadSafe()"
                      @button-add-clicked="mountedEvent"/>

          <!--      DELETE BUTTON-->
          <v-dialog v-model="deleteDialog" width="500px">
            <template v-slot:activator="{ on: clickEvent }">
              <div :title="tooltip" class="tooltip">
                <v-btn :disabled="deleteDisabled" color="secondary" class="mx-8 my-4" v-on="clickEvent">
                  <v-icon>mdi-delete</v-icon>
                  Löschen
                </v-btn>
              </div>
            </template>
            <v-card class="pb-1">
              <v-card-title>Tresor {{ safe.name }} wirklich löschen?</v-card-title>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="secondary" @click="deleteItem">
                  <v-icon>mdi-delete</v-icon>
                  Bestätigen
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </div>

        <h2 class="mb-2">Schlüssel</h2>
        <detail-table-keys ref="keyTable" @empty="keysEmpty=true"
                           @rented="$refs.keyTable.loadDataBySafeId(safe.id)"></detail-table-keys>

      </div>
    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableKeys from "@/components/detail/DetailTableKeys";
import FormPopup from "@/components/FormPopup";

export default {
  name: "DetailSafeView",
  components: {
    DetailTableKeys,
    FormPopup
  },

  data() {
    return {
      safe: {location: {}},
      safeId: undefined,
      deleteDialog: false,
      keysEmpty: false
    }
  },
  mounted() {
    this.safeId = this.$route.params.id;
    this.loadSafe();
    this.loadKeys();
  },
  methods: {
    async loadSafe() {
      if (!this.safeId) return;

      const apiStub = await api;
      apiStub.safe_getSafe(this.safeId).then(response => {
        this.safe = response.data;
      });
    },

    async loadKeys() {
      this.$refs.keyTable.loadDataBySafeId(this.safeId);
    },

    mountedEvent() {
      if (this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.safe);
    },

    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.safe.id};
      apiStub.safe_deleteSafe(param).then(() => {
        this.$router.push('/safe');
      });
    }
  },
  computed: {
    deleteDisabled() {
      return !this.keysEmpty;
    },
    tooltip() {
      if (this.deleteDisabled) return "Tresor kann nur gelöscht werden, wenn ihm keine Schlüssel zugewiesen sind";
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