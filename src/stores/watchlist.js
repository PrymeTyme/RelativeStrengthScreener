import { defineStore } from 'pinia'
import {useStorage} from '@vueuse/core'

export const useWatchListStore = defineStore('watchList', {

  state:()=>({
    watchList: useStorage('watchList',[]),
    id:0,
  }),

  actions:{

    addToList(ticker,price){
        this.watchList.push({ticker,price:price, id:this.id++})
    },

    deleteItem(tickerID) {
        this.watchList = this.watchList.filter((object) => {
          return object.id !== tickerID;})},
  

}})