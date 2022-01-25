<template>
  <v-form ref="form">
    <v-autocomplete v-model="pickedUser" :item-text="item => item.name + ' (' + item.email + ')'"  return-object
                    :items="users" label="Vergeben an"
                    prepend-icon="mdi-account" :rules="userRules"></v-autocomplete>

    <v-text-field prepend-icon="mdi-file-document" label="Dokument" v-model="grantingDocument"/>
    <v-textarea prepend-icon="mdi-note-text-outline" rows="1" label="Notiz" v-model="note"></v-textarea>

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

    <v-btn color="secondary" @click="save">
      <v-icon left size="24">mdi-content-save-outline</v-icon>
      Speichern
    </v-btn>
  </v-form>
</template>

<script>
import api from "@/api/api";
import AuthService from "@/services/AuthService";

export default {
name: "RentKeyForm",
  data() {
    return {
      users: [],
      pickedUser: undefined,
      grantingDocument: '',
      note: '',
      menuStartDate: false,
      editStartDate: false,
      dateStart: undefined,
      menuEndDate: false,
      editEndDate: false,
      dateEnd: undefined,

      userRules: [
          v => !!v || 'Bitte Nutzer auswählen'
      ],
      keyId: undefined
    }
  },

  mounted() {
    this.loadUsers();
    this.$emit('mounted');
  },

  methods: {
    setKeyId(keyId) {
      this.keyId = keyId;
      this.$refs.form.resetValidation();
    },

    async loadUsers() {
      const apiStub = await api;

      apiStub.user_getUsers().then(response => {
        this.users = response.data;
      })
    },

    dateToDatetime(date) {
      return date + 'T12:37';
    },

    async save() {
      if (this.$refs.form.validate()) {
        const apiStub = await api;

        const rental = {
          key_id: this.keyId,
          user_id: this.pickedUser.id,
          allowed_by: this.grantingDocument,
          note: this.note
        };

        if(this.editStartDate && this.dateStart) rental.begin = this.dateToDatetime(this.dateStart);
        if(this.editEndDate && this.dateEnd) rental.end = this.dateToDatetime(this.dateEnd);

        apiStub.rental_createRental(null, rental).then(() => {
          this.$emit('save-form');
        })
      }
    }

  }
}
</script>

<style scoped>
  .v-btn {
    background-color: var(--primary-color) !important;
    color: white;
    position: absolute;
    right: 0;
  }

  .v-form {
    position: relative;
  }
</style>
