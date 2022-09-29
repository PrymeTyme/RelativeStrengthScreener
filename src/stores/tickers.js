import { defineStore } from "pinia";

export const useTickerStore = defineStore({
    id:'tickers',
    state:()=>({
        ticker:""

    }),

    actions:{
        getTicker(index) {
            var element = document.getElementsByClassName('listItem');
            var ticker = element[index].firstChild.data;
            console.log(ticker)
            this.ticker = ticker;
    }}
})