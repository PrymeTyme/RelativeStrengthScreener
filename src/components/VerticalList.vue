<template>
    <div class="item">
      <div class="id">{{ source.id }} - {{ source.text }}</div>
    </div>
  </template>
  
  <script>
  export default {
    name: "itemList",
    props: {
      source: {
        type: Object,
        default() {
          return {};
        },
      },
    },
  };
  </script>
  
  <style scoped>
  .item {
    display: flex;
    flex-direction: column;
    border-bottom: 2px solid rgb(4, 4, 4);
    padding: 1em;
  }
  </style>