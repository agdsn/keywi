<template>
  <v-data-table
    :headers="headers"
    :items="tableData"
    :items-per-page="25"
    class="elevation-1"
    :loading="loading"
    loading-text="Lade Daten..."
    ref="table"
  ></v-data-table>
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
        value: "location-name"
      },
      {
        text: "Adresse",
        value: "location-address"
      },
      {
        text: "Anzahl Tresore",
        value: "location-number-safes"
      },
      {
        text: "Anzahl Schlösser",
        value: "location-number-locks"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api();


      // load specific location if uuid is given in path parameter. load all locations if not
      if(paramId) {
        apiStub.location_getLocation(paramId).then(response => {
          let location = response.data;
          this.pushLocationToDataTable(location);
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.location_getLocations().then(response => {
          response.data.forEach(location => {
            this.pushLocationToDataTable(location);
          });
          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },

    pushLocationToDataTable(location) {
      this.tableData.push({
        "location-name": location.name,
        "location-address": location.address,
        "location-number-safes": location.amount_safes,
        "location-number-locks": location.amount_locks
      });
    },
  }
}
</script>

<style>

</style>