<template>
  <div>
    <DataTable
        ref="table"
        :headers="headers"
        :items="tableData"
        sort-by="timestamp"
        :sort-desc="true"
    >
      <template v-slot:header>
        <h2 class="ml-4">Logs</h2>
      </template>

      <template v-slot:[`item.timestamp`]="{ item }">
        {{ new Date(item.timestamp).toLocaleString() }}
      </template>

      <template v-slot:[`item.creator.name`]="{ item }">
        <router-link :to="`/user/${ item.creator.id }`">{{ item.creator.name }}</router-link>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <div class="text-right">
          <span v-for="obj in ['location', 'key', 'user', 'lock', 'safe', 'rental']" v-bind:key="obj"
                style="cursor: pointer">
            <router-link :to="`/${obj}/${item[obj].id}`" v-if="item[obj] != null" class="mr-2 mt-1"
                         style="cursor: pointer">
              <v-chip color="secondary" outlined style="cursor: pointer">
                <v-icon small class="mr-1">
                  {{ obj_icons[obj] }}
                </v-icon>
                <span v-if="item[obj].name">{{ item[obj].name }}</span>
                <span v-else-if="item[obj].number">{{ item[obj].number }}</span>
                <span v-else-if="item[obj].begin">{{ new Date(item[obj].begin).getDate().toLocaleString() }}</span>
              </v-chip>
            </router-link>
          </span>
        </div>
      </template>
    </DataTable>
  </div>
</template>

<script>
import api from "@/api/api";
import DataTable from "@/components/DataTable";

export default {
  name: "DetailTableLogs",
  components: {DataTable},
  data: () => ({
    headers: [
      {
        text: 'Datum',
        value: "timestamp",
        width: '10%',
      },
      {
        text: 'Nutzer',
        value: "creator.name"
      },
      {
        text: 'Nachricht',
        value: "message"
      },
      {
        text: "Links",
        value: "actions",
        width: '20%',
        sortable: false,
        align: 'right',
      },
    ],
    tableData: null,
    obj_icons: {
      'location': 'mdi-map-marker',
      'key': 'mdi-key',
      'user': 'mdi-account',
      'lock': 'mdi-lock',
      'safe': 'mdi-safe-square',
      'rental': 'mdi-hand-coin',
    }
  }),
  methods: {
    async loadData(filter) {
      const apiStub = await api;

      apiStub.log_getLogs(filter).then(response => {
        this.tableData = response.data;
      });
    },

  },
  computed: {

  }
}
</script>
