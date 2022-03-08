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
            <td>Rolle</td>
            <td>
              {{ user.role }}
            </td>
          </tr>
          <tr>
            <td>Notiz</td>
            <td>{{ user.note }}</td>
          </tr>
          </tbody>
        </template>
      </v-simple-table>

      <v-divider></v-divider>

      <div class="buttons">
        <v-btn color="secondary" class="mx-8 my-4" @click="downloadProtocol">
          <v-icon left size="24">mdi-file-download</v-icon>
          Protokoll
        </v-btn>
      </div>

      <detail-table-rentals class="mt-10" ref="rentalTable"></detail-table-rentals>
      <detail-table-logs class="mt-10" ref="logTable"></detail-table-logs>

    </div>
  </v-card>
</template>

<script>
import api from "@/api/api";
import DetailTableRentals from "@/components/detail/DetailTableRentals";
import AuthService from "@/services/AuthService";
import DetailTableLogs from "@/components/detail/DetailTableLogs";

export default {
  name: "DetailUserView",
  components: {
    DetailTableLogs,
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
    this.loadLogs();
  },
  methods: {
    loadLogs() {
      this.$refs.logTable.loadData({ user_id: this.userId });
    },
    async loadUser() {
      if (!this.userId) return;

      const apiStub = await api;
      apiStub.user_getUser(this.userId).then(response => {
        this.user = response.data;
      });
    },
    async loadRentals() {
      this.$refs.rentalTable.loadDataByUserId(this.userId);
    },
    showFile(blob, name, mediaType = 'application/pdf') {
      // It is necessary to create a new blob object with mime-type explicitly set
      // otherwise only Chrome works like it should
      const newBlob = new Blob([blob], { type: mediaType });

      // For other browsers:
      // Create a link pointing to the ObjectURL containing the blob.
      const data = window.URL.createObjectURL(newBlob);
      const link = document.createElement('a');
      link.href = data;
      link.download = name;
      link.click();
      setTimeout(() => {
        // For Firefox it is necessary to delay revoking the ObjectURL
        window.URL.revokeObjectURL(data);
      }, 100);
    },
    async downloadProtocol() {
      const apiStub = await api;
      apiStub.user_getUserProtocol(
          { uuid: this.user.id },
          null,
          { responseType: 'blob' },
      ).then((rsp) => {
        const date = new Date();
        const isoDate = date.getFullYear() + '-' + String(date.getMonth() + 1).padStart(2, '0') + '-' + String(date.getDate()).padStart(2, '0');

        this.showFile(rsp.data, `${this.user.login}-${isoDate}.pdf`);
      });
    },
  }
}
</script>

<style scoped>
.buttons {
  text-align: end;
}

.buttons >>> .v-btn {
  margin-right: 0 !important;
  margin-left: 16px !important;
  margin-bottom: 0 !important;
}

.buttons .tooltip {
  display: inline-block;
}

.buttons .tooltip .v-btn {
  margin-right: 0 !important;
  margin-left: 16px !important;
  margin-bottom: 0 !important;
}
</style>
