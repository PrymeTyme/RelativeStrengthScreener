<template>
    <div class="lineChart">
        <div id="chartContainer">
            <div>
                <button class="buttons" @click="fetchData()">fetch</button>
            </div>
            <canvas id="myChart"> </canvas>
        </div>
        <div id="chartContainer">
            <div>
                <button class="buttons" @click="fetchData2()">fetch2</button>
            </div>
            <canvas id="myChart2"> </canvas>
        </div>
    </div>

</template>
  


   
  
<script>
import Chart from "chart.js/auto";

let stockPrice = []; // reverse order in datapoints ?
let stockDate = [];

let stockPrice2 = []; // reverse order in datapoints ?
let stockDate2 = [];

let myChart;
myChart;

let myChart2;
myChart2;


export default {

    name: "LineChart",
    mounted() {
        this.updateStockPriceHistoryChart();
        this.updateStockPriceHistoryChart2();
    },
    methods: {
        async fetchData() {
            const url = 'http://localhost:3000/SPY';
            const response = await fetch(url);
            const datapoints = await response.json();
            console.log(Object.keys(datapoints));
            console.log(Object.values(datapoints));
            console.log(datapoints)
            stockDate = Object.keys(datapoints);
            stockDate = stockDate.reverse();
            stockDate = stockDate.map(x => new Date(x * 1000));
            stockDate = stockDate.map(x => x.toLocaleDateString());
            stockPrice = Object.values(datapoints);
            stockPrice = stockPrice.reverse();
            myChart.config.data.datasets[0].data = stockPrice;
            myChart.config.data.labels = stockDate;
            myChart.update();
            return datapoints;
        },

        async fetchData2() {
            const url = 'http://localhost:3000/XLE';
            const response = await fetch(url);
            const datapoints = await response.json();
            console.log(Object.keys(datapoints));
            console.log(Object.values(datapoints));
            console.log(datapoints)
            stockDate2 = Object.keys(datapoints);
            stockDate2 = stockDate2.reverse();
            stockDate2 = stockDate2.map(x => new Date(x * 1000));
            stockDate2 = stockDate2.map(x => x.toLocaleDateString());
            stockPrice2 = Object.values(datapoints);
            stockPrice2 = stockPrice2.reverse();
            myChart2.config.data.datasets[0].data = stockPrice2;
            myChart2.config.data.labels = stockDate2;
            myChart2.update();
            return datapoints;
        },

    },
    setup() {
        let updateStockPriceHistoryChart = () => {
            const ctx = document.getElementById("myChart");
            const labels = stockDate;

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
                        },
                    },
                ],
            };
            myChart = new Chart(ctx, {
                type: "line",
                data: data,
            });
        };



        let updateStockPriceHistoryChart2 = () => {
            const ctx = document.getElementById("myChart2");
            const labels = stockDate2;

            const data = {
                labels: labels,
                datasets: [
                    {
                        label: "Stock Market Price",
                        data: stockPrice2,
                        fill: false,
                        borderColor: "rgb(75,192,192",
                        tension: 0,
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                        },
                    },
                ],
            };
            myChart2 = new Chart(ctx, {
                type: "line",
                data: data,
            });
        };
        return {
            updateStockPriceHistoryChart,
            updateStockPriceHistoryChart2,
        };
    },
};

</script>
  
<style scoped>
#chartContainer {
    width: 500px;
    height: 500px;
    margin: 0 auto;
    float: left
}

#myChart,
#myChart2 {
    width: 320px;
    height: 350px;
}

.buttons {
    float: top;
}


.lineChart {
    display: grid;
    grid-template-columns: 80px auto;
}
</style>s