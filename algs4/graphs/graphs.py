from collections import deque, defaultdict
from functools import total_ordering
from typing import Set, Optional, Sequence, DefaultDict, Deque

from algs4.priority_queues import MinHeap, IndexMinPq
from algs4.union_find import Uf


class Graph:
    """Undirected graph."""

    def __init__(self, v: int):
        """Initialize with 'v' vertices and 0 edges."""
        self.v, self.e = v, 0  # type: int, int

        # pierscin: no parallel paths, because of set
        self.adj = defaultdict(set)  # type: DefaultDict[int, Set[int]]

    @classmethod
    def from_file(cls, path: str) -> 'Graph':
        """Create from file in format:

            V # vertices count
            E # edge count
            v w # edge 1
            ...
            v w # edge E
        """
        with open(path) as f:
            g = Graph(int(f.readline()))
            _ = int(f.readline())  # pierscin: edge count

            for line in f:
                v, w = [int(x) for x in line.split()]
                g.add_edge(v, w)

        return g

    def add_edge(self, v: int, w: int) -> None:
        self.adj[v].add(w), self.adj[w].add(v)
        self.e += 1


class DfsPath:
    """Path search with dfs."""

    def __init__(self, g: Graph, s: int):
        self.source = s
        self.marked = [False] * g.v

        self.edge_to = [0] * g.v
        self._dfs(g, s)

    def has_path_to(self, target: int) -> bool:
        """Does path to target exist."""
        return self.marked[target]

    def path_to(self, t: int) -> Optional[Sequence[int]]:
        """Return path if it exists."""
        if not self.marked[t]: return None

        path = []

        v = t

        while v != self.source:
            path.append(v)
            v = self.edge_to[v]

        path.append(self.source)
        return path

    def _dfs(self, g: Graph, source: int) -> None:
        self.marked[source] = True

        for target in g.adj[source]:
            if not self.marked[target]:
                self.edge_to[target] = source
                self._dfs(g, target)


class BfsPath:
    """Shortest path search with bfs."""
    
    def __init__(self, g: Graph, s: int):
        self.source = s
        self.marked = [False] * g.v

        self.edge_to = [0] * g.v
        self._bfs(g, s)

    def has_path_to(self, target: int) -> bool:
        """Does path to target exist."""
        return self.marked[target]

    def path_to(self, t: int) -> Optional[Sequence[int]]:
        """Return path if it exists."""
        if not self.marked[t]: return None

        path = []

        v = t

        while v != self.source:
            path.append(v)
            v = self.edge_to[v]

        path.append(self.source)
        return path

    def _bfs(self, g: Graph, s: int) -> None:
        self.marked[s] = True
        q = deque([s])

        while q:
            v = q.popleft()
            for w in g.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v

                    q.append(w)


@total_ordering
class Edge:
    """Edge with weight."""

    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def other(self, v):
        if v == self.v: return self.w
        if v == self.w: return self.v
        raise ValueError("Inconsistent edge.")

    def __eq__(self, other): return self.weight == other.weight

    def __lt__(self, other): return self.weight < other.weight

    def __str__(self): return '{v} - {w} {weight:.2f}'.format(v=self.v, w=self.w, weight=self.weight)

    def __repr__(self): return 'Edge(v={v}, w={w}, weight={weight})'.format(v=self.v, w=self.w, weight=self.weight)

    def __hash__(self): return hash(self.__repr__())


class EdgeWeightedGraph:
    """Undirected graph with weighted edges."""

    def __init__(self, v: int):
        """Initialize with 'v' vertices and 0 edges."""
        self.v, self.e = v, 0  # type: int, int

        # pierscin: no parallel paths, because of set
        self.adj = defaultdict(set)  # type: DefaultDict[int, Set[Edge]]

    @classmethod
    def from_file(cls, path: str) -> 'EdgeWeightedGraph':
        """Create from file in format:

            V # vertices count
            E # edge count
            v w weight # edge 1
            ...
            v w weight # edge E
        """
        with open(path) as f:
            g = cls(int(f.readline()))
            _ = int(f.readline())  # pierscin: edge count

            for line in f:
                tokens = line.split()

                g.add_edge(Edge(v=int(tokens[0]), w=int(tokens[1]), weight=float(tokens[2])))

        return g

    def add_edge(self, e: Edge) -> None:
        self.adj[e.v].add(e), self.adj[e.w].add(e)
        self.e += 1

    def edges(self):
        bag = set()

        for v, edges in self.adj.items():
            for e in edges:
                if e.other(v) > v: bag.add(e)

        return bag


class LazyPrim:
    """
    Prim's algorithm to find Minimum Spanning Tree.

    Implementation is simple, because it doesn't "clean" priority queue of unused entries.
    """

    def __init__(self, g: EdgeWeightedGraph):
        self.mst = deque()  # type: Deque[Edge]
        self.weight = 0  # type: float

        self._marked = [False] * g.v
        self._min_pq = MinHeap()
        self._distance_to = [float('inf')] * g.v

        self._visit(g, 0)

        while self._min_pq and len(self.mst) < g.v - 1:
            e = self._min_pq.pop_min()  # type: Edge
            v, w = e.v, e.other(e.v)

            if self._marked[v] and self._marked[w]: continue

            self.mst.append(e)
            self.weight += e.weight

            if not self._marked[v]: self._visit(g, v)
            if not self._marked[w]: self._visit(g, w)

    def _visit(self, g: EdgeWeightedGraph, v: int) -> None:
        self._marked[v] = True
        for e in g.adj[v]:
            if not self._marked[e.other(v)] and e.weight < self._distance_to[e.other(v)]:
                self._distance_to[e.other(v)] = e.weight
                self._min_pq.push(e)


class Prim:
    """
    Prim's algorithm to find Minimum Spanning Tree.

    Keeps track of minimum distances to each vertex on IndexMinPq.
    """

    def __init__(self, g: EdgeWeightedGraph):
        self.mst = deque()  # type: Deque[Edge]
        self.weight = 0  # type: float

        self._marked = [False] * g.v
        self._distance_to = [float('inf')] * g.v

        self._min_pq = IndexMinPq(g.v)
        self._distance_to[0] = 0.0
        self._min_pq.insert(0, 0.0)

        while self._min_pq:
            self.weight += self._min_pq.min_key()
            self._visit(g, self._min_pq.remove_min())

    def _visit(self, g: EdgeWeightedGraph, v: int) -> None:
        self._marked[v] = True
        for e in g.adj[v]:
            w = e.other(v)
            if self._marked[w]: continue

            if e.weight < self._distance_to[w]:
                self._distance_to[w] = e.weight
                if w in self._min_pq: self._min_pq.change_key(w, e.weight)
                else: self._min_pq.insert(w, e.weight)


class Kruskal:
    """Kruskal's algorithm to find Minimum Spanning Tree."""

    def __init__(self, g: EdgeWeightedGraph):
        self.mst = deque()  # type: Deque[Edge]
        self.weight = 0  # type: float

        self._min_pq = MinHeap.from_iterable(g.edges())
        self._uf = Uf(g.v)

        while self._min_pq and len(self.mst) < g.v - 1:
            e = self._min_pq.pop_min()  # type: Edge
            v, w = e.v, e.other(e.v)

            if not self._uf.connected(v, w):
                self._uf.union(v, w)
                self.weight += e.weight
                self.mst.append(e)
