<template>
    <div class="chartCard">
        <fa @click="toggle" class="toggle" icon="chevron-right" v-show="!showWatchlist"/>
        <fa @click="toggle" class="toggle" icon="chevron-right" v-show="showWatchlist" flip="horizontal"/>
         <div :class="{'slide-in':showWatchlist,'slide-out':!showWatchlist}" v-if="showWatchlist"> <WatchList/> </div>
         <div :class="{'slide-in':showWatchlist,'slide-out':!showWatchlist}" v-else> <WatchList/> </div>
        <div :class="{'chartBox':!showWatchlist,'chartBoxToggle':showWatchlist}">
            <div>
                <button class="buttons" :class="{active:isActive==1}" @click="setDateRange1(243,350);isActive=1">1week</button>
                <button class="buttons" :class="{active:isActive==2}" @click="setDateRange1(236,350);isActive=2">14days</button>
                <button class="buttons" :class="{active:isActive==3}" @click="setDateRange1(220,350);isActive=3">1month</button>
                <button class="buttons" :class="{active:isActive==4}" @click="setDateRange1(190,350);isActive=4">2months</button>
                <button class="buttons" :class="{active:isActive==5}" @click="setDateRange1(160,350);isActive=5">3months</button>
                <button class="buttons" :class="{active:isActive==6}" @click="setDateRange1(70,350);isActive=6">6months</button>
                <button class="buttons" :class="{active:isActive==7}" @click="setDateRange1(0,350);isActive=7">1year</button>
            </div>
            <canvas id="myChart"></canvas> 
        </div>
        <div :class="{'chartBox':!showWatchlist,'chartBoxToggle':showWatchlist}">
            <div>
                <button class="buttons" :class="{active:isActive2==1}" @click="setDateRange(243,350);isActive2=1">1week</button>
                <button class="buttons" :class="{active:isActive2==2}" @click="setDateRange(236,350);isActive2=2">14days</button>
                <button class="buttons" :class="{active:isActive2==3}" @click="setDateRange(220,350);isActive2=3">1month</button>
                <button class="buttons" :class="{active:isActive2==4}" @click="setDateRange(190,350);isActive2=4">2months</button>
                <button class="buttons" :class="{active:isActive2==5}" @click="setDateRange(160,350);isActive2=5">3months</button>
                <button class="buttons" :class="{active:isActive2==6}" @click="setDateRange(70,350);isActive2=6">6months</button>
                <button class="buttons" :class="{active:isActive2==7}" @click="setDateRange(0,350);isActive2=7">1year</button>
            </div>
            <canvas id="myChart2"></canvas>
        </div>
    </div>
</template>
  


   
  
<script>
import WatchList from "./Watchlist.vue";
import Chart from "chart.js/auto";
import { useTickerStore } from "../stores/tickers.js"
import { storeToRefs } from 'pinia'
import { mapState } from 'pinia'
import { useOptionStore } from "../stores/options.js"
import { getChart } from "../getChart.js"




//import { ref } from "vue"


let stockPrice = []; // reverse order in datapoints ?
let stockDate = [];

let stockPrice2 = []; // reverse order in datapoints ?
let stockDate2 = [];


let myChart;
myChart;

let myChart2;
myChart2;

var tickerLabel = "";
var tickerLabel1 = "";

var default_ticker = "SPY";

const check_sectors = ['XLE','XLU','XLK','XLB','XLP','XLY','XLI','XLC','XLV','XLF','XLRE','SPY'];



export default {

    name: "LineChart",

    data(){
        return{
            isActive:undefined,
            isActive2:undefined,
            showWatchlist:false,
        }
    },

    components:{WatchList},

    mounted() {
        this.updateStockPriceHistoryChart();
        this.updateStockPriceHistoryChart2();
        
    },
    methods: {

         toggle(){
            this.showWatchlist = !this.showWatchlist
        },
        async fetchData(ticker,path,start,end) {
            const url = `http://localhost:3000/raw_${path}`;
            const response = await fetch(url);
            const datapoints = await response.json();
            console.log(Object.keys(datapoints));
            console.log(Object.values(datapoints));
            console.log(ticker);
            ticker = ticker.trim();
            tickerLabel1 = ticker;
            console.log("label= " + tickerLabel1)
            console.log(datapoints[ticker])
            stockDate = Object.keys(datapoints[ticker]);
            stockDate = stockDate.reverse();
            stockDate = stockDate.map(x => new Date(x*1));
            stockDate = stockDate.map(x => x.toLocaleDateString());
            stockDate = stockDate.slice(start,end);
            stockPrice = Object.values(datapoints[ticker]);
            stockPrice = stockPrice.reverse();
            stockPrice = stockPrice.slice(start,end);
            myChart.config.data.datasets[0].data = stockPrice;
            myChart.config.data.labels = stockDate;
            myChart.config.data.datasets[0].label = tickerLabel1;
            myChart.update();
            return datapoints;
        },

        async fetchData2(ticker,path,start,end) {
            const url = `http://localhost:3000/raw_${path}`;
            const response = await fetch(url);
            const datapoints = await response.json();
            console.log(Object.keys(datapoints));
            console.log(Object.values(datapoints));
            console.log(ticker);
            ticker = ticker.trim();
            tickerLabel = ticker;
            console.log("label= " + tickerLabel)
            console.log(datapoints[ticker])
            stockDate2 = Object.keys(datapoints[ticker]);
            stockDate2 = stockDate2.reverse();
            stockDate2 = stockDate2.map(x => new Date(x*1));
            stockDate2 = stockDate2.map(x => x.toLocaleDateString());
            stockDate2 = stockDate2.slice(start,end);
            stockPrice2 = Object.values(datapoints[ticker]);
            stockPrice2 = stockPrice2.reverse();
            stockPrice2 = stockPrice2.slice(start,end);
            myChart2.config.data.datasets[0].data = stockPrice2;
            myChart2.config.data.labels = stockDate2;
            myChart2.config.data.datasets[0].label = tickerLabel;
            myChart2.update();
            return datapoints;
        },

        async setDateRange1(start,end){
            var path = this.index.toLowerCase().trim()
            if(check_sectors.includes(this.ticker)){
                await this.fetchData(default_ticker,'sectors',start,end)
                 
            }
            else{
                await this.fetchData(this.index,path,start,end)  
                
            }
    
        },

        async setDateRange(start,end){
            var path = this.index.toLowerCase().trim()
            await this.fetchData2(this.ticker,path,start,end)
        
        },

    }, // if async created i need to put in arguments/parameters aswell..!!


    watch: {
        option: async function () {
            if (this.option == 'chart' && check_sectors.includes(this.ticker)) {
                this.$nextTick(function(){
                    this.fetchData2(this.ticker,'sectors',0,350)
                    this.fetchData(default_ticker,'sectors',0,350)
                    this.option="";
                    this.isActive=7;
                    this.isActive2=7;
                })
            }

            if (this.option == 'chart' && !check_sectors.includes(this.ticker)) {
                this.$nextTick(function(){
                    var path = this.index.toLowerCase().trim()
                    this.fetchData2(this.ticker,path,0,350)
                    this.fetchData(this.index,'sectors',0,350)
                    this.option="";
                    this.isActive=7;
                    this.isActive2=7;
                })
            }
            
        }
    },

    computed: {

        ...mapState(useOptionStore, ['option']), // to use this.xxx
        ...mapState(useTickerStore, ['ticker']), // to use this.
        ...mapState(useTickerStore, ['index']), // to use this.xxx


    },
    setup() {

        const tickerStore = useTickerStore();
        const { ticker } = storeToRefs(tickerStore)
        const { getTicker } = tickerStore

        const optionStore = useOptionStore();
        const { option } = storeToRefs(optionStore)
        const { getOption } = optionStore





        let updateStockPriceHistoryChart = () => {
            const ctx = document.getElementById("myChart");
            const labels = stockDate;

            const plugin = {
                id: 'custom_canvas_background_color',
                beforeDraw: (chart) => {
                    const { ctx } = chart;
                    ctx.save();
                    ctx.globalCompositeOperation = 'destination-over';
                    ctx.fillStyle = '#2A2E39';
                    ctx.fillRect(0, 0, chart.width, chart.height);
                    ctx.restore();
                }
            };

            const data = {
                labels: labels,
                datasets: [
                    {
                        label: tickerLabel1,
                        data: stockPrice,
                        fill: false,
                        borderColor: "rgb(75,192,192",
                        tension: 0,
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtzero: true
                                },
                            },
                        },
                    },
                ],
            };
            myChart = new Chart(ctx, {
                type: "line",
                data: data,
                plugins: [plugin],
            });
        };


        let updateStockPriceHistoryChart2 = () => {
            const ctx = document.getElementById("myChart2");
            const labels = stockDate2;

            const plugin = {
                id: 'custom_canvas_background_color',
                beforeDraw: (chart) => {
                    const { ctx } = chart;
                    ctx.save();
                    ctx.globalCompositeOperation = 'destination-over';
                    ctx.fillStyle = '#2A2E39';
                    ctx.fillRect(0, 0, chart.width, chart.height);
                    ctx.restore();
                }
            };

            const data = {
                labels: labels,
                datasets: [
                    {
                        label: tickerLabel,
                        data: stockPrice2,
                        fill: false,
                        borderColor: "rgb(75,192,192",
                        tension: 0,
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtzero: true
                                },
                            },
                        },
                    },
                ],
            };
            myChart2 = new Chart(ctx, {
                type: "line",
                data: data,
                plugins: [plugin],
            });
        };
        return {
            updateStockPriceHistoryChart,
            updateStockPriceHistoryChart2,
            tickerStore, ticker, getTicker,
            optionStore, option, getOption,
            getChart,
        };
    },
};

</script>
  
<style scoped>
* {
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

.chartMenu {
    width: 100vw;
    height: 40px;
    background: #1A1A1A;
    color: rgba(30, 68, 173, 0.733);
}

.chartMenu p {
    padding: 10px;
    font-size: 20px;
}

.chartCard {
    width: 70vw;
    height: calc(100vh - 300px);
    background:  #131722;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-radius: 10px;
    border: solid 3px #2A2E39;
    grid-row-start: 3;
    grid-column-start: 1;
    margin-top: 88px;
    
}



.chartBox {
    position: relative;
    width: 700px;
    padding: 20px;
    border-radius: 20px;
    border: solid 5px #131722;
    background: #2A2E39;

}

.chartBoxToggle{
    position: relative;
    width: 470px;
    padding: 20px;
    border-radius: 20px;
    border: solid 5px #131722;
    background: #2A2E39;

}

.chartBoxToggle.buttons{
    padding: 10px 5px;
    font-size: 15px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color:  #C3E0E5;
    background-color:  #131722;
    border: solid 2px  #2A2E39;
    border-radius: 10px;
    margin-bottom: 88px;
    font-weight: 500;

}

.buttons {
    padding: 10px 15px;
    font-size: 15px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color:  #C3E0E5;
    background-color:  #131722;
    border: solid 2px  #2A2E39;
    border-radius: 10px;
    margin-bottom: 88px;
    font-weight: 500;
}

.buttons:hover {
    background-color:  #131722;
    color: #E3B844;
}

.buttons:active {
    color: #E3B844;
    background-color: #131722;
    transform: translateY(4px);
    
}

.buttons.active{
    color: #E3B844;
}

.toggle{
    width: 50px;
    font-size: 50px;
}

.toggle:hover{
    color: #E3B844;
}

.toggle .tooltip {
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

.toggle:hover .tooltip {
  visibility: visible;
}

.slide-in{
 -webkit-animation: slideIn 0.5s forwards;
 -moz-animation: slideIn 0.5s forwards;
 animation: slideIn 0.5s forwards;

}

.slide-out{
-webkit-animation: slideOut 0.5s forwards;
 -moz-animation: slideOut 0.5s forwards;
 animation: slideOut 0.5s forwards;
 margin-right: -250px;

}

@-webkit-keyframes slideIn {
  0% {
    transform: translateX(-200px);
  }
  100% {
    transform: translateX(0);
  }
}
@-moz-keyframes slideIn {
  0% {
    transform: translateX(-200px);
  }
  100% {
    transform: translateX(0);
  }
}
@keyframes slideIn {
  0% {
    transform: translateX(-200px);
  }
  100% {
    transform: translateX(0);
  }
}

@-webkit-keyframes slideOut {
  100% {
    transform: translateX(-300px);
  }
  0% {
    transform: translateX(0);
  }
}
@-moz-keyframes slideOut {
  100% {
    transform: translateX(-300px);
  }
  0% {
    transform: translateX(0);
  }
}
@keyframes slideOut {
  100% {
    transform: translateX(-300px);
  }
  0% {
    transform: translateX(0);
  }
}











@media only screen and (max-width:1900px) {
    .chartBox {
        width: 50%;
        height: 45%;
        padding: 20px;
    }
}

@media only screen and (max-width:800px) {
    .chartBox {
        width: 300px;
        height: 300px;
        padding: 20px;
    }
}

@media only screen and (max-width:600px) {
    .chartBox {
        width: 200px;
        height: 200px;
        padding: 20px;
    }
}

@media only screen and (max-width:600px) {
    .chartCard {
        width: 70vw;
        height: calc(100vh - 40px);
        background: #2A2E39;
        display: block;
        align-items: center;
        border-radius: 20px;
        border: solid 5px #2A2E39;
    }
}
</style>