<template>
  <div>
    <DataTable
      :headers="headers"
      :items="tableData"
      class="elevation-1"
      sort-by="name"
      ref="table"
    >
      <template v-slot:header>
        <h2 class="ml-4">Orte</h2>
      </template>

      <template v-slot:[`item.name`] = "{ item }">
        <router-link :to="`/location/${ item.id }`">{{ item.name }}</router-link>
      </template>
      <template v-slot:[`item.actions`]="{ item }">
        <div class="text-right">
          <v-icon
            small
            class="mr-2"
            @click="editItem(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            small
            @click="openDeletePrompt(item)"
          >
            mdi-delete
          </v-icon>
        </div>
      </template>
    </DataTable>

    <v-dialog v-model="dialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Ort {{locationToDeleteName}} wirklich löschen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" @click="deleteItem">
            <v-icon left size="24">mdi-delete</v-icon>
            Bestätigen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "@/api/api";
import DataTable from "@/components/DataTable";

export default {
  name: "LocationTable",
  components: {DataTable},
  data: () => ({
    dialog: false,
    locationToDelete: undefined,
    headers: [
      {
        text: 'Ort',
        value: "name"
      },
      {
        text: "Adresse",
        value: "address"
      },
      {
        text: "Anzahl Tresore",
        value: "amount_safes"
      },
      {
        text: "Anzahl Schlösser",
        value: "amount_locks"
      },
      {
        text: "Aktionen",
        value: "actions",
        width: '200px',
        sortable: false,
        align: 'right',
      },
    ],
    tableData: null
  }),
  mounted() { this.loadData(); },
  computed: {
    locationToDeleteName() {
      if(!this.locationToDelete) return '';
      return this.locationToDelete.name;
    }
  },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;

      // load specific location if uuid is given in path parameter. load all locations if not
      if(paramId) {
        apiStub.location_getLocation(paramId).then(response => {
          this.tableData = [response.data];
        });
      } else {
        apiStub.location_getLocations().then(response => {
          this.tableData = response.data
        });
      }
    },

    editItem(location) {
      this.$emit('editItem', location);
    },

    openDeletePrompt(locationToDelete) {
      this.locationToDelete = locationToDelete;
      this.dialog = true;
    },

    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.locationToDelete.id };
      apiStub.location_deleteLocation(param).then(() => {
        this.dialog = false;
        this.loadData();
      });
    },
  }
}
</script>

<style>

</style>