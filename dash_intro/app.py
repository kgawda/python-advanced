from numbers import Number
from dash import (
    Dash,
    html,
    dcc,
    Input,
    Output,
    State,
    callback_context,
    no_update,
    set_props,
    Patch,
    ALL,
    MATCH,
    ALLSMALLER
)
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
    html.Div([
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
        dcc.Input(id="username", value="user"),
        html.Button(
            "Set title",
            n_clicks=0,
            id="button-set-title",
        ),
        dcc.Store(
            id="controls-store"
        ),
    ]),
    html.Div([
        html.Div([
            html.Button(
                "Click me",
                style={"width": 50, "height": 50},
                id={"type": "game-button", "index": x * 100 + y},
            ) for x in range(3)
        ]) for y in range(3)
    ]),
    dcc.Graph(
        style={"height": "80vh"},
        id="main-graph",
    )
])


# @app.callback(
#     Input({"type": "game-button", "index": ALL}, "n_clicks")
# )
# def update_game(n_clickss):
#     print(n_clickss, callback_context.triggered_id)

@app.callback(
    Output({"type": "game-button", "index": MATCH}, "style"),
    Input({"type": "game-button", "index": MATCH}, "n_clicks"),
    # Input({"type": "game-button", "index": ALLSMALLER}, "n_clicks"),
    # State({"type": "game-button", "index": ALLSMALLER}, "n_clicks"),
    # State({"type": "game-button", "index": ALL}, "n_clicks"),
    State({"type": "game-button", "index": MATCH}, "id"),
    prevent_initial_call=True,
)
def update_game2(n_clicks, id):
    # callback_context.triggered_id zazwyczaj == id
    return {"color": "red"}

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
        # return no_update, no_update, no_update
    
    return plot_parameter, plot_parameter, plot_parameter


@app.callback(
    Output("main-graph", "figure"),
    Input("controls-store", "data"),
    State("username", "value"),
)
def update_plot(control_data, username):
    fig = build_figure(control_data)
    fig.update_layout({"title": "Plot for " + str(username)}, overwrite="True")
    return fig

    # patched_fig = Patch()
    # patched_fig["data"][0]["y"] = [2+control_data, 3+control_data, 4+control_data, 5+control_data, 6+control_data]
    # return patched_fig
    # (uwaga: musi być napierw stworzony figure)



@app.callback(
    Output("site-title", "children"),
    Input("button-set-title", "n_clicks"),
    State("username", "value"),
)
def set_site_title(n_clicks, username):
    print(repr(n_clicks))
    set_props("button-set-title", {"children": f"Change name from {username}"})
    return f"Hello {username}!"



if __name__ == "__main__":
    app.run_server(debug=True)
