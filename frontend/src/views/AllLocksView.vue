<template>
  <div class="home">
    <app-title view-title="Schlösser"></app-title>
    <app-nav-bar></app-nav-bar>
    <lock-table ref="lockTable" @editItem="editLock" class="mx-7 mt-7"/>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Schloss hinzufügen"
                form="edit-lock-form"
                @save-form="$refs.lockTable.loadData();"
                ref="popup"
                @mounted="mountedEvent"
                @button-add-clicked="buttonAddClicked"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import LockTable from "@/components/LockTable.vue";
import FormPopup from "@/components/FormPopup.vue";
import EditLockForm from "@/components/EditLockForm.vue";

export default Vue.extend({
    name: 'AllLocksView',

    components: {
      AppNavBar,
      AppTitle,
      LockTable,
      FormPopup
    },
    data() {
      return {
        editedLock: undefined
      }
    },
    methods: {
        editLock(editedLock : any) {
          this.editedLock = editedLock;

          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.openDialog();
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            this.$refs.popup.$refs.form.fillForm(this.editedLock);
          }
        },
  
      mountedEvent() {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.$refs.form.fillForm(this.editedLock);
      },
  
      buttonAddClicked() {
          this.editedLock = undefined;
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedLock);
      }
    }
  })


</script>

<style scoped>

</style>
