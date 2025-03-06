from dash import Dash, html, dcc, Input, Output
from plotly import graph_objects as go


app = Dash(__name__)

# Layout > Graph > Figure > Trace

def build_figure(constant=0):
    fig = go.Figure([
        go.Bar(
            y=[1, 2, 3, 4, 5],
            hovertemplate="TEST<br>Value is <b>%{y}</b>"
        ),
        go.Bar(y=[5+constant, 4+constant, 2+constant, 2+constant, 1+constant],),
        ],
        layout={"title": "Przykład1"},
    )
    fig.update_layout({"title": "Przykład"})  # nadpisanie ustawień z fig.layout
    return fig


app.layout = html.Div([
    html.H1("Hello Dash!", id="site-title"),
    html.A("Visit example.com", href="https://example.com"),
    dcc.Slider(
        0,
        10,
        value=10,
        id="plot-variation-slider",
    ),
    dcc.Graph(
        style={"height": "100vh"},
        id="main-graph"
    )
])


@app.callback(
    Output("main-graph", "figure"),
    Input("plot-variation-slider", "value"),
    # prevent_initial_call=True,
)
def update_plot(slider_value):
    return build_figure(slider_value)


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)
