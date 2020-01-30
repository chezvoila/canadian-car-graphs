#!/usr/bin/env python3

'''
    Visualization of average fuel consumption vs fuel prices
'''

from pathlib import Path
import csv

# Installing plotly: https://plot.ly/python/getting-started/
import plotly.graph_objs as go
import plotly.io as pio

# This code uses static image export (e.g. png, pdf) and requires additional dependencies: https://plot.ly/python/static-image-export/
# Path to orca executable
pio.orca.config.executable = # Write path to orca executable here (e.g. '[...]/orca/orca.exe')

# Read, select, and organize data
country_data = {}
fuel_consumption_filepath = Path('data/GFEI-C3-Average-fuel-consumption.csv')
years = []
with open(fuel_consumption_filepath, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip file header and column names (in the future delete these in the original file before processing)
    for i in range(2):
        next(csv_reader)
    years = next(csv_reader)[1:]
    #print(years)

    for row in csv_reader:
        country_name = row[0]
        fuel_consumption_2016 = row[-2]

        # Skip empty lines (in the future delete these up in the original file before processing)
        if country_name == '':
            continue

        #print(country_name, fuel_consumption)
        country_data[country_name] = {'fuel-consumption': fuel_consumption_2016}
#print(country_data)

pump_price_filepath = Path('data/WorldBank-Pump-Price-Gasoline-USD-per-litre.csv')
with open(pump_price_filepath, 'r') as file:
    csv_reader = csv.reader(file)

    years = next(csv_reader)[4:-1]  # There are 4 ID columns at the beginning and a blank column at the end
    #print(years)

    for row in csv_reader:
        country_name = row[0]

        if country_name in country_data.keys():
            pump_price_2016 = row[-5]  # 2016 data is 5 from the end
            #print(country_name, pump_price_2016)
            country_data[country_name] = {'fuel-consumption': country_data[country_name]['fuel-consumption'],
                                          'pump-price': pump_price_2016}
#print(country_data)

# Remove countries that don't have both data dimensions (missing pump price)
countries_to_remove = []
for country_name in country_data.keys():
    try:
        pump_price_2016 = country_data[country_name]['pump-price']
    except KeyError:
        countries_to_remove.append(country_name)
        #print(country_name)

for country_name in countries_to_remove:
    #print('Removing', country_name, ': No pump price')
    del country_data[country_name]
#print(country_data)

# Separate data points that will be labeled
countries_to_label = ['Canada', 'United States', 'Malaysia', 'India', 'Germany', 'Portugal', 'Iceland', 'Argentina']
label_positions = ['top right', 'top left', 'top right', 'top left', 'top left', 'bottom right', 'top right', 'top right']
labelled_country_data = {}
for country in countries_to_label:
    labelled_country_data[country] = country_data.pop(country)
unlabelled_country_data = country_data
#print(labelled_country_data)
#print(unlabelled_country_data)

canada_color = '#c00000'
grey_palette = ['#f7f7f7', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525']
number_of_grey_points = len(countries_to_label)-1
grey_point_colors = [grey_palette[4]] * number_of_grey_points
labelled_point_colors = [canada_color] + grey_point_colors
#print(labelled_point_colors)

# Organize data for plotting
labelled_fuel_consumptions_2016 = []
labelled_pump_prices_2016 = []
for country_name in labelled_country_data.keys():
    labelled_fuel_consumptions_2016.append(labelled_country_data[country_name]['fuel-consumption'])
    labelled_pump_prices_2016.append(labelled_country_data[country_name]['pump-price'])
#print(labelled_fuel_consumptions_2016)
#print(labelled_pump_prices_2016)

unlabelled_fuel_consumptions_2016 = []
unlabelled_pump_prices_2016 = []
for country_name in unlabelled_country_data.keys():
    unlabelled_fuel_consumptions_2016.append(unlabelled_country_data[country_name]['fuel-consumption'])
    unlabelled_pump_prices_2016.append(unlabelled_country_data[country_name]['pump-price'])
#print(unlabelled_fuel_consumptions_2016)
#print(unlabelled_pump_prices_2016)

# Plot fuel consumption based on pump price
labelled_points = go.Scatter(
    x=labelled_pump_prices_2016,
    y=labelled_fuel_consumptions_2016,
    mode='markers+text',
    marker_color=labelled_point_colors,
    text=list(labelled_country_data.keys()),
    textposition=label_positions
)

unlabelled_points = go.Scatter(
    x=unlabelled_pump_prices_2016,
    y=unlabelled_fuel_consumptions_2016,
    mode='markers',
    marker_color=grey_palette[2]
)

axis_color = grey_palette[3]
gridline_color = grey_palette[0]
layout = go.Layout(
    font=dict(
        family='Akzidenz-Grotesk BQ'  # Can be replaced with any font installed on computer
    ),
    plot_bgcolor='#ffffff',
    xaxis=go.layout.XAxis(
        showgrid=True,
        gridcolor=gridline_color,
        showline=False,
        tickfont=dict(
            color=axis_color
        ),
        ticklen=4,
        tickcolor='#ffffff'
    ),
    yaxis=go.layout.YAxis(
        showgrid=True,
        gridcolor=gridline_color,
        showline=False,
        tickfont=dict(
            color=axis_color
        ),
        ticklen=4,
        tickcolor='#ffffff'
    ),
    showlegend=False,
    title=go.layout.Title(
        text='Cars tend to be more fuel efficient in countries where gas costs more',
        xref='paper',
        x=0,
        font=dict(
            size=18,
            color=grey_palette[5]
        )
    ),
    annotations=[dict(
        text='Canadians and Americans pay less for their gas and their cars use more',
        font=dict(
            size=13,
            color=grey_palette[2],
        ),
        showarrow=False,
        x=0,
        y=1.1275,
        xref='paper',
        yref='paper',
    )]
)

data = [unlabelled_points, labelled_points]

fig = go.Figure(data=data, layout=layout)
# Windows style filepaths (change if necessary)
image_filepath = 'graphs\\fuel-consumption-vs-price.png'
pio.write_image(fig, file=image_filepath, format='png')

# For exporting to pdf
#image_filepath = 'graphs\\fuel-consumption-vs-price.pdf'
#pio.write_image(fig, file=image_filepath, format='pdf')