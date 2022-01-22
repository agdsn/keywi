<template>
  <div class="home">
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

<script>
import Vue from 'vue'
import LockTable from "@/components/LockTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllLocksView',

    components: {
      LockTable,
      FormPopup
    },
    data() {
      return {
        editedLock: undefined
      }
    },
    methods: {
        editLock(editedLock) {
          this.editedLock = editedLock;

          this.$refs.popup.openDialog();

          if(this.$refs.popup.$refs.form) {
            this.$refs.popup.$refs.form.fillForm(this.editedLock);
          }
        },
  
      mountedEvent() {
          this.$refs.popup.$refs.form.fillForm(this.editedLock);
      },
  
      buttonAddClicked() {
          this.editedLock = undefined;

          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedLock);
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
