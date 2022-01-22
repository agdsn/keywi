<template>
  <div class="home pb-5">
    <location-table class="mx-7 mt-7" ref="locationTable" @editItem="editLocation"/>
    <form-popup text="Ort hinzufügen"
                form="edit-location-form"
                @save-form="$refs.locationTable.loadData();"
                ref="popup"
                @mounted="mountedEvent"
                @button-add-clicked="buttonAddClicked"
                icon="mdi-plus"/>
  </div>
</template>

<script>
import Vue from 'vue'
import LocationTable from "@/components/LocationTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllLocationsView',

    components: {
      FormPopup,
      LocationTable
    },
  data() {
      return {
        editedLocation: undefined
      }
    },
    methods: {
        editLocation(editedLocation) {
          this.editedLocation = editedLocation;

          this.$refs.popup.openDialog();

          if(this.$refs.popup.$refs.form) {
            this.$refs.popup.$refs.form.fillForm(this.editedLocation);
          }
        },
  
      mountedEvent() {
          this.$refs.popup.$refs.form.fillForm(this.editedLocation);
      },
  
      buttonAddClicked() {
          this.editedLocation = undefined;

          if(this.$refs.popup.$refs.form) this.$refs.popup.$refs.form.fillForm(this.editedLocation);
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
