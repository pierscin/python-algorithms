import os

from pytest import approx

from algs4.graphs.graphs import Graph, EdgeWeightedGraph, Prim


def resource_path(name: str) -> str:
    return os.path.join(os.path.dirname(__file__), '..', 'resources', name)


def test_graph_creation_from_file():
    g = Graph.from_file(resource_path('tiny_g.txt'))

    assert g.v == 13
    assert g.e == 13


def test_edge_weighted_graph_creation_from_file():
    ewg = EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt'))

    assert ewg.v == 8
    assert ewg.e == 16


def test_calculating_mst_weight_with_prim():
    mst = Prim(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(0.19 + 0.26 + 0.17 + 0.35 + 0.28 + 0.40 + 0.16)
