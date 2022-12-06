<template id="card">

<div v-if="addWatchlist" class="toast-container">
      <p class="toast" > {{this.ticker}} added to watchlist</p>
  </div>

    <div class="section">
        <div class="title" v-on:click="toggle">
            <fa icon="angle-down" class="arrow-down" v-show="!showSection" />
            <fa icon="angle-down" flip="vertical" class="arrow-down" v-show="showSection" />
        </div>

        <div class="body" v-show="showSection">
            <div id="options">
                <div class="option" v-for="item in items" :key="item" @click="getOption(item.id)">{{ item.text }}
                    <div class="icon">
                        <fa v-bind:icon="item.icon" />
                    </div>
                </div>
                <div></div>
            </div>
        </div>
    </div>

</template>


<script>

import { useOptionStore } from '../stores/options.js'
import { useWatchListStore } from '../stores/watchlist'
import { useTickerStore } from '../stores/tickers'

import { mapState } from 'pinia'
import { storeToRefs } from 'pinia'


export default {
    name: 'CardTest',
    template: '#card',
    methods: {
        toggle() {
            this.showSection = !this.showSection
        },

    },
    computed: {

        ...mapState(useOptionStore, ['option']), // to use this.xxx 
        ...mapState(useTickerStore, ['ticker']),
        ...mapState(useTickerStore, ['index']),

    },
    data() {
        return {
            addWatchlist: false,
            showSection: false,
            items: [{ text: 'Open in Chart', icon: 'line-chart', id: 'chart' }, { text: 'Show Sector Holdings', icon: 'list-dots', id: 'show' }, { text: 'Add to Watchlist', icon: 'add', id: 'add' }], // change to objects with value
        }
    },

    watch: {
        option: function () {
            if (this.option == 'add') {
                this.addWatchlist = !this.addWatchlist
                this.watchlistStore.addToList(this.ticker)
                this.option = ''
                
                
            }

        },

        addWatchlist(){
            if(this.addWatchlist)
            setTimeout(()=> this.addWatchlist = false,2500)
        }

    },

    setup() {


        const optionStore = useOptionStore();
        const { option } = storeToRefs(optionStore);
        const { getOption } = optionStore;

        const watchlistStore = useWatchListStore();
        const { tickerItem } = storeToRefs(watchlistStore);
        const { addToList } = watchlistStore;

        const tickerStore = useTickerStore();
        const { ticker } = storeToRefs(tickerStore)
        const { getTicker } = tickerStore

        return { optionStore, option, getOption, watchlistStore, tickerItem, addToList, ticker, getTicker }

    },
}
</script>

<style scoped>
.section {
    width: 50px;
    background: inherit;
    margin-bottom: 0px;
    transition: 0.4s;
}

#toggle {
    display: block;
}

.body {
    left: 50%;
    transform: translateX(-100%);
    width: 320px;
    border-top: 2px solid #2A2E39 transparent;
    margin-left: 120%;
}

.body:hover {
    border-top: 2px solid #131722 transparent;
}

.option {
    text-align: left;
    margin-top: 2%;
    display: grid;
    grid-template-columns: 60% auto;
}

.option:hover {
    width: 320px;
    margin-top: 2%;
    text-align: left;
    color: #E3B844;

}

.icon {
    margin-left: 69%;
}

.icon:hover {
    color: #E3B844;
}


.arrow-down:hover {
    color: #E3B844;
}


.toast-container{
  position: fixed;
  top: 1rem;
  right: 1.5rem;
  display: grid;
  justify-items: end;
  gap: 1.5rem;
  z-index: 10;

}

.toast{
  border-radius: 10px;
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 1;
  padding: 0.5em 1em;
  background-color: #E3B844;
  color: #0D2A38;
  animation: toastIt 3000ms cubic-bezier(0.785, 0.135, 0.15, 0.86) forwards;
 
}

@keyframes toastIt{
  0%,100%{
    transform:  translateY(-150%);
    opacity:0;
  }
  10%,90%{
    transform:  translateY(0%);
    opacity:1;

  }
}
</style>
  