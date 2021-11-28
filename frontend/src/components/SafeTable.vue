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
  name: "SafeTable",
  props: [ "safeData" ],
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Tresor',
        value: "safe-name"
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
      axios.get('http://localhost:6080/safe').then(response => {
        response.data.forEach(
          safe => {
            this.tableData.push({
              "safe-name": safe.name,
              "location-name": safe.location.name
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