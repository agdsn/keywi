<template>
  <div class="home pb-5">
    <div class="mx-8">
      <h2 class="my-2">Daten</h2>
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
        <v-dialog v-model="rentDialog" width="500px">
          <template v-slot:activator="{ on: clickEvent }">
              <v-btn class="primary-color mx-8 my-4" text v-on="clickEvent">
                Ausleihen
              </v-btn>
          </template>
          <v-card class="pb-1">
            <v-card-title>Schlüssel {{ key.name }} wirklich ausleihen?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="primary-color" @click="rentItem">Bestätigen</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <form-popup ref="popup"
                    form="edit-key-form"
                    text="Bearbeiten"
                    @mounted="mountedEvent"
                    @save-form="loadKey()"
                    @button-add-clicked="mountedEvent"/>

        <!--      DELETE BUTTON-->
        <v-dialog v-model="deleteDialog" width="500px">
          <template v-slot:activator="{ on: clickEvent }">
            <div :title="tooltip" class="tooltip">
              <v-btn :disabled="deleteDisabled" class="primary-color mx-8 my-4" text v-on="clickEvent">
                Löschen
              </v-btn>
            </div>
          </template>
          <v-card class="pb-1">
            <v-card-title>Schlüssel {{ key.name }} wirklich löschen?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="primary-color" @click="deleteItem">Bestätigen</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>

      <h2 class="mb-2">Ausleihhistorie</h2>
      <detail-table-rentals ref="rentalTable"></detail-table-rentals>

    </div>
  </div>
</template>

<script>
import api from "@/api/api";
import DetailTableRentals from "@/components/detail/DetailTableRentals";
import FormPopup from "@/components/FormPopup";
import AuthService from "@/services/AuthService";

export default {
  name: "DetailKeyView",
  components: {
    DetailTableRentals,
    FormPopup
  },

  data() {
    return {
      key: {location: {}, safe: {}, lock: {}},
      keyId: undefined,
      deleteDialog: false,
      rentDialog: false
    }
  },
  mounted() {
    this.keyId = this.$route.params.id;
    this.loadKey();
    this.loadRentals();
  },
  methods: {
    async loadKey() {
      if (!this.keyId) return;

      const apiStub = await api;
      apiStub.key_getKey(this.keyId).then(response => {
        this.key = response.data;
      });
    },

    async loadRentals() {
      this.$refs.rentalTable.loadData(this.keyId);
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

    async rentItem() {
      const user = AuthService.getUser();

      if (user == null) {
        return;
      }

      const apiStub = await api;
      const rentalModel = {
        key_id: this.key.id,
        begin: new Date().toISOString(),
        // TODO: change
        user_id: user.id
      }

      apiStub.rental_createRental(null, rentalModel).then(() => {
        this.rentDialog = false;
        this.$emit('rented');
      })
    }
  },
  computed: {
    rentalStatus() {
      if (!this.key) return '';
      if (this.key.active_rental) {
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
      return this.key.active_rental;
    },

    tooltip() {
      if (this.deleteDisabled) return "Schlüssel kann nur gelöscht werden, wenn er momentan nicht verliehen ist";
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

.red-cell {
  background-color: #DDC1BB;
  border-radius: 5px;
}

.green-cell {
  background-color: #ABCC9F;
  border-radius: 5px;
}
</style>