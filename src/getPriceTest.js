export function getPriceTest(index) {
    var element = document.getElementsByClassName('listItem')
    var price = element[index].querySelector('#price').innerHTML;
    return price
}