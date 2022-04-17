
function exeData1(){
    var request = new XMLHttpRequest();

    request.open('GET', 'http://127.0.0.1:8000/data_1/', true);
    request.responseType = 'json';
    var data = this.response;

    request.onload = function () {
    var data = this.response;
    console.log(data);

    //Chart.js
    function storeData(name){
        const storeName = data.filter(x => x.store === name);
        const chartData = {};
            chartData.label = name;
            chartData.data = storeName.map(y => y.members);
            switch (name) {
                case "A":
                    chartData.backgroundColor = "#ffc0cb";
                break;
                case "B":
                    chartData.backgroundColor = "#fffacd";
                break;
                case "C":
                    chartData.backgroundColor = "#98fb98";
                break;
            }
        console.log(chartData);
        return chartData;
    }

    const month = data.map(m => m.month);
    const monthArr = Array.from(new Set(month));
    console.log(monthArr);

    const ctx = document.getElementById("myChart").getContext("2d");
    const myChart = new Chart(ctx, {
        type: "bar",
            data: {
            labels: monthArr,
            datasets: [storeData("A"), storeData("B"), storeData("C")]
        },
            options: {
            title: {
                display: true,
                text: "BarChart"
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'members'
                    },
                    ticks: {
                        suggestedMin: 0,
                        stepSize: 300,
                        callback: function(label){
                            return label.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
                        }
                    }
                }]
            }
        }
    });
    };

    request.send();
}

