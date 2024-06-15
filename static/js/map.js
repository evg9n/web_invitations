ymaps.ready(init);
function init(){
var myMap = new ymaps.Map("map", {
    center: [55.73956396894548,52.00157879743234],
    zoom: 12
});

var myPlacemark = new ymaps.Placemark(
    [55.76, 37.64],
    {
        hintContent: 'Москва!',
        balloonContent: 'Столица России'
    }
);

myMap.geoObjects.add(myPlacemark);
}