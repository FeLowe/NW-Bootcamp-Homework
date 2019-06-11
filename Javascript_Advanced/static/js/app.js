
function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel
  var metadata_url = `/metadata/${sample}`
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(metadata_url).then(function(metada_response){
    
    // console.log(metadata_response)
    // Use d3 to select the panel with id of `#sample-metadata`
    var metadata_selector = d3.select("#sample-metadata");
    // Use `.html("") to clear any existing metadata
    metadata_selector.html("");
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(metada_response).forEach(([key, value]) => {
      metadata_selector
      .append("h5")
      .text(`${key}: ${value}`)
      .property("key", key)
      .property("value", value);
      
      console.log("key:", key, "value:", value);
    })
  })
    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);
}

function buildCharts(sample) {

  console.log("I am inside charts");
  
  var chart_url = `/samples/${sample}`

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  d3.json(chart_url).then((chart_response)=>{
    
    console.log("chart response:", chart_response)

    var otu_ids = chart_response.otu_ids;
    var otu_labels = chart_response.otu_labels;
    var sample_values = chart_response.sample_values;

    console.log("ids:", otu_ids, "labels:", otu_labels, "values:", sample_values);

      // Create array of Objects (one Object for each sample) 
      var sample_data = [];

      for (var i=0; i < otu_ids.length; i++) {
        data_dict = {};
  
        data_dict["otu_ids"] = otu_ids[i];
        data_dict["sample_values"] = sample_values[i];
        data_dict["otu_labels"] = otu_labels[i];
  
        sample_data[i] = data_dict;
  
        console.log(data_dict)
      };  
      
      // Sorts descending
      sample_data.sort(function compareFunction(first, second) {
        return second.sample_values - first.sample_values;
      });
  
     // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
      sample_data_top10 = sample_data.slice(0, 10);

      console.log (sample_data_top10)

      var pie_data = [{
        values: sample_data_top10.map(values => values.sample_values),
        labels: sample_data_top10.map(ids => ids.otu_ids),
        text: sample_data_top10.map(labels =>labels.otu_labels),
        type: "pie",
        startAngle: 500,
      }];

    var pie_layout = {
      title: "Top 10 Bacterial Samples"
    };

    Plotly.newPlot("pie", pie_data, pie_layout);

    // @TODO: Build a Bubble Chart using the sample data
    var bubble_trace = [{
      x: otu_ids,
      y: sample_values,
      text: otu_labels,
      type: 'scatter',
      mode: 'markers',
      marker: {
        color: otu_ids,
        size: sample_values,
        colorscale: 'Earth',
        showscale: true
      }
    }];

    var bubble_layout = {
      title:'Bacterial Ids vs Values',
      showlegend: false,
    };

    Plotly.newPlot("bubble", bubble_trace , bubble_layout);

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
