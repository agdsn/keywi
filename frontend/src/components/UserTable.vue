<template>
  <div>
    <v-data-table
        ref="table"
        :headers="headers"
        :items="tableData"
        :items-per-page="25"
        :loading="loading"
        class="elevation-1"
        loading-text="Lade Daten..."
    >
      <template v-slot:[`item.name`]="{ item }">
        <router-link :to="`/user/${ item.id }`">{{ item.name }}</router-link>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import api from "@/api/api";
import AuthService from "@/services/AuthService";

export default {
  name: "UserTable",
  data: () => ({
    loading: true,
    headers: [
      {
        text: "Name",
        value: "name"
      },
      {
        text: "Username",
        value: "login"
      },
      {
        text: "Mail-Adresse",
        value: "email"
      }
    ],
    tableData: []
  }),
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific user if uuid is given in path parameter. load all users if not
      if (paramId) {
        apiStub.user_getUser(paramId).then(response => {
          this.tableData = [response.data];

          this.loading = false;
        });
      } else {
        apiStub.user_getUsers().then(response => {
          this.tableData = response.data;
          this.loading = false;
        })
      }
    }
  }
}
</script>

<style scoped>

</style>