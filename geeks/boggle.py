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

from algs4.graphs import Graph


def find_words(boggle: List[List[str]], is_word: Callable[[str], bool]) -> Set[str]:
    """All words while searching adjacent cells of boggle."""
    def as_i(x: int, y: int) -> int: return y * M + x

    def add_adj_fields():
        adjacent = tuple((i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0)

        for y in range(N):
            for x in range(M):
                i = as_i(x, y)
                i_to_a[i] = boggle[y][x]

                for dx, dy in adjacent:
                    if 0 <= x + dx <= M - 1 and 0 <= y + dy <= N - 1:
                        g.add_edge(i, as_i(x + dx, y + dy))

    def dfs(s: int, letters: List[str], visited: List[int], stack: List[int]):
        visited[s] = True
        stack.append(s)

        letters.append(i_to_a[s])

        possible_word = ''.join(letters)

        if is_word(possible_word): unique_words.add(possible_word)

        for v in g.adj[s]:
            if not visited[v]:
                dfs(v, letters, visited, stack)

        letters.pop()
        visited[stack.pop()] = False

    N, M = len(boggle), len(boggle[0])  # type: int, int
    i_to_a = {}  # type: Dict[int, str]
    unique_words = set()

    g = Graph(M * N)

    add_adj_fields()

    for i in range(M * N):
        dfs(i, [], [False] * (M * N), [])

    return unique_words
