<template>
  <DataTable
      :headers="headers"
      :items="tableData"
      sort-by="name"
      ref="table"
  >
    <template v-slot:[`item.available_keys`]="{ item }">
      {{ item.amount_free_keys }} / {{ item.amount_keys }}
    </template>

    <template v-slot:[`item.name`]="{ item }">
      <router-link :to="`/lock/${ item.id }`">{{ item.name }}</router-link>
    </template>
  </DataTable>
</template>

<script>
import api from "@/api/api";
import DataTable from "@/components/DataTable";

export default {
  name: "DetailTableLocks",
  components: {DataTable},
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Schloss',
        value: "name"
      },
      {
        text: "Besitzer",
        value: "owner"
      },
      {
        text: "Verfügbare Schlüssel",
        value: "available_keys"
      }
    ],
    tableData: null
  }),
  methods: {
    async loadDataByLocationId(locationId) {
      // // remove location column
      // let locationColumn = this.headers.find(column => column.value == 'location.name');
      // if(locationColumn) delete locationColumn;

      const apiStub = await api;
      // load locks attached to location id
      let params = {
        location_id: locationId
      };

      apiStub.lock_getLocks(params).then(response => {
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