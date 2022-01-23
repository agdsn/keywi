<template>
  <div class="home pb-5">
    <rental-table class="mx-7 mt-7" ref="rentalTable" @editItem="editRental"/>
    <form-popup text="Ausleihe bearbeiten"
                form="edit-rental-form"
                @save-form="$refs.rentalTable.loadData();"
                ref="popup"
                @mounted="mountedEvent"
                hide-btn/>
  </div>
</template>

<script>
import Vue from 'vue'
import RentalTable from "@/components/RentalTable.vue";
import FormPopup from "@/components/FormPopup.vue";

export default Vue.extend({
    name: 'AllRentalsView',

    components: {
      FormPopup,
      RentalTable
    },
  data() {
      return {
        editedRental: undefined
      }
    },
    methods: {
        editRental(editedRental) {
          this.editedRental = editedRental;

          this.$refs.popup.openDialog();

          if(this.$refs.popup.$refs.form) {
            this.$refs.popup.$refs.form.fillForm(this.editedRental);
          }
        },
  
      mountedEvent() {
          this.$refs.popup.$refs.form.fillForm(this.editedRental);
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
