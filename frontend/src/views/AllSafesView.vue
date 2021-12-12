<template>
  <div class="home">
    <app-title view-title="Tresor"></app-title>
    <app-nav-bar></app-nav-bar>
    <safe-table @editItem="editSafe"></safe-table>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Tresor hinzufügen" ref="popup">
      <edit-safe-form class="mx-8 my-4 " :safe-template="safe" ref="form"></edit-safe-form>
    </form-popup>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import SafeTable from "@/components/SafeTable.vue";
import FormPopup from "@/components/FormPopup.vue";
import EditSafeForm from "@/components/EditSafeForm.vue";

export default Vue.extend({
    name: 'AllSafesView',

    components: {
      SafeTable,
      AppNavBar,
      AppTitle,
      FormPopup,
      EditSafeForm
    },
    data() {
      return {
        safe: undefined
      }
    },

  methods: {
      editSafe(safe : any) {
        this.safe = safe;

        // TODO: Suche schönere Möglichkeit, Methoden von Kindern
        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
        // @ts-ignore
        this.$refs.popup.openDialog();

        if(this.$refs.form) {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.form.updateSafeTemplate(safe);
        }
      }
  }
  })


</script>

<style scoped>
  .v-data-table {
    margin: 30px 30px 0 30px;
  }
</style>
