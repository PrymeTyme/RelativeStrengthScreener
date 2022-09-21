<template>
  <div class="outerLayout">
    <LineChart />
    <div class="vertL">
      <div v-if="items">
        <div class="listItem" v-for="item in items" :key="item">{{item.ticker}} : {{item.price}} 
        <div> Chg%: {{item.change}}%</div>
      </div>
      </div>
    </div>
  </div>
</template>

 
<script>
import LineChart from "./LineChartTest.vue";
import itemList from "./Item.vue";
import { getData } from "../getData.js"
//import VirtualList from "vue-virtual-scroll-list";

export default {
  name: "HelloWorld",
  data() {
    return {
      item: itemList,
      items: [],
    }
  },
  created() {
    getData().then(response => {
      console.log(response);
      this.items = response;
    })
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

.listItem{
  border-bottom: solid 2px #41729F;
  padding: 1em;
  display: flex;
  flex-direction: column;
  cursor: pointer;

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


@media only screen and (max-width:600px) {
  .outerLayout {
    display: inline-block;
  }
}
</style>