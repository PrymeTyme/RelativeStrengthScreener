export function getPrice() {
    var element = document.getElementsByClassName('listItem');

    for (var i = 0; i < element.length; i++) {
        var price = element[i].querySelector('#price').innerHTML
        console.log(price)
    }
    console.log(price);
    return price
}