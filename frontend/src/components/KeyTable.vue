<template>
  <div>
    <DataTable
        ref="table"
        :headers="headers"
        :item-class="row_classes"
        :items="tableData"
        multi-sort
        :sort-by="['location.name', 'lock.name', 'number']"
        class="elevation-1"
        loading-text="Lade Daten..."
    >
      <template v-slot:header>
        <h2 class="ml-4">Schlüssel</h2>
      </template>

      <template v-slot:[`item.link`]="{ item }">
        <router-link :to="`/key/${item.id}`">
          <v-icon small>
            mdi-open-in-new
          </v-icon>
        </router-link>
      </template>

      <template v-slot:[`item.number`]="{ item }">
        <router-link :to="`/key/${ item.id }`">{{ item.number }}</router-link>
      </template>

      <template v-slot:[`item.lock.name`]="{ item }">
        <router-link :to="`/lock/${ item.lock.id }`">{{ item.lock.name }}</router-link>
      </template>

      <template v-slot:[`item.safe.name`]="{ item }">
        <router-link :to="`/safe/${ item.safe.id }`">{{ item.safe.name }}</router-link>
      </template>

      <template v-slot:[`item.location.name`]="{ item }">
        <router-link :to="`/location/${ item.location.id }`">{{ item.location.name }}</router-link>
      </template>

      <template v-slot:[`item.rental`]="{ item }">
        {{ getRentalStatus(item) }}
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
          <v-icon
              small
              @click="openDeletePrompt(item)"
          >
            mdi-delete
          </v-icon>

          <v-tooltip v-if="rentable(item) || rentedByUser(item)" top>
            <template v-slot:activator="{on}">
              <v-icon
                  :color="getKeyColor(item)"
                  class="ml-2"
                  small
                  @click="openRentPrompt(item)"
                  v-on="on"
              >
                mdi-hand-coin
              </v-icon>
            </template>

            <span>{{ getTooltip(item) }}</span>
          </v-tooltip>
        </div>
      </template>
    </DataTable>

    <v-dialog v-model="deleteDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{ keyInDialogNumber }} wirklich löschen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" @click="deleteItem">
            <v-icon left size="24">mdi-delete</v-icon>
            Bestätigen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="returnDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{ keyInDialogNumber }} wirklich zurückgeben?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" @click="returnItem">
            <v-icon left size="24">mdi-content-save-outline</v-icon>
            Bestätigen
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog ref="rentForm" v-model="rentDialog" width="500px">
      <v-card class="pb-1">
        <v-card-title>Schlüssel {{ keyInDialogNumber }} wirklich ausleihen?</v-card-title>
        <v-card-text>
          <v-form ref="form">
            <v-autocomplete v-model="pickedUser" :item-text="item => item.name" :items="users"
                            :rules="userRules" label="Vergeben an"
                            prepend-icon="mdi-account" return-object></v-autocomplete>
            <v-text-field v-model="grantingDocument" label="Dokument" prepend-icon="mdi-file-document"/>
            <v-textarea v-model="note" label="Notiz" prepend-icon="mdi-note-text-outline" rows="1"></v-textarea>

            <v-checkbox v-model="editStartDate" label="Startdatum bearbeiten"/>

      <v-menu
        v-model="menuStartDate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
              :disabled="!editStartDate"
              style="margin-top:-10px"
            v-model="dateStart"
            label="Startdatum"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStart"
          @input="menuStartDate = false"
        ></v-date-picker>
      </v-menu>

      <v-checkbox v-model="editEndDate" label="Enddatum bearbeiten"/>
      <v-menu
        v-model="menuEndDate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
              :disabled="!editEndDate"
              style="margin-top:-10px"
            v-model="dateEnd"
            label="Enddatum"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateEnd"
          @input="menuEndDate = false"
        ></v-date-picker>
      </v-menu>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" @click="rentKey">
            <v-icon left size="24">mdi-content-save-outline</v-icon>
            Speichern
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
  name: "KeyTable",
  components: {DataTable},
  data: () => ({
    keyInDialog: undefined,
    deleteDialog: false,
    rentDialog: false,
    returnDialog: false,
    grantingDocument: '',
    note: '',
    menuStartDate: false,
    editStartDate: false,
    dateStart: undefined,
    menuEndDate: false,
    editEndDate: false,
    dateEnd: undefined,
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
    usersLoaded: false,
    users: [],
    pickedUser: undefined,

    userRules: [
      v => !!v || 'Bitte Nutzer auswählen'
    ],
    keyId: undefined
  }),
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      let paramId = this.$route.params.id;

      const apiStub = await api;
      // load specific key if uuid is given in path parameter. load all keys if not
      if (paramId) {
        apiStub.key_getKey(paramId).then(response => {
          this.tableData = [response.data];
        });
      } else {
        apiStub.key_getKeys().then(response => {
          this.tableData = response.data;
        });
      }
    },

    editItem(key) {
      this.$emit('editItem', key);
    },

    openDeletePrompt(keyInDialog) {
      this.keyInDialog = keyInDialog;
      this.deleteDialog = true;
    },

    openRentPrompt(keyInDialog) {
      this.keyInDialog = keyInDialog;
      this.editStartDate = false;
        this.editEndDate = false;

      if (this.rentedByUser(keyInDialog)) {
        this.returnDialog = true;
      } else {
        this.loadUsers();
        this.rentDialog = true;

        this.grantingDocument = '';
        this.note = '';
        this.dateStart = '';
        this.dateEnd = '';
        this.pickedUser = undefined;

      }
    },

    async loadUsers() {
      if (this.usersLoaded) return;

      this.usersLoaded = true;
      const apiStub = await api;

      apiStub.user_getUsers().then(response => {
        this.users = response.data;
      })
    },

    async deleteItem() {
      const apiStub = await api;
      const param = {uuid: this.keyInDialog.id};
      apiStub.key_deleteKey(param).then(() => {
        this.deleteDialog = false;
        this.loadData();
      });
    },

    async returnItem() {
      const apiStub = await api;
      const param = {uuid: this.keyInDialog.active_rental.id};
      apiStub.rental_endRental(param).then(() => {
        this.returnDialog = false;
        this.loadData();
      });
    },

    dateToDatetime(date) {
      return date + 'T12:37';
    },

    async rentKey() {
      if (this.$refs.form.validate()) {
        const apiStub = await api;

        const rental = {
          key_id: this.keyInDialog.id,
          user_id: this.pickedUser.id,
          allowed_by: this.grantingDocument,
          note: this.note
        };

        if(this.editStartDate && this.dateStart) rental.begin = this.dateToDatetime(this.dateStart);
        if(this.editEndDate && this.dateEnd) rental.end = this.dateToDatetime(this.dateEnd);

        apiStub.rental_createRental(null, rental).then(() => {
          this.rentDialog = false;
          this.$refs.form.resetValidation();
          this.pickedUser = undefined;
          this.loadData();
        })
      }
    },

    getRentalStatus(key) {
      if (this.rentedByUser(key)) {
        return "Ausgeliehen (von dir)"
      } else if (key.active_rental) {
        return "Ausgeliehen";
      } else if (!key.rentable) {
        return "Nicht ausleihbar";
      } else {
        return "Ausleihbar";
      }
    },

    rentable(key) {
      return this.getRentalStatus(key) == "Ausleihbar";
    },

    row_classes(item) {
      if (item.active_rental == null && item.rentable) {
        return "green-cell";
      } else if (!item.rentable) {
        return "grey-cell";
      } else {
        return "red-cell";
      }
    },

    // make key icon green if current user rented it
    // currently not supported by backend
    getKeyColor(key) {
      return "initial";
    },

    getTooltip(key) {
      if (this.rentedByUser(key)) return "Schlüssel zurückgeben";
      else return "Schlüssel ausleihen";
    },

    rentedByUser(key) {
      if (!key.active_rental) return false;
      let user = AuthService.getUser();

      return user.id == key.active_rental.user_id;
    }
  },
  computed: {
    keyInDialogNumber() {
      if (!this.keyInDialog) return '';
      return this.keyInDialog.number;
    }
  }
}
</script>

<style scoped>
div >>> .red-cell td:nth-last-child(2) {
  background-color: #DDC1BB;
}

div >>> .green-cell td:nth-last-child(2) {
  background-color: #ABCC9F;
}

div >>> .grey-cell td:nth-last-child(2) {
  background-color: #c9c9c9;
}

</style>
