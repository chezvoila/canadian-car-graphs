#!/usr/bin/env python3

'''
    Visualization of average co2 emissions per km for vehicles by country (2017)
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
avg_car_co2_emissions_2017 = {}
filepath = Path('data/GFEI-C2-Average-CO2-emissions-per-km.csv')
with open(filepath, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip file header and column names
    for i in range(3):
        next(csv_reader)

    for row in csv_reader:
        country_name = row[0]
        average_emissions_2017 = row[-1]

        # Skip empty lines and missing data points
        if average_emissions_2017 == '':
            continue

        #print(country_name, average_emissions_2017)
        avg_car_co2_emissions_2017[country_name] = int(average_emissions_2017.strip())
#print(avg_car_co2_emissions_2017)

# Sort countries as a function of their emissions
sorted_country_emissions = sorted(avg_car_co2_emissions_2017.items(), key=lambda country: country[1])
#print('sorted_country_emissions:', len(sorted_country_emissions), sorted_country_emissions)

# Organize data into layers for plotting
country_names = []
avg_car_co2_emissions_2017 = []
for country_data in sorted_country_emissions:
    country_name = country_data[0]
    country_names.append(country_name)
    avg_car_co2_emissions_2017.append(country_data[1])
#print(country_names)
#print(avg_car_co2_emissions_2017)

# Following functions from: https://bsou.io/posts/color-gradients-with-python
def RGB_to_hex(RGB):  # From: https://bsou.io/posts/color-gradients-with-python
  ''' [255,255,255] -> "#FFFFFF" '''
  # Components need to be integers for hex to make sense
  RGB = [int(x) for x in RGB]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])


def hex_to_RGB(hex):
  ''' "#FFFFFF" -> [255,255,255] '''
  # Pass 16 to the integer function for change of base
  return [int(hex[i:i+2], 16) for i in range(1,6,2)]


def color_dict(gradient):
  ''' Takes in a list of RGB sub-lists and returns dictionary of
    colors in RGB and hex form for use in a graphing function
    defined later on '''
  return {"hex":[RGB_to_hex(RGB) for RGB in gradient],
      "r":[RGB[0] for RGB in gradient],
      "g":[RGB[1] for RGB in gradient],
      "b":[RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
  ''' returns a gradient list of (n) colors between
    two hex colors. start_hex and finish_hex
    should be the full six-digit color string,
    inlcuding the number sign ("#FFFFFF") '''
  # Starting and ending colors in RGB form
  s = hex_to_RGB(start_hex)
  f = hex_to_RGB(finish_hex)
  # Initilize a list of the output colors with the starting color
  RGB_list = [s]
  # Calcuate a color at each evenly spaced value of t from 1 to n
  for t in range(1, n):
    # Interpolate RGB vector for color at the current value of t
    curr_vector = [
      int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
      for j in range(3)
    ]
    # Add it to our list of output colors
    RGB_list.append(curr_vector)

  return color_dict(RGB_list)


def polylinear_gradient(colors, n):
  ''' returns a list of colors forming linear gradients between
      all sequential pairs of colors. "n" specifies the total
      number of desired output colors '''
  # The number of colors per individual linear gradient
  n_out = int(float(n) / (len(colors) - 1))
  # returns dictionary defined by color_dict()
  gradient_dict = linear_gradient(colors[0], colors[1], n_out)

  if len(colors) > 1:
    for col in range(1, len(colors) - 1):
      next = linear_gradient(colors[col], colors[col+1], n_out)
      for k in ("hex", "r", "g", "b"):
        # Exclude first point to avoid duplicates
        gradient_dict[k] += next[k][1:]

  return gradient_dict
# End of code from: https://bsou.io/posts/color-gradients-with-python

# Generate gradient (yellow, orange, red)
number_bars_to_color_with_gradient = len(sorted_country_emissions)
smallest_bar_value = sorted_country_emissions[0][1]
number_color_gradations = 200 - smallest_bar_value  # 200 is a round number that is higher than the second highest bar
number_color_gradations += 3  # Hack: the polylinear gradient function below returns n-3 colors in this case
colors = [
    RGB_to_hex([254, 217, 118]),  # yellow
    RGB_to_hex([253, 141, 60]),  # orange
    RGB_to_hex([177, 0, 0])  # red
]
hex_gradient_colors = polylinear_gradient(colors=colors, n=number_color_gradations)['hex']
hex_gradient_colors = hex_gradient_colors[:-1]
#print(number_color_gradations, len(hex_gradient_colors), hex_gradient_colors)

# Determine bar color based on bar value
bar_colors = []
for idx, country_data in enumerate(sorted_country_emissions):
    if country_data[0] == 'Canada':
        bar_colors.append('#600000')  # Dark red for Canada
    else:
        bar_value = country_data[1]
        bar_color = hex_gradient_colors[bar_value-smallest_bar_value]
        #print(idx, country_data)
        bar_colors.append(bar_color)
#print('bar_colors:', len(bar_colors), bar_colors)

# Plot data
data = [go.Bar(
    x=avg_car_co2_emissions_2017,
    y=country_names,
    orientation='h',
    marker=dict(
        color=bar_colors
    )
)]

grey_palette = ['#f7f7f7', '#d9d9d9', '#bdbdbd', '#969696', '#737373', '#525252', '#252525']
layout = go.Layout(
    autosize=False,
    width=800,
    height=1000,
    margin=go.layout.Margin(
        l=150,
        r=50,
        b=100,
        t=110,
        pad=4
    ),
    font=dict(
        family='Akzidenz-Grotesk BQ'  # Can be replaced with any font installed on computer
    ),
    plot_bgcolor='#ffffff',
    title=go.layout.Title(
        text='Cars in Canada have the highest emissions in 2017',
        xref='paper',
        x=0,
        font=dict(
            size=18,
            color=grey_palette[5]
        )
    ),
    annotations=[dict(
        text="Average grams of CO₂ emitted per kilometer driven (g CO₂ / km)",
        font=dict(
            size=13,
            color=grey_palette[2],
        ),
        showarrow=False,
        x=0,
        y=1.06,
        xref='paper',
        yref='paper',
    )],
    xaxis=go.layout.XAxis(
        zeroline=False,
        side='top',
        tickfont=dict(
            color=grey_palette[2]
        )
    ),
    yaxis=go.layout.YAxis(
        tickfont=dict(
            color=grey_palette[3]
        )
    )
)

fig = go.Figure(data=data, layout=layout)
# Windows style filepaths (change if necessary)
image_filepath = 'graphs\\avg-co2-emissions-2017.png'
pio.write_image(fig, file=image_filepath, format='png')

# For exporting to pdf
#image_filepath = 'graphs\\avg-co2-emissions-2017.pdf'
#pio.write_image(fig, file=image_filepath, format='pdf')