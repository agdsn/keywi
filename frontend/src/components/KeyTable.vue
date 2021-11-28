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
  ></v-data-table>
</template>

<script>
import axios from "axios";

export default {
  name: "KeyTable",
  props: [ "keyData" ],
  data: () => ({
    loading: true,
    headers: [
      {
        text: 'Schlüssel ID',
        value: "key-id"
      },
      {
        text: "Schloss",
        value: "lock-name"
      },
      {
        text: "Tresor",
        value: "safe-name"
      },
        {
        text: "Ausleihbar",
        value: "rentable"
      }
    ],
    tableData: []
  }),
  mounted() { this.loadData(); },
  methods: {
    loadData() {
      axios.get('http://localhost:6080/key').then(response => {
        response.data.forEach(
          key => {
            this.tableData.push({
              "key-id": key.id,
              "lock-name": key.lock.name,
              "safe-name": key.safe.name,
              "rentable": this.isRentable(key) ? "Ja" : "Nein"
            });
          }
        );
        this.loading = false;
      })
    },

    isRentable(key) {
      return key.rentable && !key.checked;
    },

    row_classes(item) {
      console.log("row classes");
      console.log(item.rentable);
      if(item.rentable === "Ja") {
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
  .red-cell :last-child {
    background-color: #DDC1BB;
    border-radius: 5px;
  }

  .green-cell :last-child {
    background-color: #ABCC9F;
    border-radius: 5px;
  }
</style>