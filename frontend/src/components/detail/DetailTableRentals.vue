<template>
  <v-data-table
      ref="table"
      :headers="headers"
      :items="tableData"
      :items-per-page="25"
      :loading="loading"
      :sort-by="['begin']"
      :sort-desc="true"
      class="elevation-1"
      loading-text="Lade Daten..."
  >
    <template v-slot:[`item.begin`]="{ item }">
      {{ new Date(item.begin).toLocaleString('de') }}
    </template>

    <template v-slot:[`item.key.lock`]="{ item }">
        <router-link :to="`/lock/${ item.key.lock.id }`">{{ item.key.lock.name }}</router-link>
      </template>

    <template v-slot:[`item.key`]="{ item }">
        <router-link :to="`/key/${ item.key.id }`">{{ item.key.number }}</router-link>
      </template>

    <template v-slot:[`item.key.safe`]="{ item }">
        <router-link :to="`/safe/${ item.key.safe.id }`">{{ item.key.safe.name }}</router-link>
      </template>

        <template v-slot:[`item.user.name`]="{ item }">
        <router-link :to="`/user/${ item.user.id }`">{{ item.user.name }}</router-link>
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
        text: 'Schloss',
        value: "key.lock"
      },
      {
        text: 'Schlüsselnummer',
        value: "key"
      },
      {
        text: 'Tresor',
        value: "key.safe"
      },
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
    async loadDataByKeyId(keyId) {
      this.removeColumn("key.lock.name");
      this.removeColumn("key.number");
      this.removeColumn("key.safe.name");

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
    },

    async loadDataByUserId(userId) {
      this.removeColumn("user.name");

      const apiStub = await api;
      // load rentals attached to key id
      let params = {
        user_id: userId
      };

      apiStub.rental_getRentals(params).then(response => {
        this.tableData = response.data;
      }).finally(() => {
        this.loading = false;
      });
    },

    removeColumn(columnName) {
      let column = this.headers.find(column => column.value == columnName);
      let index = this.headers.indexOf(column);
      if (index > -1) this.headers.splice(index, 1);
    }
  },
  computed: {}
}
</script>

<style scoped>

</style>