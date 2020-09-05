from unittest import TestCase
from Cucumber_Main import GraphGen


class TestGraphGen(TestCase):

    def setUp(self):
        print("hello")
        self.generator = GraphGen()

    def tearDown(self):
        print("byebye")

    def test_graph_gene(self):
        self.fail()

    def test_normal_choice(self):
        self.fail()

    def test_constant(self):
        a, b = self.generator.constant()
        print(a, b)
        nb = 0
        self.assertEqual()
        for x, i in enumerate(b):

    def test_linear(self):
        self.fail()

    def test_quadratic(self):
        self.fail()

    def test_cubic(self):
        self.fail()

    def test_cubeRoot(self):
        self.fail()

    def test_quartic(self):
        self.fail()

    def test_quintic(self):
        self.fail()

    def test_sextic(self):
        self.fail()

    def test_rational(self):
        self.fail()

    def test_square_root(self):
        self.fail()

    def test_expo(self):
        self.fail()
