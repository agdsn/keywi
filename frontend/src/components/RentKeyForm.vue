<template>
  <v-form ref="form">
    <v-autocomplete v-model="pickedUser" :item-text="item => item.name + ' (' + item.email + ')'"  return-object
                    :items="users" label="Ausleihender Nutzer"
                    prepend-icon="mdi-account" :rules="userRules"></v-autocomplete>

    <v-text-field prepend-icon="mdi-file-document" label="Dokument" v-model="grantingDocument"/>
    <v-textarea prepend-icon="mdi-note-text-outline" rows="1" label="Notiz" v-model="note"></v-textarea>

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

    async save() {
      if (this.$refs.form.validate()) {
        const apiStub = await api;

        const rental = {
          key_id: this.keyId,
          user_id: this.pickedUser.id,
          allowed_by: this.grantingDocument,
          note: this.note
        };

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
