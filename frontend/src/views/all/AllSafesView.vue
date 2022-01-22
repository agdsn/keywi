<template>
  <div class="home">
    <safe-table ref="safeTable" @editItem="editSafe" class="mx-7 mt-7"/>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Tresor hinzufügen"
                ref="popup"
                form="edit-safe-form"
                @save-form="$refs.safeTable.loadData();"
                @mounted="mountedEvent"
                @button-add-clicked="buttonAddClicked"/>
  </div>
</template>

<script>
import Vue from 'vue'
import SafeTable from "@/components/SafeTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllSafesView',

    components: {
      SafeTable,
      FormPopup
    },
    data() {
      return {
        editedSafe: undefined
      }
    },

  methods: {
    editSafe(editedSafe) {
      this.editedSafe = editedSafe;

      this.$refs.popup.openDialog();

      if(this.$refs.popup.$refs.form) {
        this.$refs.popup.$refs.form.fillForm(this.editedSafe);
      }
    },

    mountedEvent() {
        this.$refs.popup.$refs.form.fillForm(this.editedSafe);
    },

    buttonAddClicked() {
        this.editedSafe = undefined;

        if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedSafe);
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
