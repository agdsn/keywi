<template>
  <DataTable
      :headers="headers"
      :items="tableData"
      class="elevation-1"
      :loading="loading"
      loading-text="Lade Daten..."
      sort-by="name"
      ref="table"
  >
    <template v-slot:[`item.name`]="{ item }">
      <router-link :to="`/safe/${ item.id }`">{{ item.name }}</router-link>
    </template>
  </DataTable>
</template>

<script>
import api from "@/api/api";
import DataTable from "@/components/DataTable";

export default {
  name: "DetailTableSafes",
  components: {DataTable},
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
    tableData: null
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
        if(this.tableData.length == 0) this.$emit('empty');
      });
    }
  }
}
</script>

<style>

</style>