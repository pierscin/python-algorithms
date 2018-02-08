import pytest

from algs4.union_find import Uf

N = 5

p = 0
q = 2
r = 4


@pytest.fixture
def uf():
    return Uf(N)


def test_assumptions_about_parameters():
    assert N > 0
    assert 0 <= p < N
    assert 0 <= q < N
    assert 0 <= r < N
    assert p != q and p != r and q != r


def test_at_first_union_find_has_as_many_components_as_sites(uf):
    assert uf.count == N


def test_union_results_in_the_same_component_id(uf):
    assert not uf.connected(p, q)
    assert uf.find(p) != uf.find(q)

    uf.union(p, q)

    assert uf.find(p) == uf.find(q)


def test_after_connecting_two_sites_there_are_fewer_components(uf):
    uf.union(p, q)

    assert uf.count == N - 1


def test_making_same_connection_more_than_once_doesnt_make_any_difference(uf):
    more_than_one = 5

    for _ in range(more_than_one):
        uf.union(p, q)

        assert uf.count == N - 1
        assert uf.connected(p, q)


def test_connection_is_reflective(uf):
    assert uf.connected(p, p)


def test_connection_is_transitive(uf):
    uf.union(p, q)
    uf.union(q, r)

    assert uf.connected(p, q) and uf.connected(q, r) and uf.connected(p, r)


def test_connection_is_symmetric(uf):
    uf.union(p, q)

    assert uf.connected(p, q) and uf.connected(q, p)
