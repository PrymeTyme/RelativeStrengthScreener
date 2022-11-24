export async function getCarouselData(timeframe) {
    const sectors = ['XLE', 'XLU', 'XLK', 'XLB', 'XLP', 'XLY', 'XLI', 'XLC', 'XLV', 'XLF', 'XLRE'];
    const data = [];

    for (var j in sectors) {
        var url = `http://localhost:3000/sorted_${sectors[j].toLowerCase()}_${timeframe}`;
        var response = await fetch(url);
        var datapoints = await response.json();
        for (let k = 0; k < 1; k++) {
            if (datapoints["Percent Change"][k] >= 0) {
                data.push({
                    strongest: datapoints["Ticker"][k],
                    weakest: datapoints.Ticker[Object.keys(datapoints.Ticker)[Object.keys(datapoints.Ticker).length-1]],
                    weakestChange: datapoints["Percent Change"][Object.keys(datapoints["Percent Change"])[Object.keys(datapoints["Percent Change"]).length-1]],
                    price: datapoints["Price"][k],
                    change: datapoints["Percent Change"][k],
                    index: datapoints["Index"][k],
                    name: datapoints["Name"][k],
                    changeColor: "#77D3AD"
                }
                )
            } else if (datapoints["Percent Change"][k] < 0) {
                data.push({
                    strongest: datapoints["Ticker"][k],
                    weakest: datapoints.Ticker[Object.keys(datapoints.Ticker)[Object.keys(datapoints.Ticker).length-1]],
                    weakestChange: datapoints["Percent Change"][Object.keys(datapoints["Percent Change"])[Object.keys(datapoints["Percent Change"]).length-1]],
                    price: datapoints["Price"][k],
                    change: datapoints["Percent Change"][k],
                    index: datapoints["Index"][k],
                    name: datapoints["Name"][k],
                    changeColor: "#D72375"
                })
            }

        }
    }
    //console.log(data)
    //console.log(data[0].ticker)
    //console.log(data[0].price)
    return data;
}