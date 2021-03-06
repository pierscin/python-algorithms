"""Problems from Leet Code.

Module consists of methods which DO NOT match signatures in problem description - there is no Solution object and types.

"""
from bisect import bisect, bisect_left
from itertools import product
from typing import List

from leet.utils import ListNode


def two_sum(nums: List[int], target: int) -> List[int]:
    """Two sum problem.

    Description:
        https://leetcode.com/problems/two-sum/description/

        1. Two Sum
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

        2. Add Two Numbers
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
        reverse order and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.

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

        3. Longest Substring Without Repeating Characters
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

        5. Longest Palindromic Substring
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


def convert(s: str, n: int) -> str:
    """Returns s represented as n-row zig-zag string.

    Description:
        https://leetcode.com/problems/zigzag-conversion/description/

        6. ZigZag Conversion
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Args:
        s: string.
        n: number of rows in zig-zag string.

    Returns:
        Zig-zag representation of s.
    """
    if not s: return ''

    i = 0
    rows = [[] for _ in range(n)]

    while True:
        for r in range(n):
            rows[r].append(s[i])
            i += 1
            if i == len(s): return ''.join([''.join(rows[i]) for i in range(n)])

        for r in reversed(range(1, n - 1)):
            rows[r].append(s[i])
            i += 1
            if i == len(s): return ''.join([''.join(rows[i]) for i in range(n)])


def reverse(x: int) -> int:
    """Reverses 32-bit int.

    Description:
        https://leetcode.com/problems/reverse-integer/description/

        7. Reverse Integer
        Given a 32-bit signed integer, reverse digits of an integer.

    Args:
        x: int to reverse.

    Returns:
        Reversed int within 32-bit bounds or 0 in case of overflow.
    """
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    minus = x < 0

    i = int(''.join(reversed(str(abs(x)))))
    i = -i if minus else i

    if i > INT_MAX or i < INT_MIN: return 0
    else: return i


def atoi(s: str) -> int:
    """Converts string to integer.

    Absolutely horribly specified problem. 😡😡😡

    Description:
        https://leetcode.com/problems/string-to-integer-atoi/description/

        8. String to Integer (atoi)
        Implement atoi to convert a string to an integer.

    Args:
        s: string.

    Returns:
        Converted string as int or 0 in case of overflows and invalid conversions.
    """
    INVALID_CONVERSION = 0
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    s = s.strip()

    # check validity
    if not s or not (s[0] in {'-', '+'} or s[0].isdigit()): return INVALID_CONVERSION

    # strip '-' or '+'
    minus = s[0] == '-'
    if s[0] in {'-', '+'}: s = s[1:]

    if not s: return INVALID_CONVERSION

    # strip zeros
    i = 0
    while i < len(s) and s[i] == '0':
        i += 1

    s = s[i:]

    if not s: return INVALID_CONVERSION

    # parse int
    i = 0
    while i < len(s) and s[i].isdigit():
        i += 1
        if i > 10: return INT_MIN if minus else INT_MAX

    if i == 0: return INVALID_CONVERSION

    result = -int(s[:i]) if minus else int(s[:i])

    # check bounds
    if result < INT_MIN: return INT_MIN
    if result > INT_MAX: return INT_MAX
    return result


def is_palindrome(x: int) -> bool:
    """Checks whether argument is a palindrome.

    Description:
        https://leetcode.com/problems/palindrome-number/description/

        9. Palindrome Number
        Determine whether an integer is a palindrome. Do this without extra space.

    Args:
        x: integer.

    Returns:
        Is x a palindrome.
    """
    if x < 0 or x > 0 and not x % 10: return False

    reversed_part = 0
    while x > reversed_part:
        reversed_part = reversed_part * 10 + x % 10
        x //= 10

    return x == reversed_part or x == reversed_part // 10


def max_area(heights: List[int]) -> int:
    """Calculate container with most water based on heights of containers.

    Description:
        https://leetcode.com/problems/container-with-most-water/description/

        11. Container With Most Water
        Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
        Find two lines, which together with x-axis forms a container, such that the container contains the most water.

        Note: You may not slant the container and n is at least 2.

    Args:
        heights: list with container heights

    Returns:
        Surface of the biggest possible container.
    """
    l, r, max_s = 0, len(heights) - 1, 0

    while l < r:
        d = r - l
        L, R = heights[l], heights[r]

        s = min(L, R) * d
        max_s = max(max_s, s)

        if L < R: l += 1
        else: r -= 1

    return max_s


def int_to_roman(x: int) -> str:
    """Converts int to roman numeral.

    Description:
        https://leetcode.com/problems/integer-to-roman/description/

        12. Integer to Roman
        Given an integer, convert it to a roman numeral.

        Input is guaranteed to be within the range from 1 to 3999.

    Args:
        x: number.

    Returns:
        x converted to roman numeral.
    """
    if x == 0: return ''

    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    parts = []
    i = 0

    while x > 0:
        if x >= arabic[i]:
            parts.append(roman[i])
            x -= arabic[i]
        else: i += 1

    return ''.join(parts)


def roman_to_int(s: str) -> int:
    """Converts roman numeral to integer.

    Description:
        https://leetcode.com/problems/roman-to-integer/description/

        13. Roman to Integer
        Given a roman numeral, convert it to an integer.

        Input is guaranteed to be within the range from 1 to 3999.

    Args:
        s: roman numeral.

    Returns:
        s converted to int.
    """
    if s == '': return 0

    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    x = 0
    start_idx = i = 0

    while start_idx < len(s):
        if s.startswith(roman[i], start_idx):
            start_idx += len(roman[i])
            x += arabic[i]
        else: i += 1

    return x


def longest_common_prefix(strs: List[str]) -> str:
    """Calculates longest common prefix from provided list of strings.

    Description:
        https://leetcode.com/problems/longest-common-prefix/description/

        14. Longest Common Prefix
        Write a function to find the longest common prefix string amongst an array of strings.
    Args:
        strs: list of strings to check.

    Returns:
        Longest common prefix
    """
    if not strs: return ''
    if len(strs) == 1: return strs[0]

    strs.sort()

    first, last = strs[0], strs[-1]
    prefix = []

    for i in range(1, len(first) + 1):
        if last.startswith(first[:i]): prefix.append(first[i - 1])
        else: break

    return ''.join(prefix)


def three_sum(nums: List[int]) -> List[List[int]]:
    """Solves three sum problem.

    Description:
        https://leetcode.com/problems/3sum/description/

        15. 3Sum
        Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique
        triplets in the array which gives the sum of zero.

        Note: The solution set must not contain duplicate triplets.

    Args:
        nums: list of integers.

    Returns:
        List of triplets that sum to 0.
    """
    results = []
    A = sorted(nums)

    i = 0
    while i < len(A) - 2:
        l, r = i + 1, len(A) - 1

        while l < r:
            s = A[i] + A[l] + A[r]
            if s == 0:
                results.append([A[i], A[l], A[r]])
                while l < r and A[r] == A[r - 1]: r -= 1
                while l < r and A[l] == A[l + 1]: l += 1
                l, r = l + 1, r - 1
            elif s > 0:
                r -= 1
            else:
                l += 1
        while i < len(A) - 2 and A[i] == A[i + 1]: i += 1
        i += 1

    return results


def three_sum_closest(nums: List[int], target: int) -> int:
    """Finds number which is nearest solution of three sum problem to the specific target.

    Description:
        https://leetcode.com/problems/3sum-closest/description/

        16. 3Sum Closest
        Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
        Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Args:
        nums: list of integers.
        target: target integer.

    Returns:
        Number which is nearest to the target after summing one of triplets.
    """
    A = sorted(nums)
    closest = A[0] + A[1] + A[-1]

    i = 0
    while i < len(A) - 2:
        l, r = i + 1, len(A) - 1

        while l < r:
            s = A[i] + A[l] + A[r]

            if s == target: return s
            else:
                closest = closest if abs(target - closest) < abs(target - s) else s

            if s < target:
                while l < r and A[l] == A[l + 1]: l += 1
                l += 1
            else:
                while l < r and A[r] == A[r - 1]: r -= 1
                r -= 1
        while i < len(A) - 2 and A[i] == A[i + 1]: i += 1
        i += 1

    return closest


def letter_combinations(digits: str) -> List[str]:
    """Returns all possible letter representations of a phone number.

    Description:
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

        17. Letter Combinations of a Phone Number
        Given a digit string, return all possible letter combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below.

        ---------
        | PHONE |
        | IMAGE |
        |   😉  |
        ---------

    Args:
        digits: digits in a number.

    Returns:
        List of all possible letter combinations from chosen digits.

    """
    if '' == digits: return []

    digits_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    possible_letters = [digits_to_letters[d] for d in digits]

    return list(''.join(p) for p in product(*possible_letters))


def n_sum(n: int, nums: List[int], target: int) -> List[List[int]]:
    """Returns list of lists of N numbers which sum to specified target.

    Args:
        n: order of problem.
        nums: list of integers to search through.
        target: target number to sum numbers to.

    Returns:
        List of solutions without duplicates
    """

    def _n_sum(n: int, partial: List[int], target: int, start: int) -> None:
        if sum(A[start:start + n]) > target or sum(A[-n:]) < target: return

        if n == 2:
            l, r = start, N - 1
            while l < r:
                s = A[l] + A[r]
                if s == target:
                    results.append(partial + [A[l], A[r]])
                    while l < r and A[r] == A[r - 1]: r -= 1
                    while l < r and A[l] == A[l + 1]: l += 1
                    l, r = l + 1, r - 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        else:
            for i in range(start, N - n + 1):
                if i == start or i > start and A[i - 1] != A[i]:  # pierscin: no duplicates without usage of set
                    _n_sum(n - 1, partial + [A[i]], target - A[i], i + 1)

    A = sorted(nums)
    N = len(A)
    results = []

    _n_sum(n, [], target, 0)
    return results


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """Returns list of quadruplets which sum to specified target.

    Description:
        https://leetcode.com/problems/4sum/description/

        18. 4Sum
        Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
        Find all unique quadruplets in the array which gives the sum of target.

        Note: The solution set must not contain duplicate quadruplets.

    Args:
        nums: list of integers to search through.
        target: target number to sum numbers to.

    Returns:
        List of solutions without duplicates
    """
    return n_sum(4, nums, target)


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    """Removes nth list node counting from tail.

    Description:
        https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

        19. Remove Nth Node From End of List
        Given a linked list, remove the nth node from the end of list and return its head.

        For example:
           Given linked list: 1->2->3->4->5, and n = 2.
           After removing the second node from the end, the linked list becomes 1->2->3->5.

        Note:
        Given n will always be valid.
        Try to do this in one pass.

    Args:
        head: head of list.
        n: number of node (counting from tail) to remove.

    Returns:
        Head of the modified list or None when the only element in singleton list was removed.
    """
    faster = slower = head

    for _ in range(n):
        faster = faster.next

    if faster is None: return head.next

    while faster.next:
        faster = faster.next
        slower = slower.next

    slower.next = slower.next.next

    return head


def are_parentheses_balanced(s: str) -> bool:
    """Check whether brackets in string are balanced.

    Description:
        https://leetcode.com/problems/valid-parentheses/description/

        20. Valid Parentheses
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
        string is valid.

        The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

    Args:
        s: string consisting of brackets only.

    Returns:
        True when input is valid, False otherwise.
    """
    stack = []

    left = {'(', '[', '{'}
    right_to_left = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in left: stack.append(c)
        elif c in right_to_left and stack and stack[-1] == right_to_left[c]: stack.pop()
        else: return False
    return not stack


def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """Merges two sorted lists into the new one which is sorted.

    Description:
        https://leetcode.com/problems/merge-two-sorted-lists/description/

        21. Merge Two Sorted Lists
        Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
        the nodes of the first two lists.

    Args:
        l1: sorted list
        l2: sorted list

    Returns:
        Merged list in sorted order or None when both lists were empty.
    """

    dummy = node = ListNode(None)

    while l1 and l2:
        val = min(l1.val, l2.val)

        if l1.val < l2.val: l1 = l1.next
        else: l2 = l2.next

        node.next = ListNode(val)
        node = node.next

    while l1:
        node.next = ListNode(l1.val)
        node, l1 = node.next, l1.next

    while l2:
        node.next = ListNode(l2.val)
        node, l2 = node.next, l2.next

    return dummy.next


def generate_parenthesis(n: int) -> List[str]:
    """Generate all possible valid n pairs of parenthesis.

    Description:
        https://leetcode.com/problems/generate-parentheses/description/

        22. Generate Parentheses
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        For example, given n = 3, a solution set is:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]

    Args:
        n: how many pairs of parenthesis in results.

    Returns:
        All possible valid n pairs of parenthesis in a list
    """
    def _generate(current, left, right):
        if right > left: return

        if right == left == n: results.append(''.join(current))
        else:
            if left < n: _generate(current + ['('], left + 1, right)
            if right < n: _generate(current + [')'], left, right + 1)

    results = []

    _generate([], 0, 0)

    return results


def swap_pairs(head: ListNode) -> ListNode:
    """Swaps all nodes of a list in-place.

    Description:
        https://leetcode.com/problems/swap-nodes-in-pairs/description/

        24. Swap Nodes in Pairs
        Given a linked list, swap every two adjacent nodes and return its head.

        For example,
        Given 1->2->3->4, you should return the list as 2->1->4->3.

        Your algorithm should use only constant space. You may not modify the values in the list,
        only nodes itself can be changed.

    Args:
        head: head of list to modify.

    Returns:
        Head to modified list.
    """
    dummy = node = ListNode(None)
    node.next = head

    while node.next and node.next.next:
        first = node.next
        second = node.next.next

        node.next, second.next, first.next = second, first, second.next

        node = first

    return dummy.next


def remove_duplicates(A: List[int]) -> int:
    """"Removes" duplicates from a list and returns length of a list with unique integers.

    Description:
        https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

        26. Remove Duplicates from Sorted Array
        Given a sorted array, remove the duplicates in-place such that each element appear only once
        and return the new length.

        Do not allocate extra space for another array, you must do this by modifying the input array in-place
        with O(1) extra memory.

    Args:
        A: sorted list of integers

    Returns:
        Length of a list with unique integers.
    """
    if not A: return 0

    L = 0

    for i in range(1, len(A)):
        if A[i] != A[L]:
            L += 1
            A[L] = A[i]

    return L + 1


def remove_element(A: List[int], x: int) -> int:
    """"Removes" all occurrences of x in A and returns new length of modified list A.

    Description:
        https://leetcode.com/problems/remove-element/description/

        27. Remove Element
        Given an array and a value, remove all instances of that value in-place and return the new length.

        Do not allocate extra space for another array, you must do this by modifying the input array in-place
        with O(1) extra memory.

        The order of elements can be changed. It doesn't matter what you leave beyond the new length.

    Args:
        A: list to search x in.
        x: searched number.

    Returns:
        Length of modified A with all x elements removed.
    """
    if not A: return 0

    L = 0

    for i in range(len(A)):
        if A[i] != x:
            A[L] = A[i]
            L += 1

    return L


def str_str(haystack: str, needle: str) -> int:
    """Finds index of needle in haystack.

    Description:
        https://leetcode.com/problems/implement-strstr/description/

        28. Implement strStr()
        Implement strStr().

        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Args:
        haystack: searched string.
        needle: string to look for.

    Returns:
        Index of needle in haystack, -1 when not found
    """
    return haystack.find(needle)


def divide(dividend: int, divisor: int) -> int:
    """Divides two 32-bit integers WITHOUT using *, / and % operators.

    Description:
        https://leetcode.com/problems/divide-two-integers/description/

        29. Divide Two Integers
        Divide two integers without using multiplication, division and mod operator.

        If it is overflow, return MAX_INT.

    Args:
        dividend: int
        divisor: int

    Returns:
        Signed 32-bit result of integer division

    """

    MIN_INT, MAX_INT = -2147483648, 2147483647

    if dividend == 0 or abs(divisor) > abs(dividend): return 0

    if divisor == 1: return dividend
    if divisor == -1:
        if dividend == MIN_INT: return MAX_INT
        return -dividend

    positive = dividend < 0 and divisor < 0 or dividend > 0 and divisor > 0

    divisor, dividend = abs(divisor), abs(dividend)

    res = 0

    while dividend >= divisor:
        power = 0
        while dividend > divisor << power + 1:
            power += 1
        dividend -= divisor << power
        res += 1 << power
    return res if positive else -res


def next_permutation(A: List[int]) -> None:
    """Finds next permutation of integers in A and modifies this list to reflect it.

    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    Description:
        https://leetcode.com/problems/next-permutation/description/

        31. Next Permutation
        Implement next permutation, which rearranges numbers into the lexicographically next greater permutation
        of numbers.

        If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending
        order).

        The replacement must be in-place, do not allocate extra memory.

    Args:
        A: list of ints to modify
    """
    for k in reversed(range(len(A) - 1)):
        if A[k + 1] > A[k]: break
    else:
        A[:] = list(reversed(A))  # pierscin: task doesn't allow returning list(reversed(A))... 😡
        return

    for l in reversed(range(k + 1, len(A))):
        if A[k] < A[l]:
            A[k], A[l] = A[l], A[k]
            break

    A[k + 1:] = list(reversed(A[k + 1:]))


def search(A: List[int], x: int) -> int:
    """Returns index of x in sorted (but could be rotated by n) list.

    Description:
        https://leetcode.com/problems/search-in-rotated-sorted-array/description/

        33. Search in Rotated Sorted Array
        Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
        (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

        You are given a target value to search. If found in the array return its index, otherwise return -1.
        You may assume no duplicate exists in the array.

    Args:
        A: sorted and optionally rotated list.
        x: target.

    Returns:
        Index of x or -1 when not found.
    """
    NOT_FOUND = -1

    if not A: return NOT_FOUND

    N = len(A)
    lo, hi = 0, N - 1

    while lo != hi:
        mid = (lo + hi) // 2

        if A[mid] > A[hi]: lo = mid + 1
        else: hi = mid

    rot = lo

    lo, hi = 0, N - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        r_mid = (mid + rot) % N

        if A[r_mid] == x: return r_mid
        elif A[r_mid] > x: hi = mid - 1
        else: lo = mid + 1

    return NOT_FOUND


def search_range(A, x) -> List[int]:
    """Finds inclusive range of indexes of x in a sorted array.

    Description:
        https://leetcode.com/problems/search-for-a-range/description/

        34. Search for a Range
        Given an array of integers sorted in ascending order, find the starting and ending position of a given target
        value.

        Your algorithm's runtime complexity must be in the order of O(log n).

        If the target is not found in the array, return [-1, -1].

    Args:
        A: sorted list.
        x: target.

    Returns:
        Range of indexes of x.
    """

    NOT_FOUND = [-1, -1]

    if not A: return NOT_FOUND

    l, r = bisect_left(A, x), bisect(A, x)

    if A[r - 1] == x: return [l, r - 1]

    return NOT_FOUND


def search_insert(A: List[int], x: int) -> int:
    """Searches insertion point for x in sorted list A, so that A remains sorted after it.

    More generic version of this problem (with duplicates) is often referred to as "upper bound".

    Descriptions:
        https://leetcode.com/problems/search-insert-position/description/

        35. Search Insert Position
        Given a sorted array and a target value, return the index if the target is found. If not, return the index
        where it would be if it were inserted in order.

        You may assume no duplicates in the array.

    Args:
        A: sorted list.
        x: target value.

    Returns:
        Index to insert x, so that A remains sorted.
    """
    i = bisect(A, x)
    return i - 1 if A[i - 1] == x else i  # pierscin: when i == 0 the A[-1] is checked, but array is sorted, so it works


def find_words(words: List[str]) -> List[str]:
    """Calculates words which can be written with only one row of keyboard keys.

    Description:
        500. Keyboard Row

        Given a List of words, return the words that can be typed using letters of alphabet on only one row's of
        American keyboard like the image below.

        ------------
        | KEYBOARD |
        |   IMAGE  |
        |    😉    |
        ------------

    Link:
        https://leetcode.com/problems/keyboard-row/description/

    Args:
        words: words to check.

    Returns:
        List of words which could be written with only 1 row of keyboard keys.
    """
    rows = [
        set('QWERTYUIOPqwertyuiop'),
        set('ASDFGHJKLasdfghjkl'),
        set('ZXCVBNMzxcvbnm')
    ]

    res = []

    for w in words:
        for row in rows:
            if set(w) <= row:
                res.append(w)
                break

    return res

def distribute_candies(candies: List[int]) -> int:
    """Calculates max number of candies kinds which can be given to sister.

    Description:
        575. Distribute Candies

        Given an integer array with even length, where different numbers in this array represent different kinds of
        candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in
        number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

    Link:
        https://leetcode.com/problems/distribute-candies/description/

    Args:
        candies: list of ints

    Returns:
        Max number of candies taken by sister.
    """
    k = len(set(candies))

    return min(len(candies) // 2, k)
