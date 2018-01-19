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

