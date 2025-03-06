from numbers import Number
from dash import Dash, html, dcc, Input, Output, State, callback_context
from dash.exceptions import PreventUpdate
from plotly import graph_objects as go


app = Dash(__name__)

# Layout > Graph > Figure > Trace

def build_figure(constant=0):
    fig = go.Figure([
        go.Bar(
            y=[1, 2, 3, 4, 5],
            hovertemplate="TEST<br>Value is <b>%{y}</b>",
        ),
        go.Bar(y=[5+constant, 4+constant, 2+constant, 2+constant, 1+constant],),
        ],
        # layout={"title": "Przykład1"},
    )
    # fig.update_layout({"title": "Przykład"})  # nadpisanie ustawień z fig.layout
    fig.update_layout(transition_duration=200)
    return fig


app.layout = html.Div([
    html.H1("Hello Dash!", id="site-title"),
    html.A("Visit example.com", href="https://example.com"),
    dcc.Slider(
        0,
        10,
        value=10,
        step=1,
        updatemode="drag",
        id="plot-variation-slider",
    ),
    dcc.Input(
        type='number',
        value=10,
        id="plot-variation-input",
    ),
    dcc.Input(id="username"),
    dcc.Store(
        id="controls-store"
    ),
    dcc.Graph(
        style={"height": "80vh"},
        id="main-graph"
    )
])


@app.callback(
    Output("controls-store", "data"),
    Output("plot-variation-slider", "value"),
    Output("plot-variation-input", "value"),
    Input("plot-variation-slider", "value"),
    Input("plot-variation-input", "value"),
    # prevent_initial_call=True,
)
def update_controls(slider_value, input_value):
    if callback_context.triggered_id == "plot-variation-slider":
        plot_parameter = slider_value
    elif callback_context.triggered_id == "plot-variation-input":
        plot_parameter = input_value
    else:
        plot_parameter = slider_value

    if not isinstance(plot_parameter, Number):
        raise PreventUpdate()
    
    return plot_parameter, plot_parameter, plot_parameter


@app.callback(
    Output("main-graph", "figure"),
    Input("controls-store", "data"),
    State("username", "value"),
)
def update_plot(control_data, username):
    print(repr(username))
    fig = build_figure(control_data)
    fig.update_layout({"title": "Plot for " + str(username)}, overwrite="True")
    return fig


if __name__ == "__main__":
    app.run_server()
