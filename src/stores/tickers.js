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

 export const useTickerStore = defineStore({
    id: 'tickers',
    state: () => ({
        ticker: ref("sector")


    }),

    actions: {
        getTicker(index) {
            var element = document.getElementsByClassName('listItem');
            var ticker = element[index].firstChild.data;
            ticker.trim();
            console.log(ticker);
            console.log(typeof ticker);
            return this.ticker = ticker;
        }
    }
}) 