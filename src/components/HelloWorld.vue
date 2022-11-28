<template>
  <div class="outerLayout">
    <NavHead />
    <div class="infoBox" style="color:#C3E0E5">
      <div  :class="{'infoText':showHoldings,'infoTextBtn':!showHoldings}">Timeframe:{{ capitalizeFirstLetter(this.timeframe) }}<br>Sector:{{ this.index }}<br>Ticker:{{ this.ticker }}</div> <button class="btn"
        v-if="showHoldings == true" @click="getBack()"> <!--make the info box a vue component -->
        <fa icon="angle-double-left" /> <span class="tooltip">back to sector overview</span>
      </button>
    </div>
    <Carousel  />
    <LineChart />
    <div style="color:#C3E0E5 ;grid-row-start:4">last update: xx.xx.xx</div>
    <div class="vertL">
      <div v-if="items.length">
        <div class="listHead">
          <div>Ticker </div>
          <div>Price </div>
          <div>Change%</div>
        </div>
        <div class="listItem" v-for="item, index in items" :key="item" @click="getTicker(index)">{{ item.ticker }} <div
            class="infoName">{{ item.name }}</div>
          <div id="price"> {{ item.price }}</div>
          <div class="change" :style="{ 'color': item.changeColor }"> {{ item.change }}%</div>
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
import Carousel from "./Carousel.vue";

import { getData } from "../getData.js";
import { useTickerStore } from "../stores/tickers.js"
import { useTimeframeStore } from "../stores/timeframes.js";
import { useOptionStore } from "../stores/options.js";
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
//let default_ticker = 'sector'

const check_sectors = ['XLE', 'XLU', 'XLK', 'XLB', 'XLP', 'XLY', 'XLI', 'XLC', 'XLV', 'XLF', 'XLRE', 'SPY'];



export default {
  name: "HelloWorld",
  data() {
    return {
      item: itemList,
      items: [],
      colorList: [],
      dropdownlist: [
        { title: 'add to watchlist' },
        { title: 'show stocks' }
      ],
      showHoldings: false,

    }
  },

  computed: {

    ...mapState(useTimeframeStore, ['timeframe']),
    ...mapState(useOptionStore, ['option']), // to use this.xxx 
    ...mapState(useTickerStore, ['ticker']),
    ...mapState(useTickerStore, ['index']),

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

    const optionStore = useOptionStore();
    const { option } = storeToRefs(optionStore)
    const { getOption } = optionStore


    return { tickerStore, ticker, getTicker, timeframeStore, timeframe, getTimeframe, optionStore, option, getOption }

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

    async getBack() {
      this.items = await getData('sector', this.timeframe)
      //this.timeframe = this.timeframe;
      this.showHoldings = false;


    },

    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }

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
    getData(this.ticker, this.timeframe).then(response => {
      console.log(response);
      this.items = response;
    })

  },

  watch: {
    timeframe: async function () {
      if (this.timeframe && this.ticker == 'sector') {
        this.items = await getData(this.ticker.toLowerCase().trim(), this.timeframe); // changes to ticker vs index ???
      }
      else if (this.timeframe && check_sectors.includes(this.ticker)) {
        this.items = await getData('sector', this.timeframe); // changes to ticker vs index ???
      }
      else if (this.timeframe) {
        this.items = await getData(this.index.toLowerCase().trim(), this.timeframe); // changes to ticker vs index ??? something logical!


      }
    },
    option: async function () {
      if (this.option == 'show') {
        this.items = await getData(this.index.toLowerCase().trim(), this.timeframe)
        this.option = ''
        this.showHoldings = true
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
    Carousel,

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
  border: solid 2px #2A2E39;
  grid-column-start: 2;
  grid-row-start: 2;
  height: calc(100vh - 150px);
  margin-top: 1px;

}

.outerLayout {
  display: grid;
  grid-template-rows: 10% 100px auto 5%;
  grid-template-columns: 80% auto;
  overflow: auto;
  border: 5px solid #2A2E39;
  border-radius: 5px;
  padding: 0;
  margin: 5%;
  margin-top: 0px;
  background-color: #2A2E39;
}

.listItem {
  display: grid;
  grid-template-rows: 60% auto;
  grid-template-columns: 30% 30% 30% auto;
  border-bottom: solid 2px #2A2E39;
  padding: 1em;
  cursor: pointer;
  position: relative;
  border-radius: 5px;
  background: #131722;
  transition: 0.4s;
  justify-content: center;
  color: #C3E0E5;

}


.listItem:hover {
  background-color: #2A2E39;
  color: #C3E0E5;
  transition: 0.4s;

}

.listItem:active {
  color: #C3E0E5;
  
}


.listHead {
  display: grid;
  grid-template-columns: 25% 30% 35%;
  border-bottom: solid 2px #2A2E39;
  padding: 1em;
  cursor: pointer;
  position: sticky;
  top: 0;
  z-index: 5;
  background: #131722;
  border-radius: 5px;
  color: #C3E0E5;
  font-weight: 700;

}

.listItem>.icon {
  color: black !important;
  transition: 0.4s;
  border-left: 2px solid #2A2E39;
  background: #131722;
  justify-content: center;
  top: 0;
  width: 8%;
  height: 100%;
  position: absolute;
  margin-left: 290px;


}


.listItem>.icon:hover {
  background-color: #131722 !important;
  color: #C3E0E5 !important;
  transition: 0.4s;

}

.infoBox {
  display: grid;
  grid-template-columns: 60% auto;
  border: solid 3px #2A2E39;
}

.infoText {
  background: #131722;
  border-radius: 5px;
  border: none;
  color: #C3E0E5;
  padding: 15px 40px;
  font-size: 16px;
  margin-right: 6px;
  text-align: left;
  

}

.infoTextBtn{
  background: #131722;
  border-radius: 5px;
  border: none;
  color: #C3E0E5;
  padding: 15px 40px;
  font-size: 16px;
  margin-right: 6px;
  width:240px;
  text-align: left;

}

.btn {
  background: #131722;
  border-radius: 5px;
  border: none;
  color: #C3E0E5;
  padding: 25px 40px;
  font-size: 16px;
  cursor: pointer;
}

.btn:hover {
  color: #E3B844;
}

.btn .tooltip {
  visibility: hidden;
  text-align: center;
  color: #E3B844;
  background-color: #2A2E39;
  border-radius: 5px;
  border: #131722 solid 2px;
  position: absolute;
  top: 368px;
  left: 87.3%;
  z-index: 8;
}

.btn:hover .tooltip {
  visibility: visible;
}

.infoName {
  grid-row-start: 2;
  font-size: smaller;
  width: 310px;
  text-align: left;
  margin-top: 5px;

}




@media only screen and (max-width:600px) {
  .outerLayout {
    display: inline-block;
  }
}
</style>