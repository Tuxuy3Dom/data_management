import justpy as jp
import pandas as pd

def_chart = """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Analiza ocen kursów',
    align: 'center'
  },
  subtitle: {
    text: 'Poszczególne wykresy z analizą ocen kursu',
    align: 'center'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Data'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Srednia ocen'
    },
    labels: {
      format: '{value}°'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} | {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Temperature',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}"""

def app():
  data = pd.read_csv('reviews_courses.csv', parse_dates=['Timestamp'])
  data['Day'] = data['Timestamp'].dt.date
  day_avg = data.groupby(['Day']).mean()
  
  #web page
  wp = jp.QuasarPage()
    
  #(2A) - 1st example element
  h1 = jp.QDiv(a = wp, text = "Analiza ocen kursów", classes = "text-h3 text-center q-pa-md")
    
  #(2A) - 2nd example element
  p1 = jp.QDiv(a = wp, text="Poszczególne wykresy z analizą ocen kursu", classes = "text-center")
    
    
    # (3) Adding the HighCharts
  hc = jp.HighCharts(a = wp, options = def_chart)
    
  hc.options.title.text = 'Średnia ocen według dnia'
  hc.options.subtitle.text = 'Dane z pliku CSV'
  hc.options.series[0].name = 'Rating'
  hc.options.series[0].data = list(day_avg['Rating'])
  hc.options.xAxis.labels.format = list(day_avg.index)
    
  return wp

jp.justpy(app)
    