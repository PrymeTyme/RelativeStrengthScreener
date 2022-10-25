<template>
    <div class="chartCard">
        <div class="chartBox">
            <div>
                <button class="buttons" @click="fetchData()">fetch</button>
            </div>
            <canvas id="myChart"></canvas>
        </div>
        <div class="chartBox">
            <div>
                <button class="buttons" @click="fetchData2(ticker)">fetch2</button>
            </div>
            <canvas id="myChart2"></canvas>
        </div>
    </div>
</template>
  


   
  
<script>
import Chart from "chart.js/auto";
import { useTickerStore } from "../stores/tickers.js"
import { storeToRefs } from 'pinia'
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




export default {

    name: "LineChart",
    data() {
        return {

        }
    },
    mounted() {
        this.updateStockPriceHistoryChart();
        this.updateStockPriceHistoryChart2();
    },
    methods: {
        async fetchData() {
            const url = 'http://localhost:3000/raw_sectors';
            const response = await fetch(url);
            const datapoints = await response.json();
            console.log(Object.keys(datapoints));
            console.log(Object.values(datapoints));
            console.log(datapoints["SPY"])
            stockDate = Object.keys(datapoints["SPY"]);
            stockDate = stockDate.reverse();
            stockDate = stockDate.map(x => new Date(x * 1000));
            stockDate = stockDate.map(x => x.toLocaleDateString());
            stockPrice = Object.values(datapoints["SPY"]);
            stockPrice = stockPrice.reverse();
            myChart.config.data.datasets[0].data = stockPrice;
            myChart.config.data.labels = stockDate;
            myChart.update();
            return datapoints;
        },

        async fetchData2(ticker) {
            const url = 'http://localhost:3000/raw_sectors';
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
            stockDate2 = stockDate2.map(x => new Date(x * 1000));
            stockDate2 = stockDate2.map(x => x.toLocaleDateString());
            stockPrice2 = Object.values(datapoints[ticker]);
            stockPrice2 = stockPrice2.reverse();
            myChart2.config.data.datasets[0].data = stockPrice2;
            myChart2.config.data.labels = stockDate2;
            myChart2.config.data.datasets[0].label = tickerLabel;
            myChart2.update();
            return datapoints;
        },

    },
    setup() {

        const tickerStore = useTickerStore();
        const { ticker } = storeToRefs(tickerStore)
        const { getTicker } = tickerStore




        let updateStockPriceHistoryChart = () => {
            const ctx = document.getElementById("myChart");
            const labels = stockDate;

            const plugin = {
                id: 'custom_canvas_background_color',
                beforeDraw: (chart) => {
                    const { ctx } = chart;
                    ctx.save();
                    ctx.globalCompositeOperation = 'destination-over';
                    ctx.fillStyle = '#C3E0E5';
                    ctx.fillRect(0, 0, chart.width, chart.height);
                    ctx.restore();
                }
            };

            const data = {
                labels: labels,
                datasets: [
                    {
                        label: "Stock Market Price",
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
                    ctx.fillStyle = '#C3E0E5';
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
    height: calc(100vh - 40px);
    background: #5885AF;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    border: solid 3px #41729F;
    grid-row-start: 2;
    grid-column-start: 1;
}

.chartBox {
    position: relative;
    width: 700px;
    padding: 20px;
    border-radius: 20px;
    border: solid 1px #41729F;
    background: #C3E0E5;
}

.buttons {
    padding: 10px 15px;
    font-size: 18px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color: #41729fd0;
    background-color: #41729f4b;
    border: solid 2px #41729F;
    border-radius: 10px;
}

.buttons:hover {
    background-color: #41729F;
    color: #C3E0E5;
}

.buttons:active {
    color: #41729fd0;
    background-color: #41729f4b;
    transform: translateY(4px);
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
        background: #5885AF;
        display: block;
        align-items: center;
        border-radius: 20px;
        border: solid 5px #41729F;
    }
}
</style>