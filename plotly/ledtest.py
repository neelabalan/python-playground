import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    daq.LEDDisplay(
        id='my-LED-display',
        label="color",
        color="#FF5E5E",
        backgroundColor="#000000",
        value=6
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
