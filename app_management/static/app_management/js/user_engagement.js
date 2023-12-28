
//Programme Management Audit Trail
function showAuditPro(id){
    // Get the modal dialog element
    var modal = document.getElementById("myModal");
    
    // Get the button that opens the modal
    var btn = document.getElementById(id);
    
    // Get the <span> element that closes the modal
    var closeBtn = document.getElementsByClassName("close")[0];
    
    // When the user clicks the button, open the modal
    btn.onclick = function() {
      modal.style.display = "block";
    }
    
    // When the user clicks on <span> (x), close the modal
    closeBtn.onclick = function() {
      modal.style.display = "none";
    }
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
}

//Page Visits
function getPageVisists(value){
document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the page data from the server
    var pageData = value;

    // Extract the page URLs and visit counts
    var pageUrls = pageData.map(function(item) {
        return item.page_url;
    });
    var visitCounts = pageData.map(function(item) {
        return item.visit_count;
    });
var colors = ['rgb(181,153,173)','rgb(255, 255, 135)','rgb(148,185,65)','rgb(248,163,163)','rgb(109,209,174)','rgb(53, 107, 255)','rgb(135,105,209)','rgb(255, 174, 53)'];

// Create legend items with respective colors and names
var legendItems = pageUrls.map(function(label, index) {
    return {
        name: label,
        y: visitCounts[index],
        color: colors[index]
    };
});

// Create Highcharts chart with the custom legend
pageVisitsChart = Highcharts.chart('pageVisitsChart', {
    chart: {
        type: 'pie'
    },
    title: {
        text: ''
    },
    plotOptions: {
        pie: {
            allowPointSelect: false,
            cursor: 'pointer',
            dataLabels: {
                enabled: false,
                format: '{point.name}: {point.y}',
                style: {
                    color: 'black'
                }
            },
            showInLegend: true, // Show legend
            size: '120%' // Set the size of the pie chart
        }
    },
    series: [{
        name: 'Page Visits',
        data: legendItems
    }],
    tooltip: {
        pointFormat: '{point.name}: <b>{point.y}</b>'
    },
    legend: {
        align: 'left', // Align legend to the left side
        verticalAlign: 'bottom', // Align legend to the bottom
        layout: 'horizontal', // Arrange legend items horizontally
        itemMarginTop: 10,
        itemStyle: {
            color: 'black'
        },
        symbolWidth: 0
    },
    credits: {
        enabled: false
    },
});

    
});
}

//Conversion Rate
 
function Conversion(conversion_rate_verify,users_completed_action_verify,total_users_count_verify,conversion_rate_review
    ,users_completed_action_review,total_users_count_review,conversion_rate_capture,users_completed_action_capture,total_users_count_capture){
        var conversion_rate_verify = conversion_rate_verify;
        var users_completed_action_verify = users_completed_action_verify;
        var total_users_count_verify = total_users_count_verify;

        var conversion_rate_review =conversion_rate_review;
        var users_completed_action_review = users_completed_action_review;
        var total_users_count_review = total_users_count_review;

        var conversion_rate_capture = conversion_rate_capture;
        var users_completed_action_capture = users_completed_action_capture;
        var total_users_count_capture =total_users_count_capture;

        // Create chart data
        var data = {
            labels: ['Verify', 'Review', 'Capture'],
            datasets: [
                {
                    label: 'Conversion Rate',
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    data: [conversion_rate_verify, conversion_rate_review, conversion_rate_capture]
                },
                {
                    label: 'Users Completed Action',
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    data: [users_completed_action_verify, users_completed_action_review, users_completed_action_capture]
                },
                {
                    label: 'Total Users Count',
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    data: [total_users_count_verify, total_users_count_review, total_users_count_capture]
                }
            ]
        };

        // Configuration options
        var options = {
            responsive: true,
            scales: {
                x: {
                    beginAtZero: true
                },
                y: {
                    beginAtZero: true
                }
            }
        };

        // Create bar graph
        //var ctx = document.getElementById('baGraph').getContext('2d');
        //new Chart(ctx, {
         //   type: 'bar',
         //   data: data,
          //  options: options
       // });

}

function activeusers(active_users_count,total_users_count){
    var active_users_countt = active_users_count;
    var target_active_users_countt = total_users_count;
    
    Highcharts.chart('barGraph', {
        chart: {
            type: 'column'
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: ['Active Users']
        },
        yAxis: {
            title: {
                text: 'Count'
            }
        },
        series: [{
            name: 'Current Count',
            data: [active_users_countt],
            color: 'rgb(255, 174, 53)'
        }, {
            name: 'Target Count',
            data: [target_active_users_countt],
            color: 'rgb(135,105,209)'
        }],
        plotOptions: {
            column: {
                borderWidth: 1,
                borderColor: 'transparent'
            }
        }, 
        credits: {
            enabled: false
        }
    });
    
}

//Daily Active Users
function dau(dau,total_users_count){
        // Variables
var dau = dau // Your dau value;
var total_users_count = total_users_count // Your total_users_count value;
var desired_percentage = 0.3;

var minimum_logins = total_users_count * desired_percentage;

// Calculate percentage
var percentage = (dau / minimum_logins) * 100;

// Create the Highcharts gauge chart
Highcharts.chart('gaugeGraph', {
    chart: {
        type: 'pie',
        marginTop: 50
    },
    title: {
        text: '',
        style: {
            fontSize: '24px'
        }
    },
    pane: {
        center: ['50%', '85%'],
        size: '90%',
        startAngle: -90,
        endAngle: 90,
        background: {
            backgroundColor: 'rgb(109,209,174)',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc'
        }
    },
    tooltip: {
        enabled: false
    },
    yAxis: {
        min: 0,
        max: 100,
        stops: [
            [0.1, '#DF5353'], // Red
            [0.5, '#DDDF0D'], // Yellow
            [0.9, '#55BF3B']  // Green
        ],
        lineWidth: 0,
        tickWidth: 0,
        minorTickInterval: null,
        tickAmount: 2,
        title: {
            y: -70
        },
        labels: {
            y: 16
        }
    },
    plotOptions: {
        solidgauge: {
            dataLabels: {
                y: 5,
                borderWidth: 0,
                useHTML: true
            }
        }
    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Percentage',
        data: [percentage],
        dataLabels: {
            format: '<div style="text-align:center"><span style="font-size:25px;color:' +
                ('black') + '">{y}%</span><br/>'
        },
        tooltip: {
            valueSuffix: ' %'
        },
        size: '95%',
        innerSize: '50%',
    }]
});

}

//Retantion Rate
function Retantion(retention_7_days,retention_30_days,retention_90_days,retChart){
    // Sample retention rates
const retentionData = [
    { timePeriod: '7 days', rate: retention_7_days },
    { timePeriod: '30 days', rate: retention_30_days },
    { timePeriod: '90 days', rate: retention_90_days }
];

// Extract labels and rates from the data
const labels = retentionData.map(data => data.timePeriod);
const rates = retentionData.map(data => data.rate);

// Create the Highcharts chart
Highcharts.chart(retChart, {
    chart: {
        type: 'line'
    },
    title: {
        text: ''
    },
    xAxis: {
        categories: labels
    },
    yAxis: {
        title: {
            text: 'Rate (%)'
        },
        min: 0,
        max: 100
    },
    credits: {
        enabled: false
    },
    series: [{
        name: 'Retention Rate',
        data: rates,
        color: 'rgb(255, 174, 53)',
        marker: {
            fillColor: 'white',
            lineWidth: 2,
            lineColor: 'rgb(255, 174, 53)',
            radius: 6,
            symbol: 'circle'
        }
    }]
});

}


function dayuservount(dates,counts){
        // Create the Highcharts line chart
        // Sort the dates array in ascending order
       
        Highcharts.chart('user-engagement-chart', {
            title: {
                text: ''
            },
            credits: {
                enabled: false
            },
            xAxis: {
                categories: dates,
                title: {
                    text: 'Date'
                }
            },
            yAxis: {
                title: {
                    text: 'Number of Users'
                }
            },
            series: [{
                name: 'Users',
                color: 'rgb(255, 174, 53)',
                data: counts
            }]
        });
}