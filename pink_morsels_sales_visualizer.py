from dash import Dash, html, dcc, callback, Output, Input
from plotly.express import line
import pandas as pd

DATA_PATH = "./formatted_data.csv"

# load the formatted data
df = pd.read_csv(DATA_PATH, parse_dates=[1])
# sort the data by date
df = df.sort_values(by="date")

# Dash Application
app = Dash(__name__)

REGIONS = ["north", "east", "south", "west", "all"]

COLOURS = {
    "background" : "#FEDBFF",
    "text"		 : "#522A61",
    "background-dark" : "#D598EB"
}

# COLOURS = ["#FEDBFF", "#D598EB", "#522A61"]

def generate_chart(data: pd.DataFrame) -> line:
    """
    Generates line chart from the given data frame
    """
    line_chart = line(data,
                    x="date",
                    y="sales",
                    title="Pink Morsels Sales")
    line_chart.update_layout(
        plot_bgcolor=COLOURS["background-dark"],
        paper_bgcolor=COLOURS["background"],
        font_color=COLOURS["text"]
    )
    
    return line_chart

# create the visualization
visualization = dcc.Graph(
        id='visulaization',
        figure=generate_chart(df),
)

# header
header = html.H1(children='Pink Morsels Sales Visualizer',
             id="header", 
             style={
                 'background-color': COLOURS["background-dark"],
                 'color' : COLOURS["text"],
                 'border-radius' : '20px'
			 },
)

# markdown text
markdown_text = dcc.Markdown(
    children=[
        '''
        The following graph(line chart) is plot of **Pink Morsels sales** from **2018-02-06 to 2022-02-14**.
        The original purpose of the Dash app — the goal is to answer **Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?”**
    	'''
	]
)

markdown_text_div = html.Div(
    [
        markdown_text
	],
    style={
        'color' : COLOURS["text"],
        'background-color' : COLOURS["background"]
	}
)

# radio buttons
region_selector = dcc.RadioItems(
    REGIONS,
    REGIONS[0],
    id="region_selector",
    inline=True
)

# region selector
region_selector_div = html.Div(
    [
        region_selector
	],
    style={
        "font-size": "135%",
        "color" : COLOURS["text"],
        "background-color" : "inherit"
	}
)

@callback(
    Output(visualization, "figure"),
    Input(region_selector, "value")
)
def update_graph(region:str) -> line:
    """
    Updates the plot based on the spcified region
    """
    if region == REGIONS[-1]:
        return generate_chart(df)
    else:
        return generate_chart(df[df["region"] == region])



app.layout = html.Div(children=[
    header,
    markdown_text_div,
    visualization, 
    region_selector_div
    ],
    style={
        "textAlign": "center",
        "background-color": COLOURS["background"],
        "border-radius": "20px"
    }
)



if __name__ == '__main__':
    app.run_server()