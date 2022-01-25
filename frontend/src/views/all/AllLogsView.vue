<template>
  <div class="home pb-5">
    <detail-table-logs class="mx-7 mt-7" ref="logTable"/>
  </div>
</template>

<script>
import Vue from 'vue'
import RentalTable from "@/components/RentalTable.vue";
import FormPopup from "@/components/FormPopup.vue";
import DetailTableLogs from "@/components/detail/DetailTableLogs";

export default Vue.extend({
  name: 'AllLogsView',

  components: {
    DetailTableLogs,
  },
  data() {
    return {};
  },
  mounted() {
    this.$refs.logTable.loadData({ });
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
