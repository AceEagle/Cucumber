import random
import numpy as np
from matplotlib import pyplot as plt
import operator
from lorem_text import lorem
import math


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

        self.plot = None
        self.styles = None
        self.SavePlot = None
        self.coefficientRange = (-20, 20)

    def graph_gene(self, x, y):
        name = lorem.words(1)
        self.ax.grid(b=random.choice(self.trueFalse), which=random.choice(self.gridWhich),
        axis=random.choice(self.gridAxis), color=random.choice(self.colors),
        linestyle=random.choice(self.lineStyles), linewidth=random.choice(self.lineWidth))
        # self.ax.set_facecolor(random.choice(self.colors))
        self.ax.set_xlabel(random.choice(self.units))
        self.ax.set_ylabel(random.choice(self.units))

        self.ax.plot(x, y, color=random.choice(self.colors))

        plt.savefig(fname='Graphs\Graph_{}'.format(name), dpi=random.randrange(100, 300))
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

    def constant(self):
        y = [random.randrange(-1000, 1000)] * 100
        x = random.sample(list(self.Nb100), 100)
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def linear(self):
        listeLinear = [0] * 2
        for k, m in enumerate(listeLinear):
            listeLinear[k] = random.randrange(*self.coefficientRange)
        polyLinear = np.poly1d(listeLinear)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyLinear, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def quadratic(self):
        listeQuadratic = [0] * 3
        for k, m in enumerate(listeQuadratic):
            listeQuadratic[k] = random.randrange(*self.coefficientRange)
            while listeQuadratic[0] == 0:
                listeQuadratic[0] = random.randrange(*self.coefficientRange)

        polyQuadratic = np.poly1d(listeQuadratic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyQuadratic, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def cubic(self):
        listeCubic = [0] * 4
        for k, m in enumerate(listeCubic):
            listeCubic[k] = random.randrange(*self.coefficientRange)
        polyCubic = np.poly1d(listeCubic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyCubic, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def quartic(self):
        listeQuartic = [0] * 5
        for k, m in enumerate(listeQuartic):
            listeQuartic[k] = random.randrange(*self.coefficientRange)
        polyQuartic = np.poly1d(listeQuartic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyQuartic, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)
        
    def quintic(self):
        listeQuintic = [0] * 6
        for k, m in enumerate(listeQuintic):
            listeQuintic[k] = random.randrange(*self.coefficientRange)
        polyQuintic = np.poly1d(listeQuintic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyQuintic, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def sextic(self):
        listeSextic = [0] * 7
        for k, m in enumerate(listeSextic):
            listeSextic[k] = random.randrange(*self.coefficientRange)
        polySextic = np.poly1d(listeSextic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polySextic, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def rational(self):
        listeRational = [0] * 7
        for k, m in enumerate(listeRational):
            listeRational[k] = random.randrange(*self.coefficientRange)
        listeRational2 = [0] * 7
        for k, m in enumerate(listeRational2):
            listeRational2[k] = random.randrange(*self.coefficientRange)
        polyRational = np.poly1d(listeRational/listeRational2)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyRational, x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

    def squareRoot(self):
        a = random.randrange(-20, 20)
        while a == 0:
            a = random.randrange(-20, 20)
        b = random.randrange(-20, 20)
        while b == 0:
            b = random.randrange(-20, 20)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += a * math.sqrt(b * x[l])
        L = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*L)
        self.graph_gene(x, y)

