<template>
  <div>
    <DataTable
        ref="table"
        :headers="headers"
        :items="tableData"
        sort-by="begin"
        :sort-desc="true"
    >
      <template v-slot:[`item.link`]="{ item }">
        <router-link :to="`/rental/${item.id}`">
          <v-icon small>
            mdi-open-in-new
          </v-icon>
        </router-link>
      </template>

      <template v-slot:[`item.begin`]="{ item }">
        {{ new Date(item.begin).toLocaleString('de') }}
      </template>

      <template v-slot:[`item.end`]="{ item }">
      <span v-if="item.end != null">
        {{ new Date(item.end).toLocaleString('de') }}
      </span>
        <span v-else>
        -
      </span>
      </template>

      <template v-slot:[`item.key.lock.location`]="{ item }">
        <router-link :to="`/location/${ item.key.lock.location.id }`">{{ item.key.lock.location.name }}</router-link>
      </template>

      <template v-slot:[`item.key.lock`]="{ item }">
        <router-link :to="`/lock/${ item.key.lock.id }`">{{ item.key.lock.name }}</router-link>
      </template>

      <template v-slot:[`item.key`]="{ item }">
        <router-link :to="`/key/${ item.key.id }`">{{ item.key.number }}</router-link>
      </template>

      <template v-slot:[`item.user.name`]="{ item }">
        <router-link :to="`/user/${ item.user.id }`">{{ item.user.name }}</router-link>
      </template>

      <template v-slot:[`item.issuing_user.name`]="{ item }">
        <router-link :to="`/user/${ item.issuing_user.id }`">{{ item.issuing_user.name }}</router-link>
      </template>

      <template v-slot:[`item.actions`]="{ item }">
        <div class="text-right">
          <v-icon
              class="mr-2"
              small
              @click="editItem(item)"
          >
            mdi-pencil
          </v-icon>

          <v-tooltip top v-if="item.active">
            <template v-slot:activator="{on}">
              <v-icon
                  class="mr-2"
                  small
                  @click="openReturnPrompt(item)"
                  v-on="on"
              >
                mdi-arrow-u-left-bottom
              </v-icon>
            </template>

            <span>Schlüssel zurückgeben</span>
          </v-tooltip>
        </div>
      </template>
    </DataTable>

    <v-dialog v-model="returnDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{ rentalInDialog.key.number }} wirklich zurückgeben?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" @click="returnItem">
            <v-icon left size="24">mdi-check</v-icon>
            Bestätigen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "@/api/api";
import AuthService from "@/services/AuthService";
import DataTable from "@/components/DataTable";

export default {
  name: "RentalTable",
  components: {DataTable},
  data: () => ({
    dialog: false,
    headers: [
      {
        width: '5%',
        text: 'Link',
        value: "link"
      },
      {
        text: 'Ort',
        value: "key.lock.location"
      },
      {
        text: 'Schloss',
        value: "key.lock"
      },
      {
        text: 'Schlüsselnummer',
        value: "key"
      },
      {
        text: 'Ausgeliehen von',
        value: "user.name"
      },
      {
        text: 'Ausgegeben von',
        value: "issuing_user.name"
      },
      {
        text: 'Beginn',
        value: "begin"
      },
      {
        text: 'Ende',
        value: "end"
      },
      {
        text: "Aktionen",
        value: "actions",
        width: '200px',
        sortable: false,
        align: 'right',
      },
    ],
    tableData: null,
    rentalInDialog: {key:{}},
    returnDialog: false
  }),
  mounted() {
    this.loadData();
  },

  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;

      // load specific rental if uuid is given in path parameter. load all rentals if not
      if (paramId) {
        apiStub.rental_getRental(paramId).then(response => {
          this.tableData = [response.data];
        });
      } else {
        apiStub.rental_getRentals().then(response => {
          this.tableData = response.data;
        });
      }
    },

    editItem(rental) {
      this.$emit('editItem', rental);
    },

    rentedByUser(rental) {
      if (!rental.active) return false;
      let user = AuthService.getUser();

      return user.id == rental.user.id;
    },

    openReturnPrompt(rental) {
      this.rentalInDialog = rental;
      this.returnDialog = true;
    },

    async returnItem() {
      const apiStub = await api;
      const param = {uuid: this.rentalInDialog.id};
      apiStub.rental_endRental(param).then(() => {
        this.returnDialog = false;
        this.loadData();
      });
    }
  }
}
</script>

<style>

</style>