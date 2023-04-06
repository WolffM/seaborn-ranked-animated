import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.subplots as subplots
import csv

winColor = '#0FFC7E'
loseColor = '#F53524'
defaultColor = '#ffffff'

gold_tag = 'Emblem_Gold.png'
plat_tag = 'Emblem_Platinum.png'
diamond_tag = 'Emblem_Diamond.png'
master_tag = 'Emblem_Master.png'


def createFig():
    fig = subplots.make_subplots()
    fig.update_layout(shapes=[
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=200,
            x1=1,
            y1=300,
            fillcolor='#E6D115', #gold2
            line=dict(
                width=0
            ),
            opacity=0.8,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=300,
            x1=1,
            y1=400,
            fillcolor='#E6D115', #gold1
            line=dict(
                width=0
            ),
            opacity=0.9,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=400,
            x1=1,
            y1=500,
            fillcolor='#057853', #plat4
            line=dict(
                width=0
            ),
            opacity=0.6,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=500,
            x1=1,
            y1=600,
            fillcolor='#057853', #plat3
            line=dict(
                width=0
            ),
            opacity=0.7,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=600,
            x1=1,
            y1=700,
            fillcolor='#057853', #plat2
            line=dict(
                width=0
            ),
            opacity=0.8,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=700,
            x1=1,
            y1=800,
            fillcolor='#057853', #plat1
            opacity=0.9,
            line=dict(
                width=0
            ),
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=800,
            x1=1,
            y1=900,
            fillcolor='#3239bf', #diamond4
            line=dict(
                width=0
            ),
            opacity=0.6,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=900,
            x1=1,
            y1=1000,
            fillcolor='#3239bf', #diamond3
            line=dict(
                width=0
            ),
            opacity=0.7,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=1000,
            x1=1,
            y1=1100,
            fillcolor='#3239bf', #diamond2
            line=dict(
                width=0
            ),
            opacity=0.8,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=1100,
            x1=1,
            y1=1200,
            fillcolor='#3239bf', #diamond1
            line=dict(
                width=0
            ),
            opacity=0.9,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=1200,
            x1=1,
            y1=1350,
            fillcolor="#AA45CC", #master
            line=dict(
                width=0
            ),
            opacity=0.7,
            layer="below"
        )
    ])
    fig.update_layout(width=1536, height=864)
    fig.update_layout(xaxis_title="GameId", yaxis_title="TotalLp", title_text="Ranked Climb to Masters!")
    fig.update_layout(
        plot_bgcolor="#333333", # Set the background color to dark grey
        paper_bgcolor="#333333", # Set the paper background color to dark grey
        font_color="#FFFFFF" # Set the font color to white
    )
    return fig
def addPatchLines():
    d=""    
def makePlot(filename):
    #This creates a fig background
    fig = createFig()
    fig.update_layout(
        annotations=[
            go.layout.Annotation(
                text="Hello",
                x=1,
                y=300,
                xref="paper",
                yref="paper",
                align="right",
                font=dict(
                    size=18,
                    color="#F2EBE9"
                ),
                showarrow=False
            )
        ]
    )
    with open(filename) as f:
        reader = csv.reader(f)
        x_values = []
        y_values = []
        frames = []

        minX = 1000
        minY = 1000
        maxX = 10
        maxY = 400

        maxLoss = 0
        maxWin = 0

        markerColors = [winColor]
        sizes = [2]

        prevY = 0
        prevColor = defaultColor
        currentSize = 5
        currentStreak = 1.0

        for row in reader:
            x = int(row[0])
            y = int(row[13])

            #if(x>834):
            #    break
            #if(x>1242):
            #    break
            if prevY !=0:
                if row[12] == 'True':
                    if prevColor == winColor:
                        currentStreak+=.3
                    else:
                        currentStreak=1
                    markerColors.append(winColor)
                    sizes.append(currentSize*currentStreak)
                    prevColor = winColor
                    if currentStreak>maxWin:
                        maxWin=currentStreak
                else:
                    if prevColor == loseColor:
                        currentStreak+=.3
                    else:
                        currentStreak=1
                    markerColors.append(loseColor)
                    sizes.append(currentSize*currentStreak)
                    prevColor = loseColor
                    if currentStreak>maxLoss:
                        maxLoss=currentStreak

            prevY = y
            if x < minX:
                minX = x-2
            elif x > maxX:
                maxX = x+2
            if y < minY:
                minY = y-50
            elif y > maxY:
                maxY = y+50
            #if maxY-minY>500:
            #    minY = maxY-500
            #if maxX-minX>300:
            #    minX = maxX-300
            x_values.append(x)
            y_values.append(y)
            frames.append(go.Frame(data=[go.Scatter(x=x_values, y=y_values, 
                                            mode='lines+markers', 
                                            name='main',
                                            showlegend=True,
                                            line=dict(color='#F2EBE9', width=4),
                                            marker=dict(size=sizes, color=markerColors))],
                                    layout=go.Layout(
                                            xaxis=dict(range=[minX, maxX]), 
                                            yaxis=dict(range=[minY, maxY]),
                                    annotations=[go.layout.Annotation(
                                            text=f"{row[14]}   +{row[13]} lp", 
                                            x=1, 
                                            y=0, 
                                            xref='paper', 
                                            yref='paper', 
                                            align='right', 
                                            font=dict(size=24),
                                            showarrow=False)])))
    # Add trace
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines', name='lines'))

    # Set the frames parameter of the Figure object
    fig.frames = frames

    # Remove the X and Y axis labels
    fig.update_layout(
        xaxis=dict(showticklabels=False, title=None, showgrid=False),
        yaxis=dict(showticklabels=False, title=None, showgrid=False)
    )

    fig.update_layout(
        updatemenus=[dict(buttons = [dict(
                                    args = [None, {"frame": {"duration": 75, 
                                                            "redraw": False},
                                                    "fromcurrent": True, 
                                                    "transition": {"duration": 1}}],
                                    label = "Play",
                                    method = "animate")],
                    type='buttons',
                    showactive=False,
                    y=1,
                    x=1.12,
                    xanchor='right',
                    yanchor='top')])
    
    # Display the plot
    fig.show()