<template>
  <div class="outerLayout">
    <LineChart />
    <div class="vertL">
      <div v-if="items.length">
        <div class="listHead">
          <div>Ticker </div>
          <div>Price </div>
          <div>Change%</div>
        </div>
        <div class="listItem" v-for="item , index in items" :key="item" @click="getTicker(index)">{{item.ticker}}
          <div id="price"> {{item.price}}</div>
          <div class="change" :style="{'color':item.changeColor}"> {{item.change}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

 
<script>
import LineChart from "./LineChartTest.vue";
import itemList from "./Item.vue";
import { getData } from "../getData.js";
import { useTickerStore } from "../stores/tickers.js"
//import { computed } from "@vue/reactivity";
//import { ref } from "vue";
import { storeToRefs } from 'pinia'
//import {getTicker} from "../geTicker.js";
//import { response } from "express";
//import { init } from "events";
//import { nextTick } from 'vue';
//import VirtualList from "vue-virtual-scroll-list";



export default {
  name: "HelloWorld",
  data() {
    return {
      item: itemList,
      items: [],
      colorList: [],
    }
  },

  setup() {
    /*    const tickerStore =useTickerStore();
       return{tickerStore} */

    const tickerStore = useTickerStore();
    const { ticker } = storeToRefs(tickerStore)
    const { getTicker } = tickerStore
    return { tickerStore, ticker, getTicker }

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
    getData().then(response => {
      console.log(response);
      this.items = response;
    })

  },

  updated() {
    /*     document.onreadystatechange = () => {
          if (document.readyState == "complete") {
            this.changeColor();
            console.log(document.readyState)
          }
        },
    
          document.addEventListener('DOMContentLoaded', function () { nextTick().then(() => { console.log(document.getElementsByClassName('change')) }) });
        this.$nextTick().then(() => { console.log(document.querySelectorAll('.change')) }), */

    this.changeColor();


  },

  components: {
    LineChart,
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
  background: #5885AF;
  border-radius: 10px;
  border: solid 2px #41729F;
  height: 888px;
}

.outerLayout {
  display: grid;
  grid-template-columns: 80% auto;
  overflow: auto;
  border: 5px solid #41729F;
  border-radius: 5px;
  padding: 0;
  margin: 5%;
  margin-top: 5px;
  background-color: #41729F;
  ;
}

.listItem {
  display: grid;
  grid-template-columns: 33% 33% 33%;
  border-bottom: solid 2px #41729F;
  padding: 1em;
  cursor: pointer;
  position: relative;

}


.listItem:hover {
  background-color: #41729F;
  color: #C3E0E5;
}

.listItem:active {
  color: #41729fd0;
  background-color: #41729f4b;
  transform: translateY(4px);
}

.listHead {
  display: grid;
  grid-template-columns: 33% 33% 33%;
  border-bottom: solid 2px #41729F;
  padding: 1em;
  cursor: pointer;
  position: sticky;
  top: 0;
  z-index: 5;
  background: #5885AF;

}



@media only screen and (max-width:600px) {
  .outerLayout {
    display: inline-block;
  }
}
</style>