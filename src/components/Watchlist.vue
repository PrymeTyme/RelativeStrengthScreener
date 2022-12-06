<template>
    <div class="watchlistBox"> My Watchlist
      <div class="watchlistHead">
          <div>Ticker </div>
          <div>Price </div>
          <div class="chng" >%Chng since added </div>
        </div>
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
    height: 370px;
    overflow-y: scroll;

  }

  .watchlistHead{
    display: grid;
    grid-template-columns: 32% 32% 30%;
    border-bottom: solid 2px #2A2E39;
    padding: 1em;
    cursor: pointer;
    position: sticky;
    top: 0;
    z-index: 5;
    background: #2A2E39;
    border-radius: 5px;
    color: #C3E0E5;
    font-weight: 700;
    font-size: 16px;
    margin-left: -10px;
    font-size: small;
  }

  .chng{
    width: 100px;
    margin-left: -10px;
  }

  



  </style>