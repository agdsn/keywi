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
    <template v-slot:[`item.location.name`] = "{ item }">
      <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
    </template>

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
  name: "SafeTable",
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Tresor',
        value: "name"
      },
      {
        text: "Ort",
        value: "location.name"
      },
      {
        text: "Anzahl Schlüssel",
        value: "amount_keys"
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
      // load specific safe if uuid is given in path parameter. load all safes if not
      if(paramId) {
        apiStub.safe_getSafe(paramId).then(response => {
          this.tableData = [response.data];
        }).finally(() => {
          this.loading = false;
        });
      } else {
        apiStub.safe_getSafes().then(response => {
          this.tableData = response.data;
          this.loading = false;
        }).finally(() => {
          this.loading = false;
        });
      }
    },

    editItem(safe) {
      this.$emit('editItem', safe);
    },

    async deleteItem(safe) {
      // TODO: add confirmation prompt
      const apiStub = await api;
      const param = { uuid: safe.safe_id };
      apiStub.safe_deleteSafe(param);
    },

  }
}
</script>

<style>

</style>