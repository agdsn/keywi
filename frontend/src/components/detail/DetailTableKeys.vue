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

    <template v-slot:[`item.safe.name`] = "{ item }">
        <router-link :to="`/safe/${ item.safe.id }`">{{ item.safe.name }}</router-link>
    </template>

    <template v-slot:[`item.lock.name`] = "{ item }">
        <router-link :to="`/lock/${ item.lock.id }`">{{ item.lock.name }}</router-link>
    </template>

    <template v-slot:[`item.rental`] = "{ item }">
        {{ getRentalStatus(item) }}
    </template>

    <template v-slot:[`item.actions`]="{ item }">
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
  name: "DetailTableKeys",
  data: () => ({
    loading: true,
    keyInDialog: undefined,
    rentDialog: false,
    headers: [
      {
        text: 'Schlüsselnummer',
        value: "number"
      },
      {
        text: 'Tresor',
        value: "safe.name"
      },
      {
        text: 'Schloss',
        value: "lock.name"
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
  methods: {
    async loadDataBySafeId(safeId) {
      // remove safe column
      let safeColumn = this.headers.find(column => column.value == 'safe.name');
      let index = this.headers.indexOf(safeColumn);
      if(index > -1) this.headers.splice(index, 1);

      const apiStub = await api;
      // load safes attached to location id
      let params = {
        safe_id: safeId
      };

      apiStub.key_getKeys(params).then(response => {
        this.tableData = response.data;
      }).finally(() => {
        this.loading = false;

        if(this.tableData.length == 0) this.$emit('empty');
      });
    },
    
    async loadDataByLockId(lockId) {
      // remove lock column
      let lockColumn = this.headers.find(column => column.value == 'lock.name');
      let index = this.headers.indexOf(lockColumn);
      if(index > -1) this.headers.splice(index, 1);

      const apiStub = await api;
      // load locks attached to location id
      let params = {
        lock_id: lockId
      };

      apiStub.key_getKeys(params).then(response => {
        this.tableData = response.data;
      }).finally(() => {
        this.loading = false;

        if(this.tableData.length == 0) this.$emit('empty');
      });
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

    getKeyColor(key) {
      return "initial";
    },

    openRentPrompt(keyInDialog) {
      this.keyInDialog = keyInDialog;
      this.rentDialog = true;
    },

    async rentItem() {
      const apiStub = await api;
      const rentalModel = {
        key_id: this.keyInDialog.id,
        begin: new Date().toISOString(),
        // TODO: change
        user_id: '79d9d0f6-d424-4992-872c-4f257d9ae5c5'
      }

      apiStub.rental_createRental(null, rentalModel).then(() => {
        this.rentDialog = false;
        this.$emit('rented');
      })
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
  .v-data-table >>> .red-cell td:nth-last-child(2) {
    background-color: #DDC1BB;
    border-radius: 5px;
  }

  .v-data-table >>> .green-cell td:nth-last-child(2) {
    background-color: #ABCC9F;
    border-radius: 5px;
  }
</style>