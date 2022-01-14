<template>
  <v-form ref="form">
    <v-autocomplete v-model="pickedUser" :item-text="item => item.name" return-object
                    :items="users" label="Ausleihender Nutzer"
                    prepend-icon="mdi-account" :rules="userRules"></v-autocomplete>

    <v-btn class="primary-color" color="validate" @click="save">
      <v-icon>mdi-content-save-outline</v-icon>
      Speichern
    </v-btn>
  </v-form>
</template>

<script>
import api from "@/api/api";
import AuthService from "@/services/AuthService";
import DatetimePicker from 'vuetify-datetime-picker'

export default {
name: "RentKeyForm",
  data() {
    return {
      users: [],
      pickedUser: undefined,

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
          user_id: this.pickedUser.id
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