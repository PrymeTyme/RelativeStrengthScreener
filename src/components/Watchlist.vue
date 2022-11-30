<template>
    <div class="watchlistBox">My Watchlist
      <WatchlistItem/>
    </div>
  </template>
  
  <script>
import WatchlistItem from './WatchlistItem.vue';

  export default {
    name: "WatchList",
    components:{ WatchlistItem}
  };
  </script>
  
  <style scoped>

  .watchlistBox{
    position: relative;
    width: 200px;
    padding: 20px;
    border-radius: 20px;
    border: solid 5px #131722;
    background: #2A2E39;
    color: #C3E0E5;
    height: 500px;
    overflow-y: scroll;

  }

  </style>