from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

DATA_PATH = "./formatted_data.csv"

# load the formatted data
df = pd.read_csv(DATA_PATH, parse_dates=[1])
# sort the data by date
df = df.sort_values(by="date")

# Dash Application
app = Dash(__name__)

# Create the line chart
line_chart = px.line(df \
                     , x="date" \
                     , y="sales" \
                     , title="Pink Morsels Sales" \
                     ,)

# create the visualization
visualization = dcc.Graph(
        id='visulaization',
        figure=line_chart,
    )

# markdown text
markdown_text = '''
        The following graph(line chart) is plot of **Pink Morsels sales** from **2018-02-06 to 2022-02-14**.
        The original purpose of the Dash app — the goal is to answer **Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”**
    '''

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Visualizer',
             id="header", 
             style={"fontSize": "48px", "color": "pink"},
            ),

    dcc.Markdown(children=markdown_text),

    visualization
    
])



if __name__ == '__main__':
    app.run_server()