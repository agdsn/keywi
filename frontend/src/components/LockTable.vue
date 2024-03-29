<template>
  <div>
    <DataTable
      :headers="headers"
      :items="tableData"
      class="elevation-1"
      multi-sort
      :sort-by="['location.name', 'name']"
      loading-text="Lade Daten..."
      ref="table"
    >
      <template v-slot:header>
        <h2 class="ml-4">Schlösser</h2>
      </template>

      <template v-slot:[`item.link`]="{ item }">
        <router-link :to="`/lock/${item.id}`">
          <v-icon small>
            mdi-open-in-new
          </v-icon>
        </router-link>
      </template>
      <template v-slot:[`item.location.name`] = "{ item }">
        <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
      </template>
      <template v-slot:[`item.name`] = "{ item }">
        <router-link :to="`/lock/${ item.id }`">{{ item.name }}</router-link>
      </template>
      <template v-slot:[`item.available_keys`] = "{ item }">
        {{ item.amount_free_keys }} / {{ item.amount_keys }}
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
        <v-card-title>Schloss {{lockToDeleteName}} wirklich löschen?</v-card-title>
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
  name: "LockTable",
  components: {DataTable},
  data: () => ({
    dialog: false,
    lockToDelete: undefined,
    headers: [
      {
        width: '5%',
        text: 'Link',
        value: "link"
      },
      {
        text: "Ort",
        value: "location.name"
      },
      {
        text: 'Schloss',
        value: "name"
      },
      {
        text: "Besitzer",
        value: "owner"
      },
      {
        text: "Verfügbare Schlüssel",
        value: "available_keys"
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
  computed: {
    lockToDeleteName() {
      if(!this.lockToDelete) return '';
      return this.lockToDelete.name;
    }
  },
  mounted() { this.loadData(); },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific lock if uuid is given in path parameter. load all locks if not
      if(paramId) {
        apiStub.lock_getLock(paramId).then(response => {
          this.tableData = [response.data];
        });
      } else {
        apiStub.lock_getLocks().then(response => {
          this.tableData = response.data;
        });
      }
    },

    editItem(lock) {
      this.$emit('editItem', lock);
    },

    openDeletePrompt(lockToDelete) {
      this.lockToDelete = lockToDelete;
      this.dialog = true;
    },

    async deleteItem() {
      const apiStub = await api;
      const param = { uuid: this.lockToDelete.id };
      apiStub.lock_deleteLock(param).then(() => {
        this.dialog = false;
        this.loadData();
      });
    },
  }
}
</script>

<style>

</style>
