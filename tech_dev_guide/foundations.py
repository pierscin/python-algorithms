from collections import defaultdict
from typing import Set, List


def find_longest_subsequence(S: str, D: Set[str]) -> str:
    """
    Description:
        https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/

        Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

        Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W,
        without reordering the remaining characters.

        Note: D can appear in any format (list, hash table, prefix tree, etc.)

        For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct
        output would be "apple"

        The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
        The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the
        right order.
        The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
    Args:
        S: string to search subsequence in.
        D: iterable with words.

    Returns:
        Longest subsequence of S found in D

    """
    letters_to_positions = defaultdict(list)

    for i, c in enumerate(S):
        letters_to_positions[c].append(i)

    for w in sorted(D, key=len, reverse=True):
        min_i = 0
        for c in w:
            if c not in letters_to_positions or not letters_to_positions[c]: break

            for i in letters_to_positions[c]:
                if i >= min_i:
                    min_i = i + 1
                    break
            else:
                break
        else:
            return w

    return ''


def string_splosion(s: str) -> str:
    """
    Description:
        https://techdevguide.withgoogle.com/paths/foundational/stringsplosion-problem-ccocodcode/
        http://codingbat.com/prob/p118366

        Given a non-empty string like "Code" return a string like "CCoCodCode".

        string_splosion('Code') → 'CCoCodCode'
        string_splosion('abc') → 'aababc'
        string_splosion('ab') → 'aab'

    Args:
        s: string to 💥

    Returns:
        Exploded string.

    """
    return ''.join([s[:i + 1] for i in range(len(s))])


def max_span(A: List[int]) -> int:
    """
    Description:
        https://techdevguide.withgoogle.com/paths/foundational/maxspan-problem-return-largest-span-array/
        http://codingbat.com/prob/p189576

        Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the
        number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found
        in the given array. (Efficiency is not a priority.)

        maxSpan([1, 2, 1, 1, 3]) → 4
        maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
        maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

    Args:
        A: list of ints.

    Returns:
        Longest span found in an array.
    """
    if not A: return 0

    l_idx, r_idx = dict(), dict()

    for i in range(len(A)):
        if A[i] not in l_idx:
            l_idx[A[i]] = i

    for i in reversed(range(len(A))):
        if A[i] not in r_idx:
            r_idx[A[i]] = i

    longest = 0

    for k, i in l_idx.items():
        if k in r_idx:
            longest = max(longest, r_idx[k] - i + 1)

    return longest
