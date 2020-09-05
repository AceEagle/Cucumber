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
        self.lineWidth = [0.2, 0.5, 1, 2, 3, 4, 5]
        self.trueFalse = [True, False]
        self.gridAxis = ['both', 'x', 'y']
        self.gridWhich = ['major', 'minor', "both"]

        self.dataRange = [-100, 100]
        self.nbData = 100
        self.plot = None
        self.styles = None
        self.SavePlot = None
        self.coefficientRange = (-20, 20)
        self.coefficientRangePositive = (2, 40)
        self.Nb100 = np.linspace(self.dataRange[0], self.dataRange[1], self.nbData)
        self.FunctionsListe = [self.constant, self.linear, self.quadratic, self.cubic,
                               self.quartic, self.quintic, self.sextic, self.rational,
                               self.square_root, self.cube_root, self.expo]

    def randomize_data_range(self):
        pass

    def graph_gene(self):
        name = lorem.words(1)
        x, y = self.add_functions()
        self.ax.grid(b=random.choice(self.trueFalse), which=random.choice(self.gridWhich),
                     axis=random.choice(self.gridAxis), color=random.choice(self.colors),
                     linestyle=random.choice(self.lineStyles), linewidth=random.choice(self.lineWidth))
        # self.ax.set_facecolor(random.choice(self.colors))
        self.ax.set_xlabel(random.choice(self.units))
        self.ax.set_ylabel(random.choice(self.units))

        self.ax.plot(x, y, color=random.choice(self.colors))

        plt.savefig(fname='Graphs\Graph_{}'.format(name), dpi=random.randrange(100, 300))
        self.ax.clear()

    def add_functions(self):
        listex = []
        listey = []
        nbparties = random.randrange(1, 11)
        n = int(100 / nbparties)
        dividedx = []
        dividedy = []
        for i in range(nbparties):
            badx, bady = random.choice(self.FunctionsListe)()
            x = list(badx)
            y = list(bady)
            print(y)
            for j in x[i * n:(i + 1) * n]:
                dividedx += j
            for k in y[i * n:(i + 1) * n]:
                dividedy += k
        return listex, listey

    @staticmethod
    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def constant(self):
        y = [random.randrange(-1000, 1000)] * 100
        x = random.sample(list(self.Nb100), 100)
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = list(zip(*w))
        return x, y

    def linear(self):
        listeLinear = [0] * 2
        for k, m in enumerate(listeLinear):
            listeLinear[k] = random.randrange(*self.coefficientRange)
        polyLinear = np.poly1d(listeLinear)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyLinear, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

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
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def cubic(self):
        listeCubic = [0] * 4
        for k, m in enumerate(listeCubic):
            listeCubic[k] = random.randrange(*self.coefficientRange)
        polyCubic = np.poly1d(listeCubic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyCubic, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def quartic(self):
        listeQuartic = [0] * 5
        for k, m in enumerate(listeQuartic):
            listeQuartic[k] = random.randrange(*self.coefficientRange)
        polyQuartic = np.poly1d(listeQuartic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyQuartic, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def quintic(self):
        listeQuintic = [0] * 6
        for k, m in enumerate(listeQuintic):
            listeQuintic[k] = random.randrange(*self.coefficientRange)
        polyQuintic = np.poly1d(listeQuintic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyQuintic, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def sextic(self):
        listeSextic = [0] * 7
        for k, m in enumerate(listeSextic):
            listeSextic[k] = random.randrange(*self.coefficientRange)
        polySextic = np.poly1d(listeSextic)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polySextic, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def rational(self):
        listeRational = [0] * 7
        for k, m in enumerate(listeRational):
            listeRational[k] = random.randrange(*self.coefficientRange)
        listeRational2 = [0] * 7
        for k, m in enumerate(listeRational2):
            listeRational2[k] = random.randrange(*self.coefficientRange)
        polyRational = np.poly1d(np.polydiv(listeRational, listeRational2))
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += np.polyval(polyRational, x[l])
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def square_root(self):
        a = random.randrange(*self.coefficientRange)
        while a == 0:
            a = random.randrange(*self.coefficientRange)
        b = random.randrange(*self.coefficientRange)
        while b == 0:
            b = random.randrange(*self.coefficientRange)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            mats = math.sqrt(b * x[l])
            y[l] += a * mats
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def cube_root(self):
        a = random.randrange(*self.coefficientRange)
        while a == 0:
            a = random.randrange(*self.coefficientRange)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += a * (x[l] ** 3)
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y

    def expo(self):
        a = random.randrange(*self.coefficientRange)
        b = random.randrange(*self.coefficientRange)
        c = random.randrange(*self.coefficientRangePositive)
        x = random.sample(list(self.Nb100), 100)
        y = [0] * 100
        for l in range(100):
            y[l] += a * (c ^ (b * x[l]))
        w = sorted(zip(x, y), key=operator.itemgetter(0))
        x, y = zip(*w)
        return x, y


a = GraphGen()
a.add_functions()