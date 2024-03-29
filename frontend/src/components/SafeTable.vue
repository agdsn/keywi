<template>
  <div>
    <DataTable
      :headers="headers"
      :items="tableData"
      sort-by="name"
      ref="table"
    >
      <template v-slot:header>
        <h2 class="ml-4">Tresore</h2>
      </template>

      <template v-slot:[`item.location.name`] = "{ item }">
        <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
      </template>

      <template v-slot:[`item.name`] = "{ item }">
        <router-link :to="`/safe/${ item.id }`">{{ item.name }}</router-link>
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
        <v-card-title>Tresor {{safeToDeleteName}} wirklich löschen?</v-card-title>
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
  name: "SafeTable",
  components: {DataTable},
  data: () => ({
    dialog: false,
    safeToDelete: undefined,
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
        width: '200px',
        sortable: false,
        align: 'right',
      }
    ],
    tableData: null
  }),
  mounted() { this.loadData(); },
  computed: {
    safeToDeleteName() {
      if(!this.safeToDelete) return '';
      return this.safeToDelete.name;
    }
  },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific safe if uuid is given in path parameter. load all safes if not
      if(paramId) {
        apiStub.safe_getSafe(paramId).then(response => {
          this.tableData = [response.data];
        });
      } else {
        apiStub.safe_getSafes().then(response => {
          this.tableData = response.data;
        });
      }
    },

    editItem(safe) {
      this.$emit('editItem', safe);
    },

    openDeletePrompt(safeToDelete) {
      this.safeToDelete = safeToDelete;
      this.dialog = true;
    },

    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.safeToDelete.id };
      apiStub.safe_deleteSafe(param).then(() => {
        this.dialog = false;
        this.loadData();
      });
    },

  }
}
</script>

<style>

</style>