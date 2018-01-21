"""Problems from Leet Code.

Module consists of methods which DO NOT match signatures in problem description - there is no Solution object and types.

"""
import itertools
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


def my_atoi(s: str) -> int:
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

    return list(''.join(p) for p in itertools.product(*possible_letters))


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
