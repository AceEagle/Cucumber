import random
import numpy as np
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import os
from pint import UnitRegistry

class Graph_Gen(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Graph_Gen, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        ureg = UnitRegistry()

        self.BackgroundColors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']