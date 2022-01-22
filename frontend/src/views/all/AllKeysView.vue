<template>
  <div class="home">
    <key-table ref="keyTable" @editItem="editKey" class="mx-7 mt-7"/>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Schlüssel hinzufügen"
                form="edit-key-form"
                @save-form="$refs.keyTable.loadData();"
                ref="popup"
                @mounted="mountedEvent"
                @button-add-clicked="buttonAddClicked"/>
  </div>
</template>

<script>
import Vue from 'vue'
import KeyTable from "@/components/KeyTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllKeysView',

    components: {
      KeyTable,
      FormPopup
    },
  data() {
      return {
        editedKey: undefined
      }
    },
    methods: {
        editKey(editedKey) {
          this.editedKey = editedKey;

          this.$refs.popup.openDialog();

          if(this.$refs.popup.$refs.form) {
            this.$refs.popup.$refs.form.fillForm(this.editedKey);
          }
        },
  
      mountedEvent() {
          this.$refs.popup.$refs.form.fillForm(this.editedKey);
      },
  
      buttonAddClicked() {
          this.editedKey = undefined;

          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedKey);
      }
    }
  })


</script>

<style scoped>
  .home {
    position: relative;
  }

  .home >>> .v-btn.secondary {
    position: absolute;
    right: 0;
  }
</style>
