from typing import Any, Optional


class Bst:
    """Binary Search Tree."""

    class Node:
        """Bst node."""

        def __init__(self, key: Any, val):
            self.key = key
            self.val = val
            self.left, self.right = None, None

    def __init__(self):
        self.root = None

    def __len__(self):
        return self.size(self.root)

    def put(self, key, val: object) -> None:
        """Upsert of value associated with the key."""
        if key is None: raise ValueError('None keys are not permitted')

        self.root = self._put(self.root, key, val)

    def get(self, key) -> object:
        """Get value associated with key or None if such node does not exist."""
        if key is None: raise ValueError('None keys are not permitted')

        return self._get(self.root, key)

    def min(self):
        """Return min key."""
        return self._min(self.root).key

    def max(self):
        """Return max key."""
        return self._max(self.root).key

    def remove_min(self) -> None:
        """Remove node with min key."""
        self.root = self._remove_min(self.root)

    def remove_max(self) -> None:
        """Remove node with max key."""
        self.root = self._remove_max(self.root)

    def remove(self, key) -> None:
        """Remove node with given key."""
        if key is None: raise ValueError('None keys are not permitted')

        self.root = self._remove(self.root, key)

    def size(self, node: Optional['Bst.Node']) -> int:
        if node is None: return 0

        return self.size(node.left) + self.size(node.right) + 1

    def _put(self, node: Optional['Bst.Node'], key, val: object) -> 'Bst.Node':

        if node is None: return Bst.Node(key, val)

        if key > node.key:   node.right = self._put(node.right, key, val)
        elif key < node.key: node.left = self._put(node.left, key, val)
        else: node.val = val

        return node

    def _get(self, node: Optional['Bst.Node'], key) -> object:
        if node is None: return None

        if key > node.key:   return self._get(node.right, key)
        elif key < node.key: return self._get(node.left, key)

        return node.val

    def _min(self, node) -> 'Bst.Node':
        return node if node.left is None else self._min(node.left)

    def _max(self, node) -> 'Bst.Node':
        return node if node.right is None else self._min(node.right)

    def _remove_min(self, node) -> 'Bst.Node':
        """Finds min node and returns it's RIGHT link."""
        if node.left is None: return node.right

        node.left = self._remove_min(node.left)

        return node

    def _remove_max(self, node) -> 'Bst.Node':
        """Finds max node and returns it's LEFT link."""
        if node.right is None: return node.left

        node.right = self._remove_max(node.right)

        return node

    def _remove(self, node: Optional['Bst.Node'], key) -> Optional['Bst.Node']:
        if node is None: return None

        if key > node.key:   node.right = self._remove(node.right, key)
        elif key < node.key: node.left = self._remove(node.left, key)
        else:
            if node.left is None: return node.right
            if node.right is None: return node.left

            # pierscin: Hibbard deletion
            t = node

            node = self._min(t.right)
            node.right = self._remove_min(t.right)
            node.left = t.left

        return node
