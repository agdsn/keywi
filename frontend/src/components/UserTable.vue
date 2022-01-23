<template>
  <div>
    <DataTable
        ref="table"
        :headers="headers"
        :items="tableData"
        :items-per-page="25"
        :loading="loading"
        class="elevation-1"
        sort-by="name"
        loading-text="Lade Daten..."
    >
      <template v-slot:[`item.name`]="{ item }">
        <router-link :to="`/user/${ item.id }`">{{ item.name }}</router-link>
      </template>
    </DataTable>
  </div>
</template>

<script>
import api from "@/api/api";
import AuthService from "@/services/AuthService";
import DataTable from "@/components/DataTable";

export default {
  name: "UserTable",
  components: {DataTable},
  data: () => ({
    loading: true,
    headers: [
      {
        text: "Name",
        value: "name"
      },
      {
        text: "Nutzername",
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