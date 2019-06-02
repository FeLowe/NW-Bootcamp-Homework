// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

// Function to build table
function buildTable(data){

// Clear out existing data
tbody.html("");

  data.forEach((ufo_sighting) => {
    var row = tbody.append("tr");
    Object.entries(ufo_sighting).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
}
//Function that handle buttom click
function buttonClick(){

  //Prevents page from refreshing
  d3.event.preventDefault(); 
  
  //Takes user's input
  var dateInput = d3.select("#date").property("value");

  // Filter data based on user input
  if (dateInput){
  var filteredDate = tableData.filter(ufo => ufo.datetime === dateInput || dateInput === "");
} 
  buildTable(filteredDate);
} 
//Selects submit button
d3.select("#filter-btn").on("click", buttonClick);

buildTable(tableData)
