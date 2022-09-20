<template>
  <div class="outerLayout">
    <LineChart />
    <div class="vertL">
      <div v-for="item in items" :key="item">{{item}}</div>
    </div>
  </div>
</template>

 
<script>
import LineChart from "./LineChartTest.vue";
import Item from "./Item.vue";
import {getData} from "../getData.js"

export default {
  name: "HelloWorld",
  data() {
    return {
      item:Item,
      items: getData(),
    }
  },
  components: {
    LineChart,
  },
  props: {
    msg: String,
  },

};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

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
  border: 5px solid #41729F;;
  border-radius: 5px;
  padding: 0;
  margin: 5%;
  margin-top: 5px;
  background-color: #41729F;; 
}

.mainCol {
  display: grid;
  grid-template-columns: 70% 30%;
  border: 1px solid steelblue;
  border-radius: 5px;
}

.chartCol {
  height: fit-content;
  display: grid;
  grid-template-columns: 50% 50%;
}

@media only screen and (max-width:600px) {
    .outerLayout {
      display: inline-block;
     }
}
</style>