"""Boggle (Find all possible words in a board of characters)

Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character.
Find all possible words that can be formed by a sequence of adjacent characters.
Note that we can move to any of8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

    Input:
        dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
        boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
        isWord(str): returns true if str is present in dictionary else false.

    Output:
        Following words of dictionary are present: GEEKS, QUIZ

Link:
    https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/

Returns:
    List of words which can be made from boggle.
"""
from typing import List, Dict, Set, Callable


class BoggleGraph:
    """After initialization, field unique_words is the result."""

    def __init__(self, boggle: List[List[str]], is_word: Callable[[str], bool]):
        self.M, self.N = len(boggle), len(boggle[0])  # type: int, int
        self._v = self.M * self.N  # type: int
        self._is_word = is_word
        self._i_to_a = {}  # type: Dict[int, str]
        self._adj = {v: set() for v in range(self._v)}  # type: Dict[int, Set[int]]

        adjacent = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0]

        for y in range(self.N):
            for x in range(self.M):
                i = self._as_i(x, y)
                self._i_to_a[i] = boggle[y][x]

                for dx, dy in adjacent:
                    if 0 <= x + dx <= self.M - 1 and 0 <= y + dy <= self.N - 1:
                        self._add_edge(i, self._as_i(x + dx, y + dy))

        self.unique_words = set()

        for i in range(self.M * self.N):
            self._dfs(i, [False] * (self.M * self.N), [])

    def _as_i(self, m: int, n: int) -> int:
        return m * self.M + n

    def _add_edge(self, w, v):
        self._adj[w].add(v)
        self._adj[v].add(w)

    def _dfs(self, s: int, visited: List[int], stack: List[int]):
        visited[s] = True
        stack.append(s)

        current = ''.join([self._i_to_a[i] for i in stack])

        if self._is_word(current): self.unique_words.add(current)

        for v in self._adj[s]:
            if not visited[v]:
                self._dfs(v, visited, stack)

        visited[stack.pop()] = False
