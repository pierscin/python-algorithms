import os

from algs4.graphs.graphs import Graph, EdgeWeightedGraph


def test_graph_creation_from_file():
    g = Graph.from_file(os.path.join(os.path.dirname(__file__), '..', 'resources', 'tiny_g.txt'))

    assert g.v == 13
    assert g.e == 13


def test_edge_weighted_graph_creation_from_file():
    ewg = EdgeWeightedGraph.from_file(os.path.join(os.path.dirname(__file__), '..', 'resources', 'tiny_ewg.txt'))

    assert ewg.v == 8
    assert ewg.e == 16
