var width = parseFloat(document.getElementById('width').textContent.replace(',', '.'));
var longitude = parseFloat(document.getElementById('longitude').textContent.replace(',', '.'));
var name_label = document.getElementById('name_label').textContent;
console.log(width);
console.log(longitude);
ymaps.ready(init);
function init(){
var myMap = new ymaps.Map("map", {
    center: [width,longitude],
    zoom: 12
});

var myPlacemark = new ymaps.Placemark(
    [width,longitude],
    {
        hintContent: name_label,
        balloonContent: name_label
    }
);

myMap.geoObjects.add(myPlacemark);
}