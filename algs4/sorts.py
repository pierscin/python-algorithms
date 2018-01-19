from typing import Sequence


def selection_sort(A: Sequence) -> None:
    """Selection sort implementation.

    Starting from i = 0, find the smallest item in A[i:], exchange it with A[i], increment i.

    Invariants:
     - elements in A[0:i - 1] are in their final positions
     - all objects in A[i:] are >= than those in A[0:i - 1]

    Complexity:
        exchanges: N
        compares: N^2

    Args:
        A: sequence of comparable objects
    """
    for i in range(len(A) - 1):
        j = A.index(min(A[i:]), i)
        A[i], A[j] = A[j], A[i]


def insertion_sort(A: Sequence) -> None:
    """Insertion sort implementation.

    Pick one element and insert it in its place among already sorted part of a sequence (move larger items towards
    the end of an array). Very good for almost sorted sequences.

    Invariants:
     - elements in A[0:i - 1] are sorted

    Args:
        A: sequence of comparable objects
    """
    for i in range(1, len(A)):
        for j in reversed(range(i)):
            if A[j + 1] < A[j]:
                A[j + 1], A[j] = A[j], A[j + 1]
            else:
                break


def shell_sort(A: Sequence) -> None:
    """Shell sort implementation.

    Apply insertion sort for elements with distance h between them. Make h smaller.

    Step is calculated according to h = 3 * h + 1

    Invariants:
     - elements are h-sorted

    Args:
        A: sequence of comparable objects
    """

    h = 1
    while h < len(A) // 3: h = 3 * h + 1
    while h > 0:
        for i in range(h, len(A) + 1 - h):
            for j in reversed(range(0, i, h)):
                if A[j + h] < A[j]:
                    A[j + h], A[j] = A[j], A[j + h]
                else:
                    break
        h //= 3
