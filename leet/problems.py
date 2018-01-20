"""Problems from Leet Code.

Module consists of methods which DO NOT match signatures in problem description - there is no Solution object and types.

"""
from typing import List

from leet.utils import ListNode


def two_sum(nums: List[int], target: int) -> List[int]:
    """Two sum problem.

    Description:
        https://leetcode.com/problems/two-sum/description/

        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Args:
        nums: list of numbers with exactly one solution to the problem.
        target: target number of the two sum.

    Returns:
        Indices of the two numbers which add up to a target.
    """
    x_to_i = {x: i for i, x in enumerate(nums)}
    for i, x in enumerate(nums):
        missing = target - x
        if missing in x_to_i and x_to_i[missing] != i:
            return [i, x_to_i[missing]]
        x_to_i[x] = i  # pierscin: two different elements, but with same values are permitted


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """Addition of two numbers with digits in linked lists.

    Description:
        https://leetcode.com/problems/add-two-numbers/description/

        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Args:
        l1: digits of first number.
        l2: digits of second number.

    Returns:
        Added numbers represented as digits in linked list.
    """
    node = dummy = ListNode(None)
    carry = 0

    while l1 or l2 or carry:
        val = carry

        if l1: val, l1 = val + l1.val, l1.next
        if l2: val, l2 = val + l2.val, l2.next

        carry, val = divmod(val, 10)

        node.next = ListNode(val)
        node = node.next

    return dummy.next


def length_of_longest_substring(s: str) -> int:
    """Finds length of the longest substring without repeating characters.

    Description:
        https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

        Given a string, find the length of the longest substring without repeating characters.

    Args:
        s: string.

    Returns:
        Length of the longest substring without repeating characters.
    """
    if not s: return 0

    L, a_to_i, start_char = 0, {}, s[0]

    for i, c in enumerate(s):
        if c in a_to_i and a_to_i[c] >= a_to_i[start_char]:
            L = max(L, i - a_to_i[start_char])
            start_char = s[a_to_i[c] + 1]
        a_to_i[c] = i

    return max(L, len(s) - a_to_i[start_char])


def longest_palindrome(s: str) -> str:
    """Finds longest palindromic substring in s.

    Description:
        https://leetcode.com/problems/longest-palindromic-substring/description/

        Given a string s, find the longest palindromic substring in s. You may assume that the maximum
        length of s is 1000.

    Args:
        s: string.

    Returns:
        Longest palindromic substring in s.
    """

    if len(s) < 2: return s

    def palindrome_in_s(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l - 1, r + 1
        return s[l + 1:r]

    p, s = [], list(s)

    for i in range(len(s)):
        p = max(palindrome_in_s(i, i),
                palindrome_in_s(i, i + 1),
                p,
                key=len)

    return ''.join(p)
