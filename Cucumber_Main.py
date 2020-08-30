import random
import numpy as np
from matplotlib import pyplot as plt
import operator
from lorem_text import lorem


class GraphGen():
    def __init__(self, *args, **kwargs):
        super(GraphGen, self).__init__(*args, **kwargs)

        self.figure, self.ax = plt.subplots()
        self.units = ['meters (m)', 'seconds (s)', 'ampere (A)', 'candela (cd)',
                      'gram (g)', 'mole (mol)', 'kelvin (K)', 'radian (rad)', 'bit', 'count'
                      ]
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        self.lineStyles = ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']
        self.fontSizes = ['15px', '16px', '17px', '18px', '19px', '20px']
        self.lineWidth = [0.2, 0.5, 1, 2, 3, 4, 5 ]
        self.trueFalse = [True, False]
        self.gridAxis = ['both', 'x', 'y']
        self.gridWhich = ['major', 'minor', "both"]
        self.maxPlotAmount = 3
        self.amountOfGraph = 10
        self.Nb100 = np.linspace(-1000, 1000, 2000)

        self.words = 1
        self.plot = None
        self.styles = None
        self.SavePlot = None

    def graph_gene(self, nb: int):
        self.amountOfGraph = nb

        for i in range(self.amountOfGraph):
            self.ax.grid(b=random.choice(self.trueFalse), which=random.choice(self.gridWhich),
                         axis=random.choice(self.gridAxis), color=random.choice(self.colors),
                         linestyle=random.choice(self.lineStyles), linewidth=random.choice(self.lineWidth))
            # self.ax.set_facecolor(random.choice(self.colors))
            self.ax.set_xlabel(random.choice(self.units))
            self.ax.set_ylabel(random.choice(self.units))

            for j in range(random.randrange(1, self.maxPlotAmount)):
                x = random.sample(list(self.Nb100), 100)
                y = random.sample(list(self.Nb100), 100)
                L = sorted(zip(x, y), key=operator.itemgetter(0))
                x, y = zip(*L)
                self.ax.plot(x, y, color=random.choice(self.colors))

            plt.show()
            self.ax.clear()


if __name__ == '__main__':
    a = GraphGen()
    a.graph_gene(4)
