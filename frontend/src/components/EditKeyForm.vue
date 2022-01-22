<template>
    <v-form ref="form">
      <v-autocomplete prepend-icon="mdi-lock" :items="locks" label="Schloss" :item-text="item => getDisplayName(item)" :item-value="item => item.id" :rules="lockRule" v-model="selectedLock" return-object></v-autocomplete>
      <v-text-field prepend-icon="mdi-key" label="Schlüsselnummer" v-model="number" :rules="numberRules" required/>
      <v-autocomplete prepend-icon="mdi-safe-square-outline" :items="safes" label="Tresor" :item-text="item => getDisplayName(item)" :item-value="item => item.id" :rules="safeRule" v-model="selectedSafe" return-object></v-autocomplete>
      <v-checkbox v-model="rentable" label="Ausleihbar"></v-checkbox>
      <v-textarea prepend-icon="mdi-note-text-outline" rows="1" label="Notiz" v-model="note"></v-textarea>

      <v-btn color="validate" @click="save">
        <v-icon left size="24">mdi-content-save-outline</v-icon>
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api"

export default {
  name: "EditKeyForm",
  data() {
    return {
      number: '',
      locks: [],
      safes: [],
      selectedLock: undefined,
      selectedSafe: undefined,
      rentable: true,
      note: '',
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
        this.selectedSafe = keyTemplate.safe;
        this.selectedLock = keyTemplate.lock;
        this.note = keyTemplate.note;
        this.selectedLock = keyTemplate.selectedLock;
        this.selectedSafe = keyTemplate.selectedSafe;
      } else {
        this.keyId = undefined;
        this.number = '';
        this.rentable = true;
        this.selectedSafe = undefined;
        this.selectedLock = undefined;
        this.note = '';
      }

      this.$refs.form.resetValidation();
    },

    getDisplayName(item) {
      if(!item.location) return item.name;
      return item.name + " (" + item.location.name + ")";
    },
    
    async save() {
      if (this.$refs.form.validate() && this.selectedLock && this.selectedSafe) {
        const apiStub = await api;

        let keyModel = {
          number: this.number,
          lock_id: this.selectedLock.id,
          safe_id: this.selectedSafe.id,
          rentable: this.rentable,
          note: this.note
        }
        
        if(this.keyId) {
          const param = { uuid: this.keyId };

          apiStub.key_editKey(param, keyModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.key_createKey(null, keyModel).then((response) => {
            this.$refs.form.reset();
            this.keyId = response.data.id;
            this.$emit('save-form');
          });
        }
      }
    },
    async loadData() {
      const apiStub = await api;
      apiStub.lock_getLocks().then(response => {
        this.locks = response.data;
      }).then(apiStub.safe_getSafes
      ).then(response => {
        this.safes = response.data;
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