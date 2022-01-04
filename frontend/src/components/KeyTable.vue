<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="tableData"
      :items-per-page="25"
      class="elevation-1"
      :loading="loading"
      loading-text="Lade Daten..."
      ref="table"
      :item-class="row_classes"
    >
      <template v-slot:[`item.number`] = "{ item }">
        <router-link :to="`/key/${ item.id }`">{{ item.number }}</router-link>
      </template>

      <template v-slot:[`item.lock.name`] = "{ item }">
        <router-link :to="`/lock/${ item.lock.id }`">{{ item.lock.name }}</router-link>
      </template>

      <template v-slot:[`item.safe.name`] = "{ item }">
        <router-link :to="`/safe/${ item.safe.id }`">{{ item.safe.name }}</router-link>
      </template>

      <template v-slot:[`item.location.name`] = "{ item }">
        <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
      </template>

      <template v-slot:[`item.rental`] = "{ item }">
        {{ getRentalStatus(item) }}
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="openDeletePrompt(item)"
        >
          mdi-delete
        </v-icon>
        <v-tooltip top>
          <template v-slot:activator="{on}">
            <v-icon
              class="ml-2"
              :color="getKeyColor(item)"
              small
              @click="openRentPrompt(item)"
              v-on="on"
            >
              mdi-key
            </v-icon>
          </template>

          <span>Schlüssel ausleihen</span>
        </v-tooltip>
      </template>
    </v-data-table>

    <v-dialog v-model="deleteDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{keyInDialogNumber}} wirklich löschen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="primary-color" @click="deleteItem">Bestätigen</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <v-dialog v-model="rentDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{keyInDialogNumber}} wirklich ausleihen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="primary-color" @click="rentItem">Bestätigen</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "@/api/api";

export default {
  name: "KeyTable",
  data: () => ({
    keyInDialog: undefined,
    deleteDialog: false,
    rentDialog: false,
    loading: true,
    headers: [
      {
        text: "Ort",
        value: "location.name"
      },
      {
        text: "Schloss",
        value: "lock.name"
      },
      {
        text: "Schlüsselnummer",
        value: "number"
      },
      {
        text: "Tresor",
        value: "safe.name"
      },
      {
        text: "Ausleihe",
        value: "rental"
      },
      {
        text: "Aktionen",
        value: "actions",
        sortable: false
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific key if uuid is given in path parameter. load all keys if not
      if(paramId) {
        apiStub.key_getKey(paramId).then(response => {
          this.tableData = [response.data];

          this.loading = false;
        }).finally(() => {
          this.loading = false
        });
      } else {
        apiStub.key_getKeys().then(response => {
          this.tableData = response.data;
        }).finally(() => {
          this.loading = false;
        })
      }
    },

    editItem(key) {
      this.$emit('editItem', key);
    },

    openDeletePrompt(keyInDialog) {
      this.keyInDialog = keyInDialog;
      this.deleteDialog = true;
    },

    openRentPrompt(keyInDialog) {
      this.keyInDialog = keyInDialog;
      this.rentDialog = true;
    },

    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.keyInDialog.id };
      apiStub.key_deleteKey(param).then(() => {
        this.deleteDialog = false;
        this.loadData();
      });
    },

    async rentItem() {
      const apiStub = await api;
      const rentalModel = {
        key_id: this.keyInDialog.id,
        begin: new Date().toISOString(),
        // TODO: change
        user_id: '96c5f55a-b098-4100-8999-8a4591199e78'
      }

      apiStub.rental_createRental(null, rentalModel).then(() => {
        this.rentDialog = false;
        this.loadData();
      })
    },

    getRentalStatus(key) {
      if(key.active_rental) {
        return "Ausgeliehen";
      } else if(!key.rentable) {
        return "Nicht ausleihbar";
      } else {
        return "Ausleihbar";
      }
    },

    row_classes(item) {
      if(item.active_rental == null && item.rentable) {
        return "green-cell"
      } else {
        return "red-cell";
      }
    },

    // make key icon green if current user rented it
    // currently not supported by backend
    getKeyColor(key) {
      return "initial";
    }
  },
  computed: {
    keyInDialogNumber() {
      if(!this.keyInDialog) return '';
      return this.keyInDialog.number;
    }
  }
}
</script>

<style scoped>
  div >>> .red-cell td:nth-last-child(2) {
    background-color: #DDC1BB;
    border-radius: 5px;
  }

  div >>> .green-cell td:nth-last-child(2) {
    background-color: #ABCC9F;
    border-radius: 5px;
  }
</style>