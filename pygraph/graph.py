import numpy as np


class Graph:
    """
    A class for Graph Object
    果物の各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    fruit_id : int
        対象の果物のマスタID。
    fruit_name : str
        果物名。
    price_dict : dict
        キーに地域のID、値に該当する地域での値段を保持した辞書。
    """

    def __init__(self, A, is_directed=False):
        self.adj_mat = A
        self.is_directed = is_directed

        if self.adj_mat is not None:
            self.num_vertex = self.adj_mat.shape[0]
        else:
            self.num_vertex = 0

        if self.adj_mat is not None:
            self.num_edge = np.sum(self.adj_mat) // 2
        else:
            self.num_edge = 0

    def number_of_vertex(self):
        return self.num_vertex

    def number_of_edge(self):
        return self.num_edge

    def adjacency_matrix(self):
        return self.adj_mat
