import unittest

import numpy as np

from graph import Graph


class TestGraphClass(unittest.TestCase):
    """
    Test Class for Graph Class
    """
    def test_generating_graph_object(self):
        """
        Testing Generation of Graph Object from Adjacent Matrix
        """
        # setup
        A = np.array([[0, 1, 1, 0, 0],
                      [1, 0, 0, 1, 0],
                      [1, 0, 0, 1, 1],
                      [0, 1, 1, 0, 0],
                      [0, 0, 1, 0, 0]])

        # run
        G = Graph(A, is_directed=False)

        # validation
        self.assertEqual(G.number_of_vertex(), 5)                   # |V|
        self.assertEqual(G.number_of_edge(), 5)                     # |E|
        self.assertTrue(np.array_equal(G.adjacency_matrix(), A))    # Adj Mat.


if __name__ == '__main__':
    unittest.main()
