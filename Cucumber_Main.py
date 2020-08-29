import random
from lorem_text import lorem
import numpy as np
import pyqtgraph as pg
import pyqtgraph.exporters


class GraphGen:
    def __init__(self, *args, **kwargs):
        super(GraphGen, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()

        self.units = ['meters (m)', 'seconds (s)', 'ampere (A)', 'candela (cd)',
                      'gram (g)', 'mole (mol)', 'kelvin (K)', 'radian (rad)', 'bit', 'count'
                      ]
        self.BackgroundColors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        self.FontSizes = ['15px', '16px', '17px', '18px', '19px', '20px']
        self.TrueFalse = [True, False]
        self.Nb100 = np.linspace(-1000, 1000, 2000)

        self.words = 1
        self.plot = None
        self.styles = None
        self.SavePlot = None

    def graph_gene(self, nb: int):
        for i in range(nb):
            self.graphWidget.setBackground(random.choice(self.BackgroundColors))
            self.styles = {'color': random.choice(self.BackgroundColors), 'font-size': random.choice(self.FontSizes)}
            self.graphWidget.setLabel('left', random.choice(self.units), **self.styles)
            self.graphWidget.setLabel('bottom', random.choice(self.units), **self.styles)
            self.graphWidget.showGrid(x=random.choice(self.TrueFalse), y=random.choice(self.TrueFalse))

            for j in range(random.randrange(1, 4)):
                self.plot(random.sample(self.Nb100, 100), random.sample(self.Nb100, 100), lorem.words(self.words),
                          random.choice(self.BackgroundColors))

            pen = pg.mkPen(color=random.choice(self.BackgroundColors), width=random.randrange(5, 15))
            self.SavePlot = self.graphWidget.plot(name='PlotName', pen=pen)
            exporter = pg.exporters.ImageExporter(self.SavePlot)
            exporter.export(lorem.words(self.words))
            self.graphWidget.clear()


if __name__ == '__main__':
    a = GraphGen()
    a.graph_gene(100)
