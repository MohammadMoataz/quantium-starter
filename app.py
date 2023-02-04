import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("data/final.csv")

app.layout = html.Div([
	html.H1("Impact of pink morsel's price increase on overall sales.", className='header'),
	dcc.Graph(id='pink_morsel_sales'),
	dcc.RadioItems(
		['All', 'north', 'south', 'east', 'west'], 'All', id='regions',
		className='options', inline=False)])

@app.callback(
	Output('pink_morsel_sales', 'figure'),
	Input('regions', 'value')
)
def show_region(selected_region):
	if selected_region == 'All':
		fig = px.line(
			df, x='date', y='sales',
			title="Pink Morsel sales", color='region',markers=True,
			range_x=['2021-01-01', '2021-02-01'])
	else:
		filtered_df = df[df.region == selected_region]

		fig = px.line(
			filtered_df, x='date', y='sales',
			title="Pink Morsel sales", markers=True,
			range_x=['2021-01-01', '2021-02-01'])

	return fig


if __name__ == "__main__":
	app.run_server(debug=True)