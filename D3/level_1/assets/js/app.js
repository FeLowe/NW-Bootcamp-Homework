// @TODO: YOUR CODE HERE!
var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
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
        .range([0, width]);

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
    .attr("cx", d => xLinearScale(d.poverty)-4)
    .attr("cy", d => yLinearScale(d.healthcare)+2)
    .attr("r", "15")
    .attr("fill", "orange")
    .attr("opacity", ".5")
 

    circlesGroup.append("text").text(d=>d.abbr)
    .style("font-size",".6em")
    .classed("fill-text", true);

    //Initialize tool tip
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
  return (`${d.state}/${d.abbr}<tr> <br>Poverty: ${d.poverty}<br>Healthcare: ${d.healthcare}`);
});

    // Create tooltip in the chart
    // ==============================
    scatterGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    // ==============================
    circlesGroup.on("click", function(data) {
      toolTip.show(data, this);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

    // Create axes labels
    scatterGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");

    scatterGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("In Poverty (%)");
  });


//     //Initialize tool tip
//     var toolTip = d3.tip()
//     .attr("class", "tooltip")
//     .offset([80, -60])
//     .html(function(data) {
//         var state = data.state;
//         var state_code = data.abbr;
//         var poverty_rate = +data.poverty;
//         var healthcare_rate = +data.healthcare;

//       return (`In ${state} / ${state_code}<br>Poverty rate is: ${poverty_rate}<br>And Healthcare rate is:${healthcare_rate}`);
//     // var toolTip = d3.tip()
//     //   .attr("class", "tooltip")
//     //   .offset([80, -60])
//     //   .html(function(row) {

//     //   return (`In ${row.state} / ${row.abbr}<br>Poverty rate is: ${row.poverty}<br>And Healthcare rate is: ${row.healthcare}`);
//     // });

// });
//     // Create tooltip in the chart
//     scattherGroup.call(toolTip);
    
//     });

// });
