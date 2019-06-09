
function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  var metadata_url = `/metadata/${sample}`
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(metadata_url).then(function(metada_response){
    
    console.log(metadata_response)
    // Use d3 to select the panel with id of `#sample-metadata`
    var metadata_selector = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
    metadata_selector.html("");
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(metada_response).forEach(([key, value]) => {
      metadata_selector.append("li").text(`${key}: ${value}`);
      console.log(key, value);
    })
  })
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  var chart_url = `/samples/${sample}`

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(chart_url ).then(function(chart_response){
    console.log(chart_response)

    var otu_ids = chart_response.otus_ids;
    var otu_labels = chart_response.otu_lables;
    var sample_values = chart_response.sample_values;
    
    console.log(otu_ids, otu_labels, sample_values);

     // @TODO: Build a Bubble Chart using the sample data
    var bubble_trace = {
      x: otu_ids,
      y: sample_values,
      text: otu_labels,
      mode: 'markers',
      marker: {
        color: otu_ids,
        size: sample_values,
        showscale: True
      }
    };

    var bubble_data = [bubble_trace];

    var bubble_layout = {
      title: 'Marker Size and Color',
      showlegend: false,
      height: 600,
      width: 600
    };

    Plotly.newPlot("bubble", bubble_data, bubble_layout);
  
    // @TODO: Build a Pie Chart

    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
    var pie_data = [{
      values: chart_response.sample_values.slice(0, 11),
      ids: chart_response.otu_ids.slice(0, 11),
      labels: chart_response.otu_labels.slice(0, 11),
      type: "pie"
    }];
    
    var pie_layout = {
      title: "Bacterial Samples"
    };

    Plotly.newPlot("pie", pie_data, pie_layout);

  })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}
// Initialize the dashboard
init();
