
let stockPrice2 = []; // reverse order in datapoints ?
let stockDate2 = [];

let myChart2;
myChart2;

var tickerLabel = "";


export async function getChart(ticker) {
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
}
