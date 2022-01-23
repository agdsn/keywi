<template>
  <v-card class="home pb-5 pt-1">
    <div class="mx-8">
      <v-alert color="error" v-if="key.deleted">Gelöscht.</v-alert>
      <h2 class="my-2">Schlüssel Daten</h2>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td style="width: 20%;">Schlüsselnummer</td>
            <td><b>{{ key.number }}</b></td>
          </tr>
          <tr>
            <td>Schloss</td>
            <td>
              <router-link :to="`/lock/${ key.lock.id }`">{{ key.lock.name }}</router-link>
            </td>
          </tr>
          <tr>
            <td>Tresor</td>
            <td>
              <router-link :to="`/safe/${ key.safe.id }`">{{ key.safe.name }}</router-link>
            </td>
          </tr>
          <tr>
            <td>Ausleihe</td>
            <td :class="rentalColor">{{ rentalStatus }}</td>
          </tr>
          <tr>
            <td>Notiz</td>
            <td>{{ key.note }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-divider></v-divider>

      <div class="buttons">
        <!--      KEY RETURN BUTTON-->
        <v-dialog v-if="rentedByUser" v-model="returnDialog" width="500px">
          <template v-slot:activator="{ on: clickEvent }">
            <v-btn class="mx-8 my-4" color="secondary" v-on="clickEvent">
              <v-icon left size="24">mdi-key</v-icon>
              Zurückgeben
            </v-btn>
          </template>
          <v-card class="pb-1">
            <v-card-title>Schlüssel {{ key.name }} wirklich zurückgeben?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="secondary" @click="returnItem">
                <v-icon left size="24">mdi-content-save-outline</v-icon>
                Speichern
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <form-popup v-if="rentalEnabled"
                    ref="rentalPopup"
                    form="rent-key-form"
                    icon="mdi-key"
                    text="Ausleihen"
                    @mounted="rentalFormMountedEvent"
                    @save-form="loadKey(); loadRentals()"
        />

        <form-popup ref="popup"
                    form="edit-key-form"
                    icon="mdi-pencil"
                    text="Bearbeiten"
                    @mounted="mountedEvent"
                    @save-form="loadKey()"
                    @button-add-clicked="mountedEvent"
        />

        <!--      DELETE BUTTON-->
        <v-dialog v-model="deleteDialog" width="500px">
          <template v-slot:activator="{ on: clickEvent }">
            <v-btn class="mx-8 my-4" color="secondary" v-on="clickEvent">
              <v-icon left size="24">mdi-delete</v-icon>
              Löschen
            </v-btn>
          </template>
          <v-card class="pb-1">
            <v-card-title>Schlüssel {{ key.name }} wirklich löschen?</v-card-title>
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
      <detail-table-rentals class="mt-10" ref="rentalTable"></detail-table-rentals>
      <detail-table-logs class="mt-10" ref="logTable"></detail-table-logs>
    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableRentals from "@/components/detail/DetailTableRentals";
import FormPopup from "@/components/FormPopup";
import AuthService from "@/services/AuthService";
import DetailTableLogs from "@/components/detail/DetailTableLogs";

export default {
  name: "DetailKeyView",
  components: {
    DetailTableLogs,
    DetailTableRentals,
    FormPopup
  },

  data() {
    return {
      key: {location: {}, safe: {}, lock: {}},
      keyId: undefined,
      deleteDialog: false,
      rentDialog: false,
      returnDialog: false
    }
  },
  mounted() {
    this.keyId = this.$route.params.id;
    this.loadKey();
    this.loadRentals();
    this.$refs.logTable.loadData({ key_id: this.keyId });
  },
  methods: {
    async loadKey() {
      if (!this.keyId) return;

      const apiStub = await api;
      apiStub.key_getKey(this.keyId).then(response => {
            this.key = response.data;
          }
      );
    },

    async loadRentals() {
      this.$refs.rentalTable.loadDataByKeyId(this.keyId);
    },

    rentalFormMountedEvent() {
      if (this.$refs.rentalPopup.$refs.form) this.$refs.rentalPopup.$refs.form.setKeyId(this.key.id);
    },

    mountedEvent() {
      if (this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.key);
    },

    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.key.id};
      apiStub.key_deleteKey(param).then(() => {
        this.$router.push('/key');
      });
    },

    async returnItem() {
      const apiStub = await api;
      const param = {uuid: this.key.active_rental.id};
      apiStub.rental_endRental(param).then(() => {
        this.returnDialog = false;
        this.loadKey();
        this.loadRentals();
      });
    }
  },
  computed: {
    rentalStatus() {
      if (!this.key) return '';
      if(this.rentedByUser) {
        return "Ausgeliehen (von dir)"
      } else if (this.key.active_rental) {
        return "Ausgeliehen";
      } else if (!this.key.rentable) {
        return "Nicht ausleihbar";
      } else {
        return "Ausleihbar";
      }
    },

    rentalColor() {
      if (this.key.active_rental == null && this.key.rentable) {
        return "green-cell"
      } else {
        return "red-cell";
      }
    },

    deleteDisabled() {
      return this.key.active_rental != undefined;
    },

    rentalEnabled() {
      return this.rentalStatus == "Ausleihbar"
    },

    tooltip() {
      if (this.deleteDisabled) return "Schlüssel kann nur gelöscht werden, wenn er momentan nicht verliehen ist";
      return "";
    },

    rentedByUser() {
      if (!this.key.active_rental) return false;
      let user = AuthService.getUser();

      return user.id == this.key.active_rental.user_id;
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

.red-cell {
  background-color: #DDC1BB;
  border-radius: 5px;
}

.green-cell {
  background-color: #ABCC9F;
  border-radius: 5px;
}
</style>