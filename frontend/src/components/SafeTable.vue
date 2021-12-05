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
      },
      {
        text: "Anzahl Schlüssel",
        value: "amount-keys"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api();
      // load specific safe if uuid is given in path parameter. load all safes if not
      if(paramId) {
        apiStub.safe_getSafe(paramId).then(response => {
          let safe = response.data;
          this.pushSafeToDataTable(safe);
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.safe_getSafes().then(response => {
          response.data.forEach(safe => {
            this.pushSafeToDataTable(safe);
          });
          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },
    
    pushSafeToDataTable(safe) {
      this.tableData.push({
        "safe-name": safe.name,
        "location-name": safe.location.name,
        "amount-keys": safe.amount_keys
      });
    },
  }
}
</script>

<style>

</style>