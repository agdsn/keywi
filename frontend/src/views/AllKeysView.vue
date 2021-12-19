<template>
  <div class="home">
    <app-title view-title="Schlüssel"></app-title>
    <app-nav-bar></app-nav-bar>
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

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import KeyTable from "@/components/KeyTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllKeysView',

    components: {
      KeyTable,
      AppNavBar,
      AppTitle,
      FormPopup
    },
  data() {
      return {
        editedKey: undefined
      }
    },
    methods: {
        editKey(editedKey : any) {
          this.editedKey = editedKey;
          
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.openDialog();
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            this.$refs.popup.$refs.form.fillForm(this.editedKey);
          }
        },
  
      mountedEvent() {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.$refs.form.fillForm(this.editedKey);
      },
  
      buttonAddClicked() {
          this.editedKey = undefined;
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedKey);
      }
    }
  })


</script>

<style scoped>

</style>
