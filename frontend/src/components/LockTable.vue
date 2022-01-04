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
    >
      <template v-slot:[`item.location.name`] = "{ item }">
        <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
      </template>
      <template v-slot:[`item.name`] = "{ item }">
        <router-link :to="`/lock/${ item.id }`">{{ item.name }}</router-link>
      </template>
      <template v-slot:[`item.available_keys`] = "{ item }">
        {{ item.amount_free_keys }} / {{ item.amount_keys }}
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
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schloss {{lockToDeleteName}} wirklich löschen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="primary-color" @click="deleteItem">Bestätigen</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "@/api/api";

export default {
  name: "LockTable",
  data: () => ({
    dialog: false,
    lockToDelete: undefined,
    loading: true,
    headers: [
      {
        text: 'Schloss',
        value: "name"
      },
      {
        text: "Ort",
        value: "location.name"
      },
      {
        text: "Besitzer",
        value: "owner"
      },
      {
        text: "Verfügbare Schlüssel",
        value: "available_keys"
      },
      {
        text: "Aktionen",
        value: "actions",
        sortable: false
      }
    ],
    tableData: []
  }),
  computed: {
    lockToDeleteName() {
      if(!this.lockToDelete) return '';
      return this.lockToDelete.name;
    }
  },
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific lock if uuid is given in path parameter. load all locks if not
      if(paramId) {
        apiStub.lock_getLock(paramId).then(response => {
          this.tableData = [response.data];
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.lock_getLocks().then(response => {
          this.tableData = response.data;

          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },

    editItem(lock) {
      this.$emit('editItem', lock);
    },

    openDeletePrompt(lockToDelete) {
      this.lockToDelete = lockToDelete;
      this.dialog = true;
    },

    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.lockToDelete.id };
      apiStub.lock_deleteLock(param).then(() => {
        this.dialog = false;
        this.loadData();
      });
    },
  }
}
</script>

<style>

</style>