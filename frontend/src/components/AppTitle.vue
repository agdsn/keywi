<template>
  <div>
    <h1>
      {{ viewTitle }}
    </h1>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'

  export default Vue.extend ({
  name: "AppTitle",
  props: ['viewTitle']
});
</script>

<style scoped>
  div {
    background-color: #0D2221;
    display: flex;
    width: 100%;
    padding: 10px 0;
    color: #ffffff;
    justify-content: center;
  }

  div h1 {
    background-color: #0D2221;
    font-weight: normal;
  }
</style>