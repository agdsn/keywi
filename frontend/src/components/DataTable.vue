<template>
  <v-data-table
    :items="realItems"
    :search="externalSearch ? null : searchModel"
    :loading="loading"
    loading-text="Lade Daten..."
    :items-per-page="15"
    class="elevation-1"
    :item-key="itemKey"
    :footer-props="footerProps"
    v-bind="$attrs" v-on="$listeners">
    <template v-slot:top>
      <v-row>
        <v-col align-self="start">
          <slot name="header">
          </slot>
        </v-col>
        <v-spacer v-if="!$slots.header && !$scopedSlots.header"/>
        <v-col lg="3" md="6" sm="12" v-if="showSearch || externalSearch" align-self="center">
          <v-text-field
            v-model="searchModel"
            label="Search"
            hide-details
            outlined
            dense
            class="mr-4 ml-4"
            @input="$emit('search', searchModel)"
          >
            <template v-slot:prepend-inner>
              <v-icon>
                mdi-magnify
              </v-icon>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </template>
    <template v-slot:[`footer.page-text`]>
      <v-row>
        <v-col align-self="center">
          <slot name="footer-right">
          </slot>
        </v-col>
      </v-row>
    </template>
    <template v-for="(_, slot) of inheritSlots" v-slot:[slot]="scope">
      <slot :name="slot" v-bind="scope" />
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: 'DataTable',
  data() {
    return {
      searchModel: null,
    };
  },
  props: {
    externalSearch: {
      type: Boolean,
      default: false,
    },
    items: Array,
    showSearch: {
      type: Boolean,
      default: true,
    },
    itemKey: {
      type: String,
      default: 'id',
    },
    footerProps: {
      type: Object,
      default() {
        return {
          'items-per-page-options': [5, 10, 15, 25, 50, 100, 250, 500],
        };
      },
    },
  },
  computed: {
    loading() {
      return this.items == null;
    },
    inheritSlots() {
      const slots = this.$scopedSlots;

      if ('header' in slots) {
        delete slots.header;
      }

      return slots;
    },
    realItems() {
      if (this.items) {
        return this.items;
      }

      return [];
    },
  },
  watch: {
    searchModel() {
      this.$emit('update:search', this.searchModel);
    },
  },
};
</script>
