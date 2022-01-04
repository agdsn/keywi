<template>
  <v-data-table
      :headers="headers"
      :items="tableData"
      :items-per-page="25"
      class="elevation-1"
      :loading="loading"
      loading-text="Lade Daten..."
      ref="table"
      :sort-by="['begin']"
      :sort-desc="true"
  >
    <template v-slot:[`item.begin`] = "{ item }">
        {{ new Date(item.begin).toLocaleString('de') }}
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api/api";

export default {
  name: "DetailTableKeys",
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Ausgeliehen von',
        value: "user.name"
      },
      {
        text: 'Beginn',
        value: "begin"
      },
      {
        text: 'Ende',
        value: "end"
      }
    ],
    tableData: []
  }),
  methods: {
    async loadData(keyId) {
      const apiStub = await api;
      // load rentals attached to key id
      let params = {
        key_id: keyId
      };

      apiStub.rental_getRentals(params).then(response => {
        this.tableData = response.data;
      }).finally(() => {
        this.loading = false;
      });
    }
  },
  computed: {

  }
}
</script>

<style scoped>

</style>