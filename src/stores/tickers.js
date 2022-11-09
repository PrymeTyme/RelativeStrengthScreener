import { defineStore } from "pinia";
//import { reactive } from "vue";
import { ref } from "vue";


/* export const useTickerStore = defineStore(
    'ticker', () =>{
        var ticker = ref("");

        const getTicker = (index) =>{
            var element = document.getElementsByClassName('listItem');
            var tickerZ = element[index].firstChild.data;
            console.log(tickerZ);  
            ticker = tickerZ  
            

        }

        return {ticker,getTicker};
    }
) */

const check_sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY'];

 export const useTickerStore = defineStore({
    id: 'tickers',
    state: () => ({
        ticker: ref("sector"),
        index: ref('')


    }),

    actions: {
        getTicker(index) {
            var element = document.getElementsByClassName('listItem');
            var ticker = element[index].firstChild.data;
            ticker = ticker.trim();
            if(check_sectors.includes(ticker)){
                return this.index = ticker, this.ticker = ticker;
            }
            console.log(ticker);
            console.log(typeof ticker);
            return this.ticker = ticker;
        }
    }
}) 