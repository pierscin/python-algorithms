from collections import defaultdict
from typing import Set, List


def find_longest_subsequence(S: str, D: Set[str]) -> str:
    """
    Description:
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

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string/

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

            for i in letters_to_positions[c]:  # TODO: pierscin: bisect
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
        Given a non-empty string like "Code" return a string like "CCoCodCode".

        string_splosion('Code') → 'CCoCodCode'
        string_splosion('abc') → 'aababc'
        string_splosion('ab') → 'aab'

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/stringsplosion-problem-ccocodcode/

    Args:
        s: string to 💥

    Returns:
        Exploded string.
    """
    return ''.join([s[:i + 1] for i in range(len(s))])


def max_span(A: List[int]) -> int:
    """
    Description:
        Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the
        number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found
        in the given array. (Efficiency is not a priority.)

        max_span([1, 2, 1, 1, 3]) → 4
        max_span([1, 4, 2, 1, 4, 1, 4]) → 6
        max_span([1, 4, 2, 1, 4, 4, 4]) → 6

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/maxspan-problem-return-largest-span-array/

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


def without_string(s: str, r: str) -> str:
    """
    Description:
        Given two strings, base and remove, return a version of the base string where all instances of the remove string
        have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only
        non-overlapping instances, so with "xxx" removing "xx" leaves "x".

        withoutString("Hello there", "llo") → "He there"
        withoutString("Hello there", "e") → "Hllo thr"
        withoutString("Hello there", "x") → "Hello there"

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/withoutstring-problem-strings-base-remove-return/

    Args:
        s: base string.
        r: string to remove.

    Returns:
        s with removed occurrences of r.
    """
    if not r or len(r) > len(s): return s
    if not s: return ''

    lower_s, lower_r = s.lower(), r.lower()

    res = []

    i, S, R = 0, len(s), len(r)
    while i <= S - R:
        if lower_s[i:i + R] == lower_r: i += R
        else:
            res.append(s[i])
            i += 1

    if i < S: res.append(s[i:])

    return ''.join(res)


def sum_numbers(s: str) -> int:
    """
    Description:
        Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number
        is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of
        the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

        sum_numbers("abc123xyz") → 123
        sum_numbers("aa11b33") → 44
        sum_numbers("7 11") → 18

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/subnumbers-problem-string-return-sum/

    Args:
        s: string.

    Returns:
        Sum of all numbers in a string.
    """
    if not s: return 0

    i, res = 0, 0

    while i < len(s):
        if s[i].isdigit():
            j = i + 1

            while j < len(s) and s[j].isdigit(): j += 1

            res += int(s[i:j])
            i = j
        else: i += 1

    return res


def can_balance(A: List[int]) -> bool:
    """
    Description:
        Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on
        one side is equal to the sum of the numbers on the other side.

        can_balance([1, 1, 1, 2, 1]) → true
        can_balance([2, 1, 1, 2, 1]) → false
        can_balance([10, 10]) → true

    Link:
        https://techdevguide.withgoogle.com/paths/foundational/canbalance-problem-arrays-non-empty/

    Returns:
        Is list possible to balance.
    """
    if len(A) < 2: return False

    split_point = 1
    sum_l, sum_r = A[split_point - 1], sum(A[split_point:])

    while sum_l != sum_r and split_point < len(A) - 1:
        diff = A[split_point]
        sum_l, sum_r = sum_l + diff, sum_r - diff
        split_point += 1

    return sum_l == sum_r
