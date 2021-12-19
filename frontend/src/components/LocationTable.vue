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
  name: "LocationTable",
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Ort',
        value: "name"
      },
      {
        text: "Adresse",
        value: "address"
      },
      {
        text: "Anzahl Tresore",
        value: "amount_safes"
      },
      {
        text: "Anzahl Schlösser",
        value: "amount_locks"
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

      // load specific location if uuid is given in path parameter. load all locations if not
      if(paramId) {
        apiStub.location_getLocation(paramId).then(response => {
          this.tableData = [response.data];
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.location_getLocations().then(response => {
          this.tableData = response.data;

          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },

    editItem(location) {
      this.$emit('editItem', location);
    },

    async deleteItem(location) {
      // TODO: add confirmation prompt
      const apiStub = await api;
      const param = { uuid: location.id };
      apiStub.location_deleteLocation(param).then(this.loadData);
    },
  }
}
</script>

<style>

</style>