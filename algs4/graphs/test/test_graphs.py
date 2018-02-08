import os

from pytest import approx

from algs4.graphs.graphs import Graph, EdgeWeightedGraph, Prim, Kruskal, LazyPrim


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


def test_calculating_tiny_mst_weight_with_lazy_prim():
    mst = LazyPrim(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_calculating_tiny_mst_weight_with_prim():
    mst = Prim(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_calculating_tiny_mst_weight_with_kruskal():
    mst = Kruskal(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_compare_mst_weight_on_larger_data_set():
    ewg = EdgeWeightedGraph.from_file(resource_path('medium_ewg.txt'))

    assert LazyPrim(ewg).weight == approx(Prim(ewg).weight) == approx(Kruskal(ewg).weight)
