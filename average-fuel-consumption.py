#!/usr/bin/env python3

'''
    Visualization of evolution of average fuel consumption of cars in Canada

    Portions of the code in this file have been generated with generate-country-fuel-consumption-plot-code.py
      - Generated code is marked with comments
      - Significant changes to these sections can be done by changing the generation script, running it, and manually
         copy-pasting the printed code into this file
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
avg_fuel_consumption = {}
filepath = Path('data/GFEI-C3-Average-fuel-consumption.csv')
years = []
with open(filepath, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip file header and column names
    for i in range(2):
        next(csv_reader)
    years = next(csv_reader)[1:]
    #print(years)

    for row in csv_reader:
        country_name = row[0]
        fuel_consumption = row[1:]

        # Skip empty lines
        if country_name == '':
            continue

        #print(country_name, fuel_consumption)
        avg_fuel_consumption[country_name] = fuel_consumption
#print(avg_fuel_consumption)

# Organize Canadian data for plotting
plotting_data = {}
for country in avg_fuel_consumption.keys():
    country_years = []
    country_fuel_consumption = []
    for i, year in enumerate(years):
        fuel_consumption = avg_fuel_consumption[country][i]
        if fuel_consumption != '':
            country_years.append(year)
            country_fuel_consumption.append(fuel_consumption)
    plotting_data[country] = {'years': country_years, 'fuel-consumption': country_fuel_consumption}
#print(plotting_data)

# Plot fuel consumption data
canada_color = 'rgb(192,0,0)'
grey_palette = ['#f7f7f7', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525']
grey_marker_color = grey_palette[2]
grey_marker_size = 5
background_grey_line_color = '#ededed'  # Not from the grey palette
text_color = grey_palette[4]

canadian_fuel_consumption = go.Scatter(
    x=plotting_data['Canada']['years'],
    y=plotting_data['Canada']['fuel-consumption'],
    mode='lines+markers',
    marker=dict(
        color=canada_color
    )
)

chinese_fuel_consumption = go.Scatter(
    x=plotting_data['China']['years'],
    y=plotting_data['China']['fuel-consumption'],
    mode='lines+markers',
    marker=dict(
        color=grey_marker_color,
        size=grey_marker_size
    )
)

german_fuel_consumption = go.Scatter(
    x=plotting_data['Germany']['years'],
    y=plotting_data['Germany']['fuel-consumption'],
    mode='lines+markers',
    marker=dict(
        color=grey_marker_color,
        size=grey_marker_size
    )
)

us_fuel_consumption = go.Scatter(
    x=plotting_data['United States']['years'],
    y=plotting_data['United States']['fuel-consumption'],
    mode='lines+markers',
    marker=dict(
        color=grey_marker_color,
        size=grey_marker_size
    )
)

# Code for scatter plots below is generated with generate-country-fuel-consumption-plot-code.py
argentina_fuel_consumption = go.Scatter(
    x=plotting_data['Argentina']['years'],
    y=plotting_data['Argentina']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

australia_fuel_consumption = go.Scatter(
    x=plotting_data['Australia']['years'],
    y=plotting_data['Australia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

austria_fuel_consumption = go.Scatter(
    x=plotting_data['Austria']['years'],
    y=plotting_data['Austria']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

belgium_fuel_consumption = go.Scatter(
    x=plotting_data['Belgium']['years'],
    y=plotting_data['Belgium']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

brazil_fuel_consumption = go.Scatter(
    x=plotting_data['Brazil']['years'],
    y=plotting_data['Brazil']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

bulgaria_fuel_consumption = go.Scatter(
    x=plotting_data['Bulgaria']['years'],
    y=plotting_data['Bulgaria']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

chile_fuel_consumption = go.Scatter(
    x=plotting_data['Chile']['years'],
    y=plotting_data['Chile']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

croatia_fuel_consumption = go.Scatter(
    x=plotting_data['Croatia']['years'],
    y=plotting_data['Croatia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

cyprus_fuel_consumption = go.Scatter(
    x=plotting_data['Cyprus']['years'],
    y=plotting_data['Cyprus']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

czechrepublic_fuel_consumption = go.Scatter(
    x=plotting_data['Czech Republic']['years'],
    y=plotting_data['Czech Republic']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

denmark_fuel_consumption = go.Scatter(
    x=plotting_data['Denmark']['years'],
    y=plotting_data['Denmark']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

egypt_fuel_consumption = go.Scatter(
    x=plotting_data['Egypt']['years'],
    y=plotting_data['Egypt']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

estonia_fuel_consumption = go.Scatter(
    x=plotting_data['Estonia']['years'],
    y=plotting_data['Estonia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

finland_fuel_consumption = go.Scatter(
    x=plotting_data['Finland']['years'],
    y=plotting_data['Finland']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

france_fuel_consumption = go.Scatter(
    x=plotting_data['France']['years'],
    y=plotting_data['France']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

greece_fuel_consumption = go.Scatter(
    x=plotting_data['Greece']['years'],
    y=plotting_data['Greece']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

hungary_fuel_consumption = go.Scatter(
    x=plotting_data['Hungary']['years'],
    y=plotting_data['Hungary']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

iceland_fuel_consumption = go.Scatter(
    x=plotting_data['Iceland']['years'],
    y=plotting_data['Iceland']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

india_fuel_consumption = go.Scatter(
    x=plotting_data['India']['years'],
    y=plotting_data['India']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

indonesia_fuel_consumption = go.Scatter(
    x=plotting_data['Indonesia']['years'],
    y=plotting_data['Indonesia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

ireland_fuel_consumption = go.Scatter(
    x=plotting_data['Ireland']['years'],
    y=plotting_data['Ireland']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

italy_fuel_consumption = go.Scatter(
    x=plotting_data['Italy']['years'],
    y=plotting_data['Italy']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

japan_fuel_consumption = go.Scatter(
    x=plotting_data['Japan']['years'],
    y=plotting_data['Japan']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

korea_fuel_consumption = go.Scatter(
    x=plotting_data['Korea']['years'],
    y=plotting_data['Korea']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

latvia_fuel_consumption = go.Scatter(
    x=plotting_data['Latvia']['years'],
    y=plotting_data['Latvia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

lithuania_fuel_consumption = go.Scatter(
    x=plotting_data['Lithuania']['years'],
    y=plotting_data['Lithuania']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

luxembourg_fuel_consumption = go.Scatter(
    x=plotting_data['Luxembourg']['years'],
    y=plotting_data['Luxembourg']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

macedonia_fuel_consumption = go.Scatter(
    x=plotting_data['Macedonia']['years'],
    y=plotting_data['Macedonia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

malaysia_fuel_consumption = go.Scatter(
    x=plotting_data['Malaysia']['years'],
    y=plotting_data['Malaysia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

malta_fuel_consumption = go.Scatter(
    x=plotting_data['Malta']['years'],
    y=plotting_data['Malta']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

mexico_fuel_consumption = go.Scatter(
    x=plotting_data['Mexico']['years'],
    y=plotting_data['Mexico']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

netherlands_fuel_consumption = go.Scatter(
    x=plotting_data['Netherlands']['years'],
    y=plotting_data['Netherlands']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

norway_fuel_consumption = go.Scatter(
    x=plotting_data['Norway']['years'],
    y=plotting_data['Norway']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

peru_fuel_consumption = go.Scatter(
    x=plotting_data['Peru']['years'],
    y=plotting_data['Peru']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

philippines_fuel_consumption = go.Scatter(
    x=plotting_data['Philippines']['years'],
    y=plotting_data['Philippines']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

poland_fuel_consumption = go.Scatter(
    x=plotting_data['Poland']['years'],
    y=plotting_data['Poland']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

portugal_fuel_consumption = go.Scatter(
    x=plotting_data['Portugal']['years'],
    y=plotting_data['Portugal']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

romania_fuel_consumption = go.Scatter(
    x=plotting_data['Romania']['years'],
    y=plotting_data['Romania']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

russianfederation_fuel_consumption = go.Scatter(
    x=plotting_data['Russian Federation']['years'],
    y=plotting_data['Russian Federation']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

slovakia_fuel_consumption = go.Scatter(
    x=plotting_data['Slovakia']['years'],
    y=plotting_data['Slovakia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

slovenia_fuel_consumption = go.Scatter(
    x=plotting_data['Slovenia']['years'],
    y=plotting_data['Slovenia']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

southafrica_fuel_consumption = go.Scatter(
    x=plotting_data['South Africa']['years'],
    y=plotting_data['South Africa']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

spain_fuel_consumption = go.Scatter(
    x=plotting_data['Spain']['years'],
    y=plotting_data['Spain']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

sweden_fuel_consumption = go.Scatter(
    x=plotting_data['Sweden']['years'],
    y=plotting_data['Sweden']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

switzerland_fuel_consumption = go.Scatter(
    x=plotting_data['Switzerland']['years'],
    y=plotting_data['Switzerland']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

thailand_fuel_consumption = go.Scatter(
    x=plotting_data['Thailand']['years'],
    y=plotting_data['Thailand']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

turkey_fuel_consumption = go.Scatter(
    x=plotting_data['Turkey']['years'],
    y=plotting_data['Turkey']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

ukraine_fuel_consumption = go.Scatter(
    x=plotting_data['Ukraine']['years'],
    y=plotting_data['Ukraine']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

unitedkingdom_fuel_consumption = go.Scatter(
    x=plotting_data['United Kingdom']['years'],
    y=plotting_data['United Kingdom']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)

data = [  # Start of generated names
    argentina_fuel_consumption,
    australia_fuel_consumption,
    austria_fuel_consumption,
    belgium_fuel_consumption,
    brazil_fuel_consumption,
    bulgaria_fuel_consumption,
    chile_fuel_consumption,
    croatia_fuel_consumption,
    cyprus_fuel_consumption,
    czechrepublic_fuel_consumption,
    denmark_fuel_consumption,
    egypt_fuel_consumption,
    estonia_fuel_consumption,
    finland_fuel_consumption,
    france_fuel_consumption,
    greece_fuel_consumption,
    hungary_fuel_consumption,
    iceland_fuel_consumption,
    india_fuel_consumption,
    indonesia_fuel_consumption,
    ireland_fuel_consumption,
    italy_fuel_consumption,
    japan_fuel_consumption,
    korea_fuel_consumption,
    latvia_fuel_consumption,
    lithuania_fuel_consumption,
    luxembourg_fuel_consumption,
    macedonia_fuel_consumption,
    malaysia_fuel_consumption,
    malta_fuel_consumption,
    mexico_fuel_consumption,
    netherlands_fuel_consumption,
    norway_fuel_consumption,
    peru_fuel_consumption,
    philippines_fuel_consumption,
    poland_fuel_consumption,
    portugal_fuel_consumption,
    romania_fuel_consumption,
    russianfederation_fuel_consumption,
    slovakia_fuel_consumption,
    slovenia_fuel_consumption,
    southafrica_fuel_consumption,
    spain_fuel_consumption,
    sweden_fuel_consumption,
    switzerland_fuel_consumption,
    thailand_fuel_consumption,
    turkey_fuel_consumption,
    ukraine_fuel_consumption,
    unitedkingdom_fuel_consumption,  # End of generated names
    us_fuel_consumption,
    german_fuel_consumption,
    chinese_fuel_consumption,
    canadian_fuel_consumption]

axis_color = grey_palette[3]
gridline_color = grey_palette[0]
grey_annotation_color = grey_palette[3]
line_label_x = 1.06
layout = go.Layout(
    font=dict(
        family='Akzidenz-Grotesk BQ'  # Can be replaced with any font installed on computer
    ),
    plot_bgcolor='#ffffff',
    xaxis=go.layout.XAxis(
        tickvals=['2005', '', '2007', '', '2009', '', '2011', '', '2013', '', '2015', '', '2017'],
        showgrid=True,
        gridcolor=gridline_color,
        showline=False,
        tickfont=dict(
            color=axis_color
        ),
        ticklen=6,
        tickcolor='#ffffff'
    ),
    yaxis=go.layout.YAxis(
        range=[2, 11.5],
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
        text='Canadian car fuel consumption has stopped decreasing',
        xref='paper',
        x=0,
        font=dict(
            size=18,
            color=grey_palette[5]
        )
    ),
    # Annotation position is specified manually
    annotations=[dict(
        text="Average litres of gasoline-equivalent per 100 km (L / 100 km)",
        font=dict(
            size=13,
            color=grey_palette[2],
        ),
        showarrow=False,
        x=0,
        y=1.1275,
        xref='paper',
        yref='paper',
    ), dict(
        text="Canada",
        font=dict(
            size=13,
            color=canada_color,
        ),
        showarrow=False,
        x=line_label_x,
        y=0.77,
        xref='paper',
        yref='paper',
    ), dict(
        text="US",
        font=dict(
            size=13,
            color=grey_annotation_color,
        ),
        showarrow=False,
        x=line_label_x - 0.053,
        y=0.72,
        xref='paper',
        yref='paper',
    ), dict(
        text="China",
        font=dict(
            size=13,
            color=grey_annotation_color,
        ),
        showarrow=False,
        x=line_label_x - 0.02,
        y=0.595,
        xref='paper',
        yref='paper',
    ), dict(
        text="Germany",
        font=dict(
            size=13,
            color=grey_annotation_color,
        ),
        showarrow=False,
        x=line_label_x + 0.02,
        y=0.42,
        xref='paper',
        yref='paper',
    )]
)

fig = go.Figure(data=data, layout=layout)
# Windows style filepaths (change if necessary)
image_filepath = 'graphs\\avg-fuel-consumption-canada.png'
pio.write_image(fig, file=image_filepath, format='png')

# For exporting to pdf
#image_filepath = 'graphs\\avg-fuel-consumption-canada.pdf'
#pio.write_image(fig, file=image_filepath, format='pdf')