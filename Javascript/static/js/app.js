// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

data.forEach((ufo_sighting) => {
  var row = tbody.append("tr");
  Object.entries(ufo_sighting).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});


