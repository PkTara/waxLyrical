fetch('./songInfo.json')
    .then((response) => response.json())
    .then((json) => {
        document.getElementById("songIMG").src=json["songCoverLink"]
        console.log()
    });

// Creating graph
const ctx = document.getElementById("songGraph")

fetch('./songGraph.json')
    .then((response) => response.json())
    .then((json) => {
        var xValues = json["x"];
        var yValues = json["y"];
        var barColors = ["red", "green","blue","orange","brown"];

        const chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: xValues,
            datasets: [{
            backgroundColor: barColors,
            data: yValues
            }]
        },
        options: {
            onClick: async (evt) => {
                
                const points = chart.getElementsAtEventForMode(evt, 'nearest', { intersect: true }, true);

                console.log(points)

    if (points.length) {
        const firstPoint = points[0];
        const label = chart.data.labels[firstPoint.index];
        const value = chart.data.datasets[firstPoint.datasetIndex].data[firstPoint.index];

        document.getElementById("word").innerHTML=label
        document.getElementById("wordDesc").innerHTML = json["translatedX"][xValues.indexOf(label)]
    }
    
}
            // indexAxis: "y",
            // scales: {
            //     xAxes: {
            //       ticks: {
            //         autoSkip: false,
            //         maxRotation: 90,
            //         minRotation: 90
            //       }
            //     }
            //   }
        }}
        );
    });

