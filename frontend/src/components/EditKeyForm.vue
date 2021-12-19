<template>
    <v-form ref="form">
      <v-select :items="locks" label="Schloss" item-text="displayName" item-value="id" :rules="lockRule" v-model="selectedLockId"></v-select>
      <v-text-field label="Schlüsselnummer" v-model="number" :rules="numberRules" required/>
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
      number: '',
      locks: [],
      safes: [],
      selectedLockId: undefined,
      selectedSafeId: undefined,
      rentable: true,
      keyId: undefined,

      numberRules: [
          v => !!v || 'Schlüsselnummer erforderlich'
      ],

      lockRule: [
         v => !!v || "Bitte Schloss auswählen"
      ],
      safeRule: [
          v => !!v || "Bitte Tresor auswählen"
      ]
    }
  },
  mounted() {
    this.loadData();
    this.$emit('mounted');
  },
  methods: {
    fillForm(keyTemplate) {
      if(keyTemplate){
        this.keyId = keyTemplate.id;
        this.number = keyTemplate.number;
        this.rentable = keyTemplate.rentable;
        this.selectedSafeId = keyTemplate.safe.id;
        this.selectedLockId = keyTemplate.lock.id;
      } else {
        this.keyId = undefined;
        this.number = '';
        this.rentable = true;
        this.selectedSafeId = undefined;
        this.selectedLockId = undefined;
      }

      this.$refs.form.resetValidation();
    },

    
    async save() {
      if (this.$refs.form.validate() && this.selectedLockId && this.selectedSafeId) {
        const apiStub = await api;

        let keyModel = {
          number: this.number,
          lock_id: this.selectedLockId,
          safe_id: this.selectedSafeId,
          rentable: this.rentable
        }
        
        if(this.keyId) {
          const param = { uuid: this.keyId };

          apiStub.key_editKey(param, keyModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.key_createKey(null, keyModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        }
      }
    },
    async loadData() {
      const apiStub = await api;
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