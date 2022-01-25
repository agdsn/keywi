<template>
    <v-form ref="form">
      <v-text-field v-model="grantingDocument" label="Dokument" prepend-icon="mdi-file-document"/>
      <v-textarea v-model="note" label="Notiz" prepend-icon="mdi-note-text-outline" rows="1"></v-textarea>
      <v-checkbox v-model="editStartDate" label="Startdatum bearbeiten"/>

      <v-menu
        v-model="menuStartDate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
              :disabled="!editStartDate"
              style="margin-top:-10px"
            v-model="dateStart"
            label="Startdatum"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateStart"
          @input="menuStartDate = false"
        ></v-date-picker>
      </v-menu>

      <v-checkbox v-model="editEndDate" label="Enddatum bearbeiten"/>
      <v-menu
        v-model="menuEndDate"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="auto"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
              :disabled="!editEndDate"
              style="margin-top:-10px"
            v-model="dateEnd"
            label="Enddatum"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker
          v-model="dateEnd"
          @input="menuEndDate = false"
        ></v-date-picker>
      </v-menu>

      <v-btn color="validate" @click="save">
        <v-icon left size="24">mdi-content-save-outline</v-icon>
        Speichern
      </v-btn>
   </v-form>
</template>

<script>
import api from "@/api/api"

export default {
  name: "EditRentalForm",
  data() {
    return {
      rentalId: undefined,
      grantingDocument: '',
      note: '',
      menuStartDate: false,
      editStartDate: false,
      dateStart: undefined,
      menuEndDate: false,
      editEndDate: false,
      dateEnd: undefined
    }
  },
  mounted() {
    this.$emit('mounted');
  },
  methods: {
    fillForm(rentalTemplate) {
      if(rentalTemplate){
        this.rentalId = rentalTemplate.id;
        this.grantingDocument = rentalTemplate.allowed_by;
        this.note = rentalTemplate.note;
        if(rentalTemplate.begin) this.dateStart = this.datetimeToDate(rentalTemplate.begin);
        if(rentalTemplate.end) this.dateEnd = this.datetimeToDate(rentalTemplate.end);
      } else {
        this.rentalId = undefined;
        this.grantingDocument = '';
        this.note = '';
      }

      this.$refs.form.resetValidation();
    },

    dateToDatetime(date) {
      return date + 'T12:00';
    },

    datetimeToDate(datetime) {
      return datetime.substring(0, datetime.indexOf('T'));
    },
    
    async save() {
        const apiStub = await api;

        let rentalModel = {
          allowed_by: this.grantingDocument,
          note: this.note
        }
        
        if(this.editStartDate && this.dateStart) rentalModel.begin = this.dateToDatetime(this.dateStart);
        if(this.editEndDate && this.dateEnd) rentalModel.end = this.dateToDatetime(this.dateEnd);
        
        if(this.rentalId) {
          const param = { uuid: this.rentalId };

          apiStub.rental_editRental(param, rentalModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        } else {
          apiStub.rental_createRental(null, rentalModel).then(() => {
            this.$refs.form.reset();
            this.$emit('save-form');
          });
        }
      }
  }
}
</script>

<style scoped>
  .v-btn {
    background-color: var(--primary-color) !important;
    color: white;
    position: absolute;
    right: 0;
  }

  .v-form {
    position: relative;
  }
</style>