#!/usr/bin/env python3

"""
    Generates portions of plot code and variable names for average-fuel-consumption.py

    Generated code is printed into the console and needs to by copy-pasted manually
"""

from string import Template

country_names_filepath = 'country-list.txt'
country_names = []
countries_to_ignore = ['Canada', 'United States', 'China', 'Germany']  # These countries are plotted differently in average-fuel-consumption.py
with open(country_names_filepath, 'r') as file:
    for line in file:
        country = line.strip('\n')
        if country not in countries_to_ignore:
            country_names.append(country)
print(country_names)

plot_definition_code = Template('''${variable_name} = go.Scatter(
    x=plotting_data['$country']['years'],
    y=plotting_data['$country']['fuel-consumption'],
    mode='lines',
    line=dict(
        width=1,
        color=background_grey_line_color
    )
)
''')

plot_variable_names = []
for country in country_names:
    variable_name = country.lower().replace(' ', '') + '_fuel_consumption'
    plot_variable_names.append(variable_name)
    plot_code = plot_definition_code.substitute(country=country, variable_name=variable_name)
    print(plot_code)

for variable_name in plot_variable_names:
    print('\t' + variable_name + ',')