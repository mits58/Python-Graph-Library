import unittest

from graph import Graph


class TestGraphObject(unittest.TestCase):
    """
    Test Class of Grah Object
    """

    def test_graph_to_string(self):
        num_vertex, num_edge = 10, 10
        g = Graph(num_vertex, num_edge)
        expected = "|V|=10, |E|=10"
        actual = str(g)
        self.assertEqual(expected, actual)
