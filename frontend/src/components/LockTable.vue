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
    <template v-slot:[`item.location_name`] = "{ item }">
      <router-link :to="`/location/${ item.location_id }`">{{ item.location_name }}</router-link>
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
        value: "lock-name"
      },
      {
        text: "Ort",
        value: "location_name"
      },
      {
        text: "Besitzer",
        value: "owner-name"
      },
      {
        text: "Verfügbare Schlüssel",
        value: "available-keys"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api();
      // load specific lock if uuid is given in path parameter. load all locks if not
      if(paramId) {
        apiStub.lock_getLock(paramId).then(response => {
          let lock = response.data;
          this.pushLockToDataTable(lock);
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.lock_getLocks().then(response => {
          response.data.forEach(lock => {
            this.pushLockToDataTable(lock);
          });
          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },

    pushLockToDataTable(lock) {
      this.tableData.push({
              "lock-name": lock.name,
              "location_name": lock.location.name,
              "location_id": lock.location.id,
              "owner-name": lock.owner,
              "available-keys": lock.amount_free_keys + " / " + lock.amount_keys
            });
    },
  }
}
</script>

<style>

</style>