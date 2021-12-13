<template>
  <v-data-table
    :headers="headers"
    :items="tableData"
    :items-per-page="25"
    class="elevation-1"
    :loading="loading"
    loading-text="Lade Daten..."
    ref="table"
    :item-class="row_classes"
  >
<!--    TODO: umschreiben als Komponente-->
    <template v-slot:[`item.lock.name`] = "{ item }">
      <router-link :to="`/lock/${ item.lock.id }`">{{ item.lock.name }}</router-link>
    </template>

    <template v-slot:[`item.safe.name`] = "{ item }">
      <router-link :to="`/safe/${ item.safe.id }`">{{ item.safe.name }}</router-link>
    </template>

    <template v-slot:[`item.location.name`] = "{ item }">
      <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
    </template>

    <template v-slot:[`item.rental`] = "{ item }">
      {{ getRentalStatus(item) }}
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api/api";

export default {
  name: "KeyTable",
  data: () => ({
    loading: true,
    headers: [
      {
        text: "Ort",
        value: "location.name"
      },
      {
        text: "Schloss",
        value: "lock.name"
      },
      {
        text: "Schlüsselnummer",
        value: "number"
      },
      {
        text: "Tresor",
        value: "safe.name"
      },
        {
        text: "Ausleihe",
        value: "rental"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific key if uuid is given in path parameter. load all keys if not
      if(paramId) {
        apiStub.key_getKey(paramId).then(response => {
          this.tableData = [response.data];

          this.loading = false;
        }).finally(() => {
          this.loading = false
        });
      } else {
        apiStub.key_getKeys().then(response => {
          this.tableData = response.data;
        }).finally(() => {
          this.loading = false;
        })
      }
    },


    getRentalStatus(key) {
      if(key.active_rental) {
        return "Ausgeliehen";
      } else if(!key.rentable) {
        return "Nicht ausleihbar";
      } else {
        return "Ausleihbar";
      }
    },

    row_classes(item) {
      if(item.active_rental == null && item.rentable) {
        return "green-cell"
      } else {
        return "red-cell";
      }
    }
  },
  computed: {

  }
}
</script>

<style>
  .red-cell td:last-child {
    background-color: #DDC1BB;
    border-radius: 5px;
  }

  .green-cell td:last-child {
    background-color: #ABCC9F;
    border-radius: 5px;
  }

  td a {
    text-decoration: none;
  }
</style>