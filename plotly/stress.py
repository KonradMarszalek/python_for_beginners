import plotly.graph_objs as go
import plotly.plotly as py

load_76 = [6, 360, 2400, 3240]
load_80 = [6, 360, 3240, 4050, 4860, 6480]

marker = go.scatter.Marker(size=20, line=go.scatter.marker.Line(width=1))
line = go.scatter.Line(dict(width=4))

median_76 = go.Scatter(
    x=load_76,
    y=[192, 167, 217, 25916],
    mode='lines+markers',
    name='7.6 median',
    marker=marker,
    line=line
)
median_80 = go.Scatter(
    x=load_80,
    y=[137, 134, 179, 211, 8188, 29327],
    mode='lines+markers',
    name='8.0 median',
    marker=marker,
    line=line
)

percentile_95_76 = go.Scatter(
    x=load_76,
    y=[818, 591, 4261, 32675],
    mode='lines+markers',
    name='7.6 95th percentile',
    marker=marker,
    line=line
)
percentile_95_80 = go.Scatter(
    x=load_80,
    y=[402, 368, 500, 4020, 12794, 35612],
    mode='lines+markers',
    name='8.0 95th percentile',
    marker=marker,
    line=line
)

percentile_99_76 = go.Scatter(
    x=load_76,
    y=[4175, 623, 9776, 34424],
    mode='lines+markers',
    name='7.6 99th percentile',
    marker=marker,
    line=line
)
percentile_99_80 = go.Scatter(
    x=load_80,
    y=[435, 380, 6161, 8546, 14023, 38317],
    mode='lines+markers',
    name='8.0 99th percentile',
    marker=marker,
    line=line
)



# data = [median_76, median_80, percentile_95_76, percentile_95_80, percentile_99_76, percentile_99_80]
data = [percentile_99_76, percentile_99_80]

font = dict(family='Courier New, monospace', size=36, color='#7f7f7f')

layout = go.Layout()

layout.title = "Searches stress test"
layout.titlefont = font

layout.xaxis.title = "Load [requests / minute]"
layout.xaxis.titlefont = font
layout.xaxis.tickfont.size = 22
layout.xaxis.tickfont.family = 'Courier New, monospace'
layout.xaxis.tickfont.color = '#7f7f7f'
layout.xaxis.tickmode= "array"
layout.xaxis.ticktext = ["6x1", "6x60", "6x400", "6x540", "6x675", "6x810", "6x1080"]
layout.xaxis.tickvals = [6, 360, 2400, 3240, 4050, 4860, 6480]
layout.xaxis.tick0 = 0

layout.yaxis.title = "Response time [miliseconds]"
layout.yaxis.titlefont = font
layout.yaxis.tickfont.size = 22
layout.yaxis.tickfont.family = 'Courier New, monospace'
layout.yaxis.tickfont.color = '#7f7f7f'

layout.legend.font = font

layout.shapes = [{
    'type': 'line',
    'x0': 0,
    'y0': 10000,
    'x1': 7600,
    'y1': 10000,
    'line': {
        'color': 'rgb(11, 102, 35)',
        'width': 4,
        'dash': 'dash'
    },
}]

layout.annotations = [go.layout.Annotation(x=6400,
                                           y=9000,
                                           text='Acceptable deadline of 10 seconds',
                                           showarrow=False,
                                           font=font
                                           )]


fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='basic-line', auto_open=True)
