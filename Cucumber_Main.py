import random
import numpy as np
from matplotlib import pyplot as plt
import operator
from lorem_text import lorem


class GraphGen:
    def __init__(self, *args, **kwargs):
        super(GraphGen, self).__init__(*args, **kwargs)

        self.figure, self.ax = plt.subplots()
        self.units = ['meters (m)', 'seconds (s)', 'ampere (A)', 'candela (cd)',
                      'gram (g)', 'mole (mol)', 'kelvin (K)', 'radian (rad)', 'bit', 'count'
                      ]
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        self.lineStyles = ['-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted']
        self.fontSizes = ['15px', '16px', '17px', '18px', '19px', '20px']
        self.lineWidth = [0.2, 0.5, 1, 2, 3, 4, 5 ]
        self.trueFalse = [True, False]
        self.gridAxis = ['both', 'x', 'y']
        self.gridWhich = ['major', 'minor', "both"]
        self.maxPlotAmount = 3
        self.amountOfGraph = 10
        self.Nb100 = np.linspace(-2, 2, 100)

        self.words = 1
        self.plot = None
        self.styles = None
        self.SavePlot = None

    def graph_gene(self, nb: int):
        self.amountOfGraph = nb
        name = 0
        for i in range(self.amountOfGraph):
            name += 1
            self.ax.grid(b=random.choice(self.trueFalse), which=random.choice(self.gridWhich),
                         axis=random.choice(self.gridAxis), color=random.choice(self.colors),
                         linestyle=random.choice(self.lineStyles), linewidth=random.choice(self.lineWidth))
            # self.ax.set_facecolor(random.choice(self.colors))
            self.ax.set_xlabel(random.choice(self.units))
            self.ax.set_ylabel(random.choice(self.units))

            for j in range(random.randrange(1, self.maxPlotAmount)):
                liste100 = list(np.linspace(-10, 10, 21))
                liste100.pop(0)
                polyNb = random.randrange(2, 9)
                liste = [0] * polyNb
                for k, m in enumerate(liste):
                    liste[k] = random.choice(liste100)
                # print(liste)
                polyNom = np.poly1d(liste)
                print(polyNom)
                x = random.sample(list(self.Nb100), 100)
                y = [0] * 100
                for l in range(100):
                    y[l] += np.polyval(polyNom, x[l])
                L = sorted(zip(x, y), key=operator.itemgetter(0))
                x, y = zip(*L)
                self.ax.plot(x, y, color=random.choice(self.colors))

            plt.savefig(fname='Graphs\Graph_{}'.format(name), dpi=random.randrange(20, 300))
            self.ax.clear()

    def normal_choice(self, lst, mean=None, stddev=None):
        if mean is None:
            # if mean is not specified, use center of list
            mean = (len(lst) - 1) / 2

        if stddev is None:
            # if stddev is not specified, let list be -3 .. +3 standard deviations
            stddev = len(lst) / 6

        while True:
            index = int(random.normalvariate(mean, 2) + 0.5)
            if 0 <= index < len(lst):
                return lst[index]

    def functions(self):
        self.constant = random.randrange(-1000, 1000)
        self.linear =



if __name__ == '__main__':
    a = GraphGen()
    a.graph_gene(20)
