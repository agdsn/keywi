<template>
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
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api/api";

export default {
  name: "LockTable",
  data: () => ({
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

    async deleteItem(lock) {
      // TODO: add confirmation prompt
      const apiStub = await api;
      const param = { uuid: lock.id };
      apiStub.lock_deleteLock(param).then(this.loadData);
    },
  }
}
</script>

<style>

</style>