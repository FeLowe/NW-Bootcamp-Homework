
function makeResponsive() {

// if the SVG area isn't empty when the browser loads,
// remove it and replace it with a resized version of the chart
var svgArea = d3.select("body").select("svg");

if (!svgArea.empty()) {
  svgArea.remove();
}
// @TODO: YOUR CODE HERE!
// var svgWidth = 960;
// var svgHeight = 500;

// svg params
var svgHeight = window.innerHeight;
var svgWidth = window.innerWidth;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 50
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var scatterGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Retrieve data from the CSV file and execute everything below
d3.csv("data.csv").then(function(censusData) {
    // if (err) throw err;

    // console.log(censusData);

    // Parse Data/Cast as numbers
    censusData.forEach(function(data){
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;

        console.log("poverty rate:", data.poverty)
    });

    //Create scale functions
    var xLinearScale = d3.scaleLinear()
        .domain([8, d3.max(censusData, d => d.poverty)])
        .range([0, width -200]);

    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(censusData, d => d.healthcare)])
        .range([height, 0]);

    // Create axis functions
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append Axes to the chart
    scatterGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    // append y axis
    scatterGroup.append("g")
      .call(leftAxis);

    // Create Circles
    var circlesGroup = scatterGroup.selectAll("circle")
    .data(censusData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "15")
    .attr("fill", "orange")
    .attr("opacity", ".5")
 
    //Create circle labels
    var circleLabels = scatterGroup.selectAll(null)
    .data(censusData)
    .enter()
    .append("text");

    circleLabels
      .attr("x", function(d) {
        return xLinearScale(d.poverty);
      })
      .attr("y", function(d) {
        return yLinearScale(d.healthcare);
      })
      .text(function(d) {
        return d.abbr;
      })
      .attr("font-family", "sans-serif")
      .attr("font-size", "12px")
      .attr("text-anchor", "middle")
      .attr("fill", "black")
      .attr("stroke", "black");

    //Initialize tool tip
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
  return (`${d.state}<tr> <br>Poverty: ${d.poverty}<br>Healthcare: ${d.healthcare}`);
});

    // Create tooltip in the chart
    scatterGroup.call(toolTip);

    // Create event listeners to display and hide the tooltip
    circleLabels.on("click", function(data) {
      toolTip.show(data, this);
    })
      //mouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

    // Create axes labels
    scatterGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");

    scatterGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("In Poverty (%)");
  });
}

makeResponsive();

// Event listener for window resize.
// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);

