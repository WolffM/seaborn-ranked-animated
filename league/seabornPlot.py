import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.subplots as subplots
import csv

def createFig():
    fig = subplots.make_subplots()
    fig.update_layout(shapes=[
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=250,
            x1=1,
            y1=400,
            fillcolor='#ccba12', #gold
            opacity=0.7,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=400,
            x1=1,
            y1=800,
            fillcolor='#057853', #plat
            opacity=0.7,
            layer="below"
        ),
        go.layout.Shape(
            type='rect',
            xref='paper',
            yref='y',
            x0=0,
            y0=800,
            x1=1,
            y1=1200,
            fillcolor='#3239bf', #diamond
            opacity=0.7,
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
            fillcolor="#8d39a8", #master
            opacity=0.7,
            layer="below"
        )
    ])
    fig.update_layout(xaxis_title="GameId", yaxis_title="TotalLp", title_text="Ranked Climb to Masters!")
    fig.update_layout(
        plot_bgcolor="#333333", # Set the background color to dark grey
        paper_bgcolor="#333333", # Set the paper background color to dark grey
        font_color="#FFFFFF" # Set the font color to white
    )
    return fig
def makePlot(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        x_values = []
        y_values = []
        frames = []

        minX = 1000
        minY = 1000
        maxX = 10
        maxY = 400
        for row in reader:
            x = int(row[0])
            y = int(row[13])
            if x < minX:
                minX = x
            elif x > maxX:
                maxX = x
            if y < minY:
                minY = y
            elif y > maxY:
                maxY = y
            x_values.append(x)
            y_values.append(y)
            frames.append(go.Frame(data=[go.Scatter(x=x_values, y=y_values, 
                                                    mode='lines', 
                                                    name='lines', 
                                                    line=dict(color='#333333', width=5),
                                                    showlegend=True,
                                                    opacity=0.5),
                                         go.Scatter(x=x_values, y=y_values, 
                                                    mode='lines', 
                                                    name='lines',
                                                    showlegend=True,
                                                    line=dict(color='#ff0000', width=2))],
                                   layout=go.Layout(xaxis=dict(range=[minX, maxX]),
                                                    yaxis=dict(range=[minY, maxY]))))


    #This creates a fig background
    fig = createFig()
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
                                    args = [None, {"frame": {"duration": 50, 
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