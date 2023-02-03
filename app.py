import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("data/final.csv")

fig = px.line(
    df, x='date', y='sales',
	title="Soul Foods's total sales", color='region', markers=True,
	range_x=['2021-01-01', '2021-02-01'])

app.layout = html.Div([
	html.H1("Impact of pink morsel's price increase on overall sales."),
	dcc.Graph(id='price_impact_on_sales', figure=fig)])

if __name__ == "__main__":
    app.run_server(debug=True)