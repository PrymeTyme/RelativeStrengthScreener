import { defineStore } from 'pinia'
import {useStorage} from '@vueuse/core'

export const useWatchListStore = defineStore('watchList', {

  state:()=>({
    watchList: useStorage('watchList',[]),
    id:0,
  }),

  actions:{

    addToList(ticker){
        this.watchList.push({ticker, id:this.id++})
    },

    deleteItem(tickerID) {
        this.watchList = this.watchList.filter((object) => {
          return object.id !== tickerID;})},
  

}})