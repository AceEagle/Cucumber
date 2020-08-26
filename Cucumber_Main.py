import random
import numpy as np
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import os


class Create100graphs(QtWidgets.QMainWindow):

        def __init__(self, *args, **kwargs):
            super(Create100graphs, self).__init__(*args, **kwargs)

            self.graphWidget = pg.PlotWidget()
            self.setCentralWidget(self.graphWidget)

            self.colors = np.array('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
            self.letters = np.array(
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                'w', 'x', 'y', 'z')
