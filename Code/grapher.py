#-*-coding: utf8-*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

ticks_pos = [*range(100,0,-1)]
ticks_lbl = [*range(0,201)]


fig = go.Figure(data=
    go.Parcoords(name = "Attachment",
        line_color='red',
        dimensions = list([
            dict( label = 'UE',
                range = [-100,100],
                values = [100,98,95,91,86,80,73,65],              #Values are necessary
                tickvals = ticks_pos,
                ticktext = ticks_lbl
                #tickvals = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77],
                #ticktext = ticks_lbl
                #ticktext = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
            ),
            dict( label = 'eNodeB',
                range = [-100,100],
                values = [100,98,95,91,86,80,73,65],
                #values = [95,90,75],
                tickvals = ticks_pos,
                ticktext = ticks_lbl
                #tickvals = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77],                 #Sets the values at which ticks on this axis appear
                #ticktext = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]    #Sets the text displayed at the ticks position via `tickvals`
            ),
            dict( label = 'Coeur Reseau',
                range = [-100,100],
                values = [100,98,95,91,86,80,73,65],
                #values = [90,85,80],              #Values are necessary
                tickvals = ticks_pos,
                ticktext = ticks_lbl
                #tickvals = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77],
                #ticktext = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
            ),
        ])
    )
)

fig.update_layout(
    autosize=False,
    width=1300,
    height=5000,
    margin=dict(
        l=200,
        r=200,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightGray",
)

fig.update_yaxes(automargin=True)
fig.update_xaxes(automargin=True)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = "PIR"
colors = {
    #'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div( children=[                   #style={'backgroundColor': colors['background']},
    html.H1(
        children='Cellular Analysis -- PIR 7',
        style={
        'textAlign': 'center'#,
        #'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center'#,
        #'color': colors['text']
    }),

    dcc.Graph(
        id='Analyzing an attachment sequence',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
