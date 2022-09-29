export function getTicker(index){
    var element = document.getElementsByClassName('listItem');
    var ticker = element[index].firstChild.data;
    console.log(ticker);
    //console.log(element)
    return ticker
  }