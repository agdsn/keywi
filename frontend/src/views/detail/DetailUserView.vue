<template>
  <v-card class="home pb-5 pt-1">
    <div class="mx-8">
      <h2 class="my-2">Nutzer Daten</h2>
      <v-simple-table>
        <template v-slot:default>
          <tbody>
          <tr>
            <td style="width: 20%;">Name</td>
            <td><b>{{ user.name }}</b></td>
          </tr>
          <tr>
            <td>Loginname</td>
            <td>
              {{ user.login }}
            </td>
          </tr>
          <tr>
            <td>Mail-Adresse</td>
            <td>
              {{ user.email }}
            </td>
          </tr>
          <tr>
            <td>Notiz</td>
            <td>{{ user.note }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>

      <v-divider class="mb-8"></v-divider>

      <h2 class="mb-2">Ausleihhistorie</h2>

      <detail-table-rentals ref="rentalTable"></detail-table-rentals>

    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableRentals from "@/components/detail/DetailTableRentals";
import AuthService from "@/services/AuthService";

export default {
  name: "DetailUserView",
  components: {
    DetailTableRentals
  },

  data() {
    return {
      user: {name: '', login: '', email: '', note: ''},
      userId: undefined
    }
  },
  mounted() {
    this.userId = this.$route.params.id;
    this.loadUser();
    this.loadRentals();
  },
  methods: {
    async loadUser() {
      if (!this.userId) return;

      const apiStub = await api;
      apiStub.user_getUser(this.userId).then(response => {
        this.user = response.data;
      });
    },

    async loadRentals() {
      this.$refs.rentalTable.loadDataByUserId(this.userId);
    }
  }
}
</script>

<style scoped>

</style>