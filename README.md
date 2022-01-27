# Compare Python Interactives

My goal here is create the same interactive plot using a variety of different plotting packages in Python in order to test and compare the various options that other people have developed.  I'm looking for a plotting package that allows me to:

- create a plot of COVID-19 cases vs. time (while displaying the date correctly),
- zoom and pan on the plot,
- create customizable tooltips to show the data values when the mouse hovers over the plot,
- create a dropdown menu to choose the country,
- create a set of buttons to choose which columns I want to plot (for a given country), and
- export directly to a .html file for use on a personal website (without needing any other service).

After scouring the internet for the most popular plotting packages, I've decided to test this set of tools:

 - [Bokeh](https://bokeh.org/)
 - [Plotly](https://plotly.com/python/)
 - [Altair](https://altair-viz.github.io/)
 - [mpld3](http://mpld3.github.io/)
 - [matplotlib](https://matplotlib.org/) + [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/)
 - [pygal](https://www.pygal.org/en/stable/) 
 - [bqplot](https://github.com/bqplot/bqplot)
 - [Streamlit](https://streamlit.io/) 
 

Please see [compareInteractives.ipynb](https://github.com/ageller/comparePythonInteractives/blob/main/compareInteractives.ipynb) for the code.

Live examples of the [Bokeh](https://ageller.github.io/comparePythonInteractives/bokeh_COVID.html) and [Plotly](https://ageller.github.io/comparePythonInteractives/plotly_COVID.html) versions (others are too large for GitHub = Altair & mpld3, or less interesting = pygal).
