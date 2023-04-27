"""
A class used to organize a plot window and add matplotlib figures to the window using tabs.
"""
import sys

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QVBoxLayout


class PlotWindow:
    """
    A utility class used to create a Plot Window for matplotlib plots using a Qt backend.
    """
    def __init__(self, window_name="Plot Window"):
        """
        The constructor for the PlotWindow class. This sets up the the Qt window and associated
        backend properties.

        :param window_name: A string of the name of the window being created.
        """
        # creating the window and setting up it's basic properties
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.main_window.__init__()
        self.main_window.setWindowTitle(window_name)

        # initializing lists that will hold window properties
        self.canvases = []
        self.figure_handles = []
        self.toolbar_handles = []
        self.tab_handles = []

        # initializing the tabs
        self.tabs = QTabWidget()
        self.main_window.setCentralWidget(self.tabs)

        # resizing the window and displaying it
        self.main_window.resize(1280, 900)
        self.main_window.show()

    def addPlot(self, title, figure):
        """
        Used to add plots as new tabs into the Plot Window.

        :param title: A string of the title of the additional tab.
        :param figure: The matplotlib Figure being added as a new tab to the window.
        """
        # initializing a new window with a QV box layout
        new_tab = QWidget()
        layout = QVBoxLayout()
        new_tab.setLayout(layout)

        # adjusting the spacing of the new subplot
        figure.set_tight_layout(True)
        # creating the new canvas and toolbar objects for this subplot
        new_canvas = FigureCanvas(figure)
        new_toolbar = NavigationToolbar(new_canvas, new_tab)

        # adding the new subplot as widget
        layout.addWidget(new_canvas)
        layout.addWidget(new_toolbar)
        self.tabs.addTab(new_tab, title)

        # updating window properties to include new subplot information
        self.toolbar_handles.append(new_toolbar)
        self.canvases.append(new_canvas)
        self.figure_handles.append(figure)
        self.tab_handles.append(new_tab)

    @staticmethod
    def plot(x_val, y_vals, x_label="Time (s)", legend_labels=None, title=None):
        """
        A simple plotting function that plots multiple y values against the same x value.

        :param x_val: The value to plot on the x-axis.
        :param y_vals: A tuple or list of values to plot on the y-axis.
        :param x_label: A string of the label on the x-axis.
        :param legend_labels: A tuple or list of the legend_labels for the y values.
        :param title: A string of the title of the figure being plotted.

        :return: A tuple of the matplotlib Figure and Axis subplot pair.
        """
        # creating a subplot axis to plot on
        current_fig, current_ax = plt.subplots()

        # adding variables to the plot
        for ind, value in enumerate(y_vals):
            if ind == 0:
                current_ax.plot(x_val, value, linewidth=3.0)
            else:
                current_ax.plot(x_val, value, '--', linewidth=3.0)
            current_ax.set_xlabel(x_label)

        # if there are any legend_labels, create a legend using them
        if legend_labels:
            current_ax.legend(legend_labels)

        # if there is a title, add it
        if title:
            current_fig.suptitle(title, fontsize=12)

        return current_fig, current_ax

    def show(self):
        """
        Displays the window.
        """
        self.app.exec_()

