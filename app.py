import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages.sub_page3a import layout as sub_page3a_layout, register_callbacks as register_sub_page3a_callbacks
from pages.sub_page3b import layout as sub_page3b_layout, register_callbacks as register_sub_page3b_callbacks
from pages.page3 import index_layout as page3_layout
from pages.page1 import layout as page1_layout
from pages.sub_page1a import layout as sub_page1a_layout, register_callbacks as register_sub_page1a_callbacks
from pages.page2 import layout as page2_layout
from pages.sub_page2a import layout as sub_page2a_layout,register_callbacks as register_sub_page2a_callbacks

# Create the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# Define the main layout of the app
app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(
            dbc.Col(
                html.Header(
                    html.H1("Unlimited Analysis", className="text-center my-4"),
                    className="header"
                )
            )
        ),
        html.Div(id="page-content")  # Content area for the different pages
    ],
    fluid=True
)

# Define the home layout with thumbnails
home_layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col(html.H1("Welcome to my Dashboard", className="display-3 text-center"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.P(
                "Select below to navigate to the respective analysis.",
                className="lead text-center"
            ), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.Hr(className="my-2"), width=12)
        ]),
        dbc.Row([
            dbc.Col(html.P("Explore the various sections of the dashboard.", className="text-center"), width=12)
        ]),
        html.Div(
            className="container",
            children=[
                html.Div(
                    className="thumbnail m-2",
                    children=[
                        html.A([
                            html.Img(src='/assets/weather_thumbnail.webp', className='thumbnail-img'),
                            html.Span("Weather Analysis", className='thumbnail-text')
                        ], href="/page1")
                    ]
                ),
                html.Div(
                    className="thumbnail m-2",
                    children=[
                        html.A([
                            html.Img(src='/assets/image_detection_thumbnail.webp', className='thumbnail-img'),
                            html.Span("Image Detection Project", className='thumbnail-text')
                        ], href="/page2")
                    ]
                ),
                html.Div(
                    className="thumbnail m-2",
                    children=[
                        html.A([
                            html.Img(src='/assets/forest_fire_thumbnail.webp', className='thumbnail-img'),
                            html.Span("Fire Hazard Analysis", className='thumbnail-text')
                        ], href="/page3")
                    ]
                ),
                # Additional thumbnails for future pages...
            ]
        )
    ],
    fluid=True
)

# Define a callback to update the content based on the URL
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/page1":
        return page1_layout
    elif pathname == "/sub_page1a":
        return sub_page1a_layout
    elif pathname == "/page2":
        return page2_layout
    elif pathname == "/sub_page2a":
        return sub_page2a_layout
    elif pathname == "/page3":
        return page3_layout
    elif pathname == "/sub_page3a":
        return sub_page3a_layout
    elif pathname == "/sub_page3b":
        return sub_page3b_layout
    else:
        return home_layout

# Register callbacks for the sub-pages
register_sub_page3a_callbacks(app)
register_sub_page3b_callbacks(app)
register_sub_page1a_callbacks(app)
register_sub_page2a_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
