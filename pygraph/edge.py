class Edge:
    """
    A class for representating an edge.

    Attributes
    ----------
    source : A Start Vertex
    sink : A End Vertex
    """

    def __init__(self, source=None, sink=None, weight=1, cap=0):
        """
        Making Edge

        Parameters
        ----------
        source : Vertex Object, default None
        sink : Vertex Object, default None
        weigth : float, default 1
        cap : capacity, default 0
        """
        self.source = source
        if sink is None and source is not None:
            self.sink = source
        else:
            self.sink = sink
