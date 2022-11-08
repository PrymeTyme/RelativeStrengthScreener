<template>
  <div class="outerLayout">
    <NavHead />
    <div>{{ this.timeframe }}</div>
    <LineChart />
    <div class="vertL">
      <div v-if="items.length">
        <div class="listHead">
          <div>Ticker </div>
          <div>Price </div>
          <div>Change%</div>
        </div>
        <div class="listItem" v-for="item, index in items" :key="item" @click="getTicker(index)">{{ item.ticker }}
          <div id="price"> {{ item.price }}</div>
          <div class="change" :style="{ 'color': item.changeColor }"> {{ item.change }}</div>
          <card></card>
        </div>
      </div>
    </div>
  </div>
</template>

 
<script>
import NavHead from "./NavHead.vue"
import LineChart from "./LineChartTest.vue";
import itemList from "./Item.vue";

import Card from "./Card.vue"

import { getData } from "../getData.js";
import { useTickerStore } from "../stores/tickers.js"
import { useTimeframeStore } from "../stores/timeframes.js";
//import { computed } from "@vue/reactivity";
import { mapState } from 'pinia'

//import { ref } from "vue";
import { storeToRefs } from 'pinia';
//import {getTicker} from "../geTicker.js";
//import { response } from "express";
//import { init } from "events";
//import { nextTick } from 'vue';
//import VirtualList from "vue-virtual-scroll-list";

//const timeframeStore = useTimeframeStore();
//const {timeframe} = storeToRefs(timeframeStore);

//let default_timeframe = 'daily'
let default_ticker = 'sector'




export default {
  name: "HelloWorld",
  data() {
    return {
      item: itemList,
      items: [],
      colorList: [],
      dropdownlist:[
        {title:'add to watchlist'},
        {title: 'show stocks'}
      ]
    }
  },

  computed: {

    ...mapState(useTimeframeStore, ['timeframe']) // to use this.timeframe in component

  },

  setup() {
    /*    const tickerStore =useTickerStore();
       return{tickerStore} */

    const tickerStore = useTickerStore();
    const { ticker } = storeToRefs(tickerStore)
    const { getTicker } = tickerStore

    const timeframeStore = useTimeframeStore();
    const { timeframe } = storeToRefs(timeframeStore)
    const { getTimeframe } = timeframeStore

    return { tickerStore, ticker, getTicker, timeframeStore, timeframe, getTimeframe }

  },



  methods: {

    changeColor() {
      var element = document.querySelectorAll('.change');
      const colorList = [];

      for (let i = 0; i < element.length; i++) {
        var color = (element[i].innerHTML) > 0 ? "color: green" : "color: red";
        colorList.push(color)

        console.log(color);
        console.log("worked");
        // console.log(element);
        //console.log(element.length);
        console.log(element[i].innerHTML);


      }
      return this.colorList = colorList
    },

    /*     getTicker(index) {
          var element = document.getElementsByClassName('listItem');
          var ticker = element[index].firstChild.data;
          console.log(ticker);
          console.log(element)
    
          return this.ticker = ticker
        },
     */



  },

  async created() {
    getData(default_ticker, this.timeframe).then(response => {
      console.log(response);
      this.items = response;
    })

  },

  watch: {
    timeframe: async function () {
      if (this.timeframe) {
        this.items = await getData(default_ticker, this.timeframe);
      }
    }
  },

  updated() { // runs after watch

    // getData(default_ticker,this.timeframe).then(response => {
    //   console.log(response);
    //   this.items = response;
    // })
    /*     document.onreadystatechange = () => {
          if (document.readyState == "complete") {
            this.changeColor();
            console.log(document.readyState)
          }
        },
    
          document.addEventListener('DOMContentLoaded', function () { nextTick().then(() => { console.log(document.getElementsByClassName('change')) }) });
        this.$nextTick().then(() => { console.log(document.querySelectorAll('.change')) }), */

    //this.changeColor();
    //console.log('watched '+this.timeframe)
    //console.log(this.items[0])

  },

  components: {
    LineChart,
    NavHead,
    Card,
    
  },
  props: {
    msg: String,
  },



};
</script>


<style scoped>
.vertL {
  overflow-y: scroll;
  float: right;
  border-radius: 10px;
  border: solid 2px #41729F;
  grid-column-start: 2;
  grid-row-start: 2;
  height: calc(100vh - 40px);

}

.outerLayout {
  display: grid;
  grid-template-rows: 10% auto;
  grid-template-columns: 80% auto;
  overflow: auto;
  border: 5px solid #41729F;
  border-radius: 5px;
  padding: 0;
  margin: 5%;
  margin-top: 0px;
  background-color: #41729F;
  ;
}

.listItem {
  display: grid;
  grid-template-columns: 30% 30% 30% auto;
  border-bottom: solid 2px #41729F;
  padding: 1em;
  cursor: pointer;
  position: relative;
  border-radius: 5px;
  background: #5885AF;
  transition: 0.4s;
  justify-content: center;

}


.listItem:hover {
  background-color: #41729F;
  color: #C3E0E5;
  transition: 0.4s;

}

.listItem:active {
  color: #C3E0E5;
  background-color: #41729f4b;
  transform: translateY(4px);
}


.listHead {
  display: grid;
  grid-template-columns: 25% 30% 35%;
  border-bottom: solid 2px #41729F;
  padding: 1em;
  cursor: pointer;
  position: sticky;
  top: 0;
  z-index: 5;
  background: #5885AF;
  border-radius: 5px;

}

.listItem>.icon {
  color: black !important;
  transition: 0.4s;
  border-left:  2px solid #41729F;
  background: #5885AF;
  justify-content: center;
  top: 0;
  width: 8%;
  height: 100%;
  position: absolute;
  margin-left: 290px;


}


.listItem>.icon:hover {
  background-color: #5885AF !important;
  color: #C3E0E5 !important;
  transition: 0.4s;
  
}



@media only screen and (max-width:600px) {
  .outerLayout {
    display: inline-block;
  }
}
</style>