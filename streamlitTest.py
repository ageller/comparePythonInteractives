# run with 
# $ streamlit run streamlitTest.py

import pandas as pd
import numpy as np

import streamlit as st
import altair as alt

# page info
st.set_page_config(layout = 'centered', page_title = 'COVID-19 Data Explorer')

# read in the data (do this only once)
@st.cache
def readData():

	# COVID-19 cases and deaths as a function of time for multiple countries
	# df = pd.read_csv('data/WHO-COVID-19-global-data.csv') # in case the WHO server goes down
	df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')

	# convert the date column to datetime objects for easier plotting and manipulation later on
	df['Date_reported'] = pd.to_datetime(df['Date_reported'])

	# get all the available countries from the data 
	availableCountries = df['Country'].unique().tolist()

	# I'll also want to take rolling means over 7 day intervals for each country
	rollingAve = 7

	# The DataFrame is already sorted by country, so I will just go through each country and append to a list
	r1 = []
	r2 = []
	r3 = []
	r4 = []
	for c in availableCountries:
		usedf =  df.loc[df['Country'] == c]
		r1 += usedf['New_cases'].rolling(rollingAve).mean().to_list()
		r2 += usedf['New_deaths'].rolling(rollingAve).mean().to_list()
		r3 += usedf['Cumulative_cases'].rolling(rollingAve).mean().to_list()
		r4 += usedf['Cumulative_deaths'].rolling(rollingAve).mean().to_list()
	df['New_cases_rolling'] = np.nan_to_num(r1)
	df['New_deaths_rolling'] = np.nan_to_num(r2)
	df['Cumulative_cases_rolling'] = np.nan_to_num(r3)
	df['Cumulative_deaths_rolling'] = np.nan_to_num(r4)

	return df, availableCountries

# this should only be executed once
df, availableCountries = readData()


# for spacing between items on the page
def space(num_lines=1):
	"""Adds empty lines to the Streamlit app."""
	for _ in range(num_lines):
		st.write("")


# plot title
st.title('Streamlit COVID-19 Data Explorer')
space(1)

# radio buttons to choose column
columns = ['New_cases_rolling', 'New_deaths_rolling', 'Cumulative_cases_rolling', 'Cumulative_deaths_rolling']
labels = {'New_cases_rolling':'Daily Cases', 
	'New_deaths_rolling':'Daily Deaths', 
	'Cumulative_cases_rolling':'Cumulative Cases',
	'Cumulative_deaths_rolling':'Cumulative Deaths'
}

def format_func(option):
    return labels[option]

column = st.radio(
	'Choose data type',
	columns,
	format_func = format_func,
	index = 0
)
space(1)

# dropdown to choose country
country = st.selectbox(
	'Select a Country',
	availableCountries,
	index = availableCountries.index('United States of America'))
space(1)


# select the data
usedf = df.loc[df['Country'] == country].reset_index(drop = True)
chart_data = usedf[['Date_reported',column]].set_index('Date_reported')

# create the chart
# this is a wrapper for altair
#   if I wanted to change the color or remove the legend or make other tweaks, I would need to use st.altiar_chart
st.area_chart(chart_data)




