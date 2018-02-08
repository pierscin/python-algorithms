class Uf:
    """Weighted quick union find with path comprehension."""

    def __init__(self, N: int):
        """Initialize N sites with integer names (0 to N-1)."""
        self.count = N

        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def union(self, p: int, q: int) -> None:
        """Add connection between p and q."""
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root != q_root:
            if self.size[p_root] < self.size[q_root]:
                self.parent[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                self.parent[q_root] = p_root
                self.size[p_root] += self.size[q_root]
            self.count -= 1

    def find(self, p: int) -> int:
        """Component identifier for p (0 to N-1)."""
        root = p
        while root != self.parent[root]:
            root = self.parent[root]

        while p != root:
            new_p = self.parent[p]
            self.parent[p] = root
            p = new_p

        return p

    def connected(self, p: int, q: int) -> bool:
        """Are p and q in the same component."""
        return self.find(p) == self.find(q)
