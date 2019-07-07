// create map
var map = L.map("map-id", {
  center: [37.09, -95.71],
  zoom: 4
});

// Set color array for magnitude

// var mag_colors = ["light green", "light", "dark yellow", "orange", "light red","dark red"]

var mag_colors = ["#CCFF33", "#FFE533", "#FFBA33", "#FF8C33", "#FF6533","#FF3F33"]

function getColor(magnitude){
  if (magnitude < 1){
    color = mag_colors[0];
  } else if (magnitude >= 1 && magnitude < 2){
    color = mag_colors[1];
  } else if (magnitude >= 2 && magnitude < 3){
    color = mag_colors[2];
  } else if (magnitude >= 3 && magnitude < 4){
    color = mag_colors[3];
  } else if (magnitude >= 4 && magnitude < 5){
    color = mag_colors[4];
  } else {
    color = mag_colors[5];
  }
  return color;
}
 
// Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: API_KEY
  }).addTo(map)

// Store our API endpoint inside queryUrl
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";


d3.json(url, function(response) {
  var data = response["features"];

//Loop through the data and create markers for each earthquake,
//bind popup containing magnitude, depth, time and color based on magnitude
for (var i = 0; i < data.length; i++) {
  var location = data[i]["geometry"]["coordinates"];
  var magnitude = data[i]["properties"]["mag"];
  var title = data[i]["properties"]["title"];
  var coords = {
    longitude: location["0"],
    latitude: location["1"]
  };
  
    var latlong = L.latLng(coords.latitude, coords.longitude);
    var circle = L.circle(latlong, {
      color: getColor(magnitude),
      fillOpacity: 0.50,
      radius: magnitude * 40000
    }).addTo(map);

    L.circle(latlong)
      .bindPopup("<h1>" + title + "</h1> <hr> <h3>Magnitude: " + magnitude + "</h3><h3>Latitude: " + coords.latitude + "</h3><h3>Longitude: " + coords.longitude + "</h3>")
      .addTo(map);
}

//Set up legend in bottom right
var legend = L.control({position: 'bottomright'});
legend.onAdd = function (map){
  var div = L.DomUtil.create('div', 'info legend'),
    grades = [0,1,2,3,4,5];
    div.innerHTML = '<h3>Earthquake Magnitude</h3>'

// Loop through our intervals and generate a label with a color square for each interval
  for (var i = 0; i < grades.length; i++){
    div.innerHTML +=
      '<i class="legend" style="background:' + mag_colors[i] + '; color:' + mag_colors[i] + ';">....</i>' +
      grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '++');
  }
  return div;
};

legend.addTo(map);

});
