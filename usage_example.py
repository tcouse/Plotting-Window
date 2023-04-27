"""
This file will not run, but it shows an example of how I implemented this class previously.
I will update this if I ever use this again - this repo exists purely because I want to
remember how I implemented it last time.
"""
data = 'this would be a dataframe or table such as a pandas dataframe'
y_types = 'this would be a list of the names of the columns in data'

# creating the plot window
pw = PlotWindow()

time = data.col('time')

# looping through all the data to plot
for y_type in y_types:

    # getting the actual data
    if left_and_right:
        y_data1 = data.col(y_type + '_left')
        y_data2 = data.col(y_type + '_right')
        y_data = (y_data1, y_data2,)
    else:
        y_data = data.col(y_type)

    # creating the plots
    fig, ax = PlotWindow.plot(time, y_data)

    # formatting the legend based on y_types list
    if left_and_right:
        label = y_type
    else:
        label = y_type[0:-5]

    ax.set_ylabel(label)
    pw.addPlot(label, fig)

pw.show()
