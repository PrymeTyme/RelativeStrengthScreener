<template>
    <div v-for="item in watchList" :key="item.id">
        <div class="items">
            <div>{{ item.ticker }}</div>
            <div class="deleteItem" title="Delete" > <fa  @click="deleteItem(item.id)" icon="trash-can"> </fa> </div> 
        </div>
    </div>
</template>
  
<script>

import { useWatchListStore } from '../stores/watchlist'
import { storeToRefs } from 'pinia'

export default {
    name: "WatchListItem",

    setup() {

        const watchlistStore = useWatchListStore();
        const { watchList } = storeToRefs(watchlistStore);
        const { deleteItem } = watchlistStore

        return { watchList, deleteItem }

    },
};

</script>
  
<style scoped>
.items {
    display: flex;
    border-bottom: 2px solid #131722;
    padding: 1em;
    justify-content: space-between;
    color: #C3E0E5;
}

.items:hover{
    cursor: pointer;
}

.deleteItem{
    font-weight:500;
    font-size: 16px;
}

/*.deleteItem:hover:after{
  display: -webkit-flex;
  display: flex;
  -webkit-justify-content: center;
  justify-content: center;
  background: #131722;
  border-radius: 5px;
  color: #E3B844;
  content: attr(title);
  margin: -20px 70px 0px;
  font-size: 12px;
  padding: 13px;
  width: 50px;
  font-weight: lighter;
  margin-bottom: -5%;
}*/


.deleteItem:hover{
    color: #E3B844;
}


</style>