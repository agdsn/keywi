<template>
  <v-card class="home pb-5 pt-1">
    <div class="mx-8">
      <v-alert color="error" v-if="rental.deleted">Gelöscht.</v-alert>
      <h2 class="my-2">Ausleihe Daten</h2>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td style="width: 20%;">Schlüssel</td>
            <td><router-link :to="`/key/${rental.key.id}`">{{ rental.key.number }}</router-link></td>
          </tr>
          <tr>
            <td>Vergeben an</td>
            <td><router-link :to="`/user/${rental.user.id}`">{{ rental.user.name }}</router-link></td>
          </tr>
          <tr>
            <td>Ausgegeben von</td>
            <td><router-link :to="`/user/${rental.issuing_user.id}`">{{ rental.issuing_user.name }}</router-link></td>
          </tr>
          <tr>
            <td>Dokument</td>
            <td>{{ rental.allowed_by }}</td>
          </tr>
          <tr>
            <td>Start</td>
            <td>{{ new Date(rental.begin).toLocaleString('de') }}</td>
          </tr>
          <tr>
            <td>Ende</td>
            <td><span v-if="rental.end">{{ new Date(rental.end).toLocaleString('de') }}</span></td>
          </tr>
          <tr>
            <td>Aktiv</td>
            <td class="font-weight-bold" v-if="rental.active != null">
              <span class="green--text" v-if="rental.active">
                Ja
              </span>
              <span class="red--text" v-else>
                Nein
              </span>
            </td>
          </tr>
          <tr>
            <td>Notiz</td>
            <td>{{ rental.note }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>

      <v-divider></v-divider>

      <div class="buttons">
        <!--      DELETE BUTTON-->
        <v-dialog v-model="deleteDialog" width="500px">
          <template v-slot:activator="{ on: clickEvent }">
              <v-btn color="secondary" class="mx-8 my-4" v-on="clickEvent">
                <v-icon left size="24">mdi-delete</v-icon>
                Löschen
              </v-btn>
          </template>
          <v-card class="pb-1">
            <v-card-title>Ausleihe wirklich löschen?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="secondary" @click="deleteItem">
                <v-icon left size="24">mdi-delete</v-icon>
                Bestätigen
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <form-popup
                    ref="rentalEditPopup"
                    form="edit-rental-form"
                    icon="mdi-pencil"
                    text="Bearbeiten"
                    @mounted="rentalEditFormMountedEvent()"
                    @save-form="loadRental(); loadLogs();"
                    @button-add-clicked="rentalEditFormMountedEvent()"
        />

        <v-dialog v-model="returnDialog" width="500px" v-if="rental.active">
          <template v-slot:activator="{ on: clickEvent }">
            <v-btn class="mx-8 my-4" color="secondary" v-on="clickEvent">
              <v-icon left size="24">mdi-arrow-u-left-bottom</v-icon>
              Schlüssel Zurückgeben
            </v-btn>
          </template>
          <v-card class="pb-1">
            <v-card-title>Schlüssel wirklich zurückgeben?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="secondary" @click="returnItem">
                <v-icon left size="24">mdi-check</v-icon>
                Speichern
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>

      <detail-table-logs class="mt-10" ref="logTable"></detail-table-logs>
    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableRentals from "@/components/detail/DetailTableRentals";
import AuthService from "@/services/AuthService";
import FormPopup from "@/components/FormPopup";
import DetailTableLogs from "@/components/detail/DetailTableLogs";

export default {
  name: "DetailRentalView",

  components: {
    DetailTableLogs,
    FormPopup
  },

  data() {
    return {
      rental: {key:{}, user:{}, issuing_user:{}},
      rentalId: undefined,
      returnDialog: false,
      deleteDialog: false,
    }
  },
  mounted() {
    this.rentalId = this.$route.params.id;
    this.loadRental();
    this.loadLogs();
  },
  methods: {
    loadLogs() {
      this.$refs.logTable.loadData({ rental_id: this.rentalId });
    },
    async loadRental() {
      if (!this.rentalId) return;

      const apiStub = await api;
      apiStub.rental_getRental(this.rentalId).then(response => {
        this.rental = response.data;
      });
    },

    rentalEditFormMountedEvent() {
      if (this.$refs.rentalEditPopup.$refs.form)
        this.$refs.rentalEditPopup.$refs.form.fillForm(this.rental);
    },

    async returnItem() {
      const apiStub = await api;
      const param = {uuid: this.rental.id};
      apiStub.rental_endRental(param).then(() => {
        this.returnDialog = false;
        this.loadRental();
      });
    },

    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.rental.id};
      apiStub.rental_deleteRental(param).then(() => {
        this.$router.push('/rental');
      });
    }
  },

  computed: {
    rentedByUser() {
      if (!this.rental.active) return false;
      let user = AuthService.getUser();

      return user.id === this.rental.user.id;
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