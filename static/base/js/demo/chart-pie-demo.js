// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["MAS IPSP","PASO","MTS","PAN-BOL", "MDA","CID","BLANCO","NULO"],
    datasets: [{
      data: [44,9,30,7, 10,5,2,3],
      backgroundColor: ['#4e73df','#05ff80','#1cc88a','#fc0000','#fff600','#ff5733','#ffffff','#000000'],
      hoverBackgroundColor: ['#2e59d9','#04a654', '#17a673','#c80808','#d3cb01','#ff9078','#f4ecec','#544f4f'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
