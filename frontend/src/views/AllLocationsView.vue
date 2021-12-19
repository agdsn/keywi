<template>
  <div class="home pb-5">
    <app-title view-title="Orte"></app-title>
    <app-nav-bar></app-nav-bar>
    <location-table class="mx-7 mt-7" ref="locationTable" @editItem="editLocation"/>
    <v-divider class="mx-8"></v-divider>
    <form-popup text="Ort hinzufügen"
                form="edit-location-form"
                @save-form="$refs.locationTable.loadData();"
                ref="popup"
                @mounted="mountedEvent"
                @button-add-clicked="buttonAddClicked"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import AppTitle from "@/components/AppTitle.vue";
import AppNavBar from "@/components/AppNavBar.vue";
import LocationTable from "@/components/LocationTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllLocationsView',

    components: {
      FormPopup,
      AppNavBar,
      AppTitle,
      LocationTable
    },
  data() {
      return {
        editedLocation: undefined
      }
    },
    methods: {
        editLocation(editedLocation : any) {
          this.editedLocation = editedLocation;
          
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.openDialog();
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) {
            // eslint-disable-next-line @typescript-eslint/ban-ts-comment
            // @ts-ignore
            this.$refs.popup.$refs.form.fillForm(this.editedLocation);
          }
        },
  
      mountedEvent() {
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          this.$refs.popup.$refs.form.fillForm(this.editedLocation);
      },
  
      buttonAddClicked() {
          this.editedLocation = undefined;
  
          // eslint-disable-next-line @typescript-eslint/ban-ts-comment
          // @ts-ignore
          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedLocation);
      }
    }
  })

</script>

<style scoped>

</style>
