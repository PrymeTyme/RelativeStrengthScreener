//export function getData() {
//let elements = []
//fetch('http://localhost:3000/sector_daily')
//  .then(res => res.json())
// .then(data => elements = data)
// .catch(err => console.log(err.message))
// return elements
//}



export async function getData() {
    const data = [];
    const url = 'http://localhost:3000/sector_daily';
    const response = await fetch(url);
    const datapoints = await response.json();

    for (var k in datapoints["Ticker"]) {
        if (datapoints["Percent Change"][k] >= 0) {
            data.push({
                ticker: datapoints["Ticker"][k],
                price: datapoints["Price"][k],
                change: datapoints["Percent Change"][k],
                changeColor: "green"
            }
            )
        } else if (datapoints["Percent Change"][k] < 0) {
            data.push({
                ticker: datapoints["Ticker"][k],
                price: datapoints["Price"][k],
                change: datapoints["Percent Change"][k],
                changeColor: "red"
            })
        }

    }
    //console.log(data)
    //console.log(data[0].ticker)
    //console.log(data[0].price)
    return data;
}

//let data = fetchData()

//export function getData(data) {
//    const output = [];
//    for (let index = 0; index < data; index++) {
//        output.push({
//            id: String(idCounter++),
//            text: Math.random()
//                .toString(16)
//                .substr(10),
//        });
//    }
//    return output;
//}