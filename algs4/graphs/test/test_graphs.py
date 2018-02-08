import os

from pytest import approx

from algs4.graphs.graphs import Graph, EdgeWeightedGraph, Prim, Kruskal, LazyPrim, Dijkstra, EdgeWeightedDigraph


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


def test_calculating_mst_weight_on_tiny_data_with_lazy_prim():
    mst = LazyPrim(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_calculating_mst_weight_on_tiny_data_with_prim():
    mst = Prim(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_calculating_mst_weight_on_tiny_data_with_kruskal():
    mst = Kruskal(EdgeWeightedGraph.from_file(resource_path('tiny_ewg.txt')))

    assert mst.weight == approx(1.81)


def test_compare_mst_weight_on_larger_data_set():
    ewg = EdgeWeightedGraph.from_file(resource_path('medium_ewg.txt'))

    assert LazyPrim(ewg).weight == approx(Prim(ewg).weight) == approx(Kruskal(ewg).weight)


def test_calculating_shortest_path_on_tiny_data_with_dijkstra():
    v_to_d = {
        0: 0.00,
        1: 1.05,
        2: 0.26,
        3: 0.99,
        4: 0.38,
        5: 0.73,
        6: 1.51,
        7: 0.60
    }

    sp = Dijkstra(EdgeWeightedDigraph.from_file(resource_path('tiny_ewd.txt')))

    for v, d in v_to_d.items(): assert sp.distance_to[v] == approx(d)
