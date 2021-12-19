<template>
  <div class="home">
    <app-title view-title="Tresor"></app-title>
    <app-nav-bar></app-nav-bar>
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

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import SafeTable from "@/components/SafeTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllSafesView',

    components: {
      SafeTable,
      AppNavBar,
      AppTitle,
      FormPopup
    },
    data() {
      return {
        editedSafe: undefined
      }
    },

  methods: {
      editSafe(editedSafe : any) {
        this.editedSafe = editedSafe;

        // Sind schlecht konfigurierte linter nicht eine tolle Erfindung
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        this.$refs.popup.openDialog();

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        if(this.$refs.popup.$refs.form) {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.$refs.form.fillForm(this.editedSafe);
        }
      },

    mountedEvent() {
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        this.$refs.popup.$refs.form.fillForm(this.editedSafe);
    },

    buttonAddClicked() {
        this.editedSafe = undefined;

        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedSafe);
    }
  }
  })

</script>

<style scoped>
</style>
