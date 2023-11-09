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
    
    colors = ['#E6D115', '#057853', '#3239bf', "#AA45CC"]
    opacities = [.8,.9,.6,.7,.8,.9,.6,.7,.8,.9,.6,.7]
    
    y_values = list(range(200, 1301, 100))
    
    for i in range(len(y_values)):
        if i < 2:
            fillcolor_index = 0
        elif i < 6:
            fillcolor_index = 1
        elif i < 10:
            fillcolor_index = 2
        else:
            fillcolor_index = 3
        
        fig.add_shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=y_values[i],
            x1=1,
            y1=y_values[i]+100,
            fillcolor=colors[fillcolor_index],
            line=dict(width=0),
            opacity=opacities[i],
            layer="below"
        )
        
    fig.update_layout(width=1536, height=864)
    fig.update_layout(xaxis_title="GameId", yaxis_title="TotalLp", title_text="Ranked Climb to Masters!")
    fig.update_layout(
        plot_bgcolor="#333333",
        paper_bgcolor="#333333",
        font_color="#FFFFFF",
        yaxis=dict(tickmode="linear", dtick=100)
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
        maxX = 50
        maxY = 400

        maxLoss = 0
        maxWin = 0

        markerColors = [winColor]
        sizes = [2]

        prevY = 0
        prevColor = defaultColor
        currentSize = 5.0
        currentStreak = 1.0

        for row in reader:
            x = int(row[0])
            y = int(row[13])

            #if(x>836):
            #    break
            #if(x>1242):
            #    break
            if prevY !=0:
                if row[12] == 'True':
                    if prevColor == winColor:
                        currentStreak+=.5
                    else:
                        currentStreak=1
                    markerColors.append(winColor)
                    sizes.append(currentSize*currentStreak)
                    prevColor = winColor
                    if currentStreak>maxWin:
                        maxWin=currentStreak
                else:
                    if prevColor == loseColor:
                        currentStreak+=.5
                    else:
                        currentStreak=1
                    markerColors.append(loseColor)
                    sizes.append(currentSize*currentStreak)
                    prevColor = loseColor
                    if currentStreak>maxLoss:
                        maxLoss=currentStreak

            prevY = y
            if x < minX:
                minX = x-1
            elif x > maxX:
                maxX = x+1
            if y < (minY-10):
                minY = y-20
            elif y > (maxY-10):
                maxY = y+20
            #Move drop old X axis values 
            if maxY-minY>600:
                minY = maxY-600
            if maxX-minX>150:
                minX = maxX-150

            x_values.append(x)
            y_values.append(y)
            frames.append(go.Frame(
                data=[go.Scatter(
                    x=x_values, y=y_values, 
                    mode='lines+markers', 
                    name='main',
                    showlegend=False,
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
        updatemenus=[dict(
            buttons = [dict(
                args = [None, {
                    "frame": {
                        "duration": 110, 
                        "redraw": True},
                    "fromcurrent": True, 
                    "transition": {
                        "duration": 80,  # duration of transition in ms
                        "easing": "linear"  # easing function for transition
                        }
                    }],
                label = "Play",
                method = "animate")],
        type='buttons',
        showactive=False,
        y=1,
        x=1,
        xanchor='right',
        yanchor='bottom')])
    
    # Display the plot
    fig.show()