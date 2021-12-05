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
    <template v-slot:[`item.lock_name`] = "{ item }">
      <router-link :to="`/lock/${ item.lock_id }`">{{ item.lock_name }}</router-link>
    </template>

    <template v-slot:[`item.safe_name`] = "{ item }">
      <router-link :to="`/safe/${ item.safe_id }`">{{ item.safe_name }}</router-link>
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api/api";

export default {
  name: "KeyTable",
  props: [ "keyData" ],
  data: () => ({
    loading: true,
    headers: [
      {
        text: "Schloss",
        // lock-name als identifier schmeißt Fehler -> lock_name
        value: "lock_name"
      },
      {
        text: "Schlüsselnummer",
        value: "key_number"
      },
      {
        text: "Tresor",
        value: "safe_name"
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

      const apiStub = await api();
      // load specific key if uuid is given in path parameter. load all keys if not
      if(paramId) {
        apiStub.key_getKey(paramId).then(response => {
          let key = response.data;
          this.pushKeyToDataTable(key);
          this.loading = false;
        }).finally(() => {
          this.loading = false
        });
      } else {
        apiStub.key_getKeys().then(response => {
          response.data.forEach(key => {
            this.pushKeyToDataTable(key);
          });
        }).finally(() => {
          this.loading = false;
        })
      }
    },

    pushKeyToDataTable(key) {
      this.tableData.push({
              "lock_name": key.lock.name,
              "key_number": key.number,
              "safe_name": key.safe.name,
              "rental": this.getRentalStatus(key),
              "lock_id": key.lock.id,
              "safe_id": key.safe.id
            });
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
      if(item.rental === "Ausleihbar") {
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