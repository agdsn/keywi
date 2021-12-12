<template>
    <v-form ref="form">
      <v-select :items="locks" label="Schloss" item-text="displayName" item-value="id" :rules="lockRule" v-model="selectedLockId"></v-select>
      <v-text-field label="Schlüsselnummer" v-model="name" :rules="nameRules" required/>
      <v-select :items="safes" label="Tresor" item-text="displayName" item-value="id" :rules="safeRule" v-model="selectedSafeId"></v-select>
      <v-checkbox v-model="rentable" label="Ausleihbar"></v-checkbox>
      <v-btn color="validate" @click="save">
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api";

export default {
  name: "EditKeyForm",
  data() {
    return {
      name: '',
      locks: [],
      safes: [],
      selectedLockId: undefined,
      selectedSafeId: undefined,
      rentable: true,

      nameRules: [
          v => !!v || 'Name erforderlich'
      ],

      lockRule: [
         v => !!v || "Bitte Schloss auswählen"
      ],
      safeRule: [
          v => !!v || "Bitte Tresor auswählen"
      ]
    }
  },
  mounted() { this.loadData(); },
  methods: {
    async save() {
      if (this.$refs.form.validate() && this.selectedLockId && this.selectedSafeId) {
        const apiStub = await api();

        let keyModel = {
          number: this.name,
          lock_id: this.selectedLockId,
          safe_id: this.selectedSafeId,
          rentable: this.rentable
        }

        apiStub.key_createKey(null, keyModel).then(() => {
          this.$refs.form.reset();
          this.$parent.$emit('save-form');
        });
      }
    },
    async loadData() {
      const apiStub = await api();
      apiStub.lock_getLocks().then(response => {
        this.locks = response.data;
        this.locks.forEach(lock => {
          lock.displayName = lock.name + " (" + lock.location.name + ")";
        })
      }).then(apiStub.safe_getSafes
      ).then(response => {
        this.safes = response.data;
        this.safes.forEach(safe => {
          safe.displayName = safe.name + " (" + safe.location.name + ")";
        })
      })
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