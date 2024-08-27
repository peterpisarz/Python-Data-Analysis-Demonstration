import os
import json
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

# Initialize the app
app = Dash(__name__)

# Directory where JSON files are stored
directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine_runs')


# Function to retrieve available engine runs
def get_engine_runs():
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    return sorted([int(f.split('_')[2].split('.')[0]) for f in files])


# Function to load data from a selected engine run
def load_run_data(run_number):
    file_name = f'engine_run_{run_number}.json'
    file_path = os.path.join(directory, file_name)

    with open(file_path, 'r') as f:
        engine_run_data = json.load(f)

    return pd.DataFrame(engine_run_data["Data"])


# Layout of the app
app.layout = html.Div([
    html.H1("Engine Run Data Visualization", style={'textAlign': 'center', 'marginBottom': '30px'}),

    # Main container
    html.Div([
        # Container for dropdown and checklist
        html.Div([
            dcc.Dropdown(
                id='engine-run-dropdown',
                options=[{'label': f'Engine Run {i}', 'value': i} for i in get_engine_runs()],
                value=get_engine_runs()[0],  # Default value
                clearable=False,
                style={'marginBottom': '20px'}
            ),
            html.Div("Select Parameters:", style={'fontWeight': 'bold', 'marginBottom': '10px'}),
            dcc.Checklist(
                id='parameter-checklist',
                options=[
                    {'label': 'RPM', 'value': 'RPM'},
                    {'label': 'Battery Voltage (V)', 'value': 'Battery Voltage (V)'},
                    {'label': 'Fuel Consumption (GPM)', 'value': 'Fuel Consumption (GPM)'},
                    {'label': 'Engine Temperature (°F)', 'value': 'Engine Temperature (°F)'},
                    {'label': 'Throttle Position (%)', 'value': 'Throttle Position (%)'},
                    {'label': 'Oil Pressure (psi)', 'value': 'Oil Pressure (psi)'}
                ],
                value=['RPM'],  # Default checked parameter
                style={'marginBottom': '20px'}
            )
        ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px',
                  'boxShadow': '2px 2px 10px #888888', 'borderRadius': '10px'}),

        # Container for the graph
        html.Div([
            dcc.Graph(id='engine-run-graph')
        ], style={'width': '70%', 'display': 'inline-block', 'padding': '20px', 'boxShadow': '2px 2px 10px #888888',
                  'borderRadius': '10px'})
    ], style={'display': 'flex', 'justifyContent': 'space-around'})
])


# Callback to update the graph based on selected engine run and parameters
@app.callback(
    Output('engine-run-graph', 'figure'),
    [Input('engine-run-dropdown', 'value'),
     Input('parameter-checklist', 'value')]
)
def update_graph(selected_run, selected_params):
    # Load the data for the selected engine run
    df = load_run_data(selected_run)

    # Create the figure
    fig = go.Figure()

    # Add traces for each selected parameter
    for param in selected_params:
        fig.add_trace(go.Scatter(x=df['Time (s)'], y=df[param], mode='lines', name=param))

    # Update layout
    fig.update_layout(
        title=f"Engine Run {selected_run} Data",
        xaxis_title='Time (s)',
        yaxis_title='Value',
        template='plotly_dark',
        margin={'l': 50, 'r': 50, 't': 50, 'b': 50}
    )

    return fig


# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)