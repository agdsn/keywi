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
import axios from "axios";

export default {
  name: "LockTable",
  props: [ "lockData" ],
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Schloss',
        value: "lock-name"
      },
      {
        text: "Ort",
        value: "location-name"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    loadData() {
      axios.get('http://localhost:6080/lock').then(response => {
        response.data.forEach(
          lock => {
            this.tableData.push({
              "lock-name": lock.name,
              "location-name": lock.location.name
            });
          }
        );
        this.loading = false;
      })
    },
  }
}
</script>

<style>

</style>