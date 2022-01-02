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
  </v-data-table>
</template>

<script>
import api from "@/api/api";

export default {
  name: "DetailTableSafes",
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Tresor',
        value: "name"
      },
      {
        text: "Anzahl Schlüssel",
        value: "amount_keys"
      }
    ],
    tableData: []
  }),
  methods: {
    async loadDataByLocationId(locationId) {
      const apiStub = await api;
      // load safes attached to location id
      let params = {
        location_id: locationId
      };

      apiStub.safe_getSafes(params).then(response => {
        this.tableData = response.data;
      }).finally(() => {
        this.loading = false;
      });
    }
  }
}
</script>

<style>

</style>