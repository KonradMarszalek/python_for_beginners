import plotly.graph_objs as go
import plotly.plotly as py

load_76 = [6, 360, 2400, 3240]
load_80 = [6, 360, 3240, 4050, 4860, 6480]

marker = go.scatter.Marker(size=20, line=go.scatter.marker.Line(width=1))
line = go.scatter.Line(dict(width=4))

errors_76 = go.Scatter(
    x=load_76,
    y=[0.00, 0.00, 0.00, 0.3425],
    mode='lines+markers',
    name='7.6 errors',
    marker=marker,
    line=line
)
errors_80 = go.Scatter(
    x=load_80,
    y=[0.00, 0.00, 0.00, 0.00, 0.00, 0.2008],
    mode='lines+markers',
    name='8.0 errors',
    marker=marker,
    line=line
)





data = [errors_76, errors_80]

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

layout.yaxis.title = "Errors [percentage of requests]"
layout.yaxis.titlefont = font
layout.yaxis.tickfont.size = 22
layout.yaxis.tickfont.family = 'Courier New, monospace'
layout.yaxis.tickfont.color = '#7f7f7f'
layout.yaxis.tickformat = '%'

layout.legend.font = font


fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='basic-line', auto_open=True)
