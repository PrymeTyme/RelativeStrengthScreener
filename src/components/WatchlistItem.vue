<template>
    <div v-for="item in watchList" :key="item.id">
        <div class="items">
            <div>{{ item.ticker }}</div>
            <fa @click="deleteItem(item.id)" icon="subtract"> </fa>
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
    border-bottom: 2px solid #131722;;
    padding: 1em;
    justify-content: space-between;
    color: #C3E0E5;
}
</style>