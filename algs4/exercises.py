from typing import Iterable, Sequence


def insert_left_parentheses(e):
    """Inserts left parentheses to imbalanced expression without them.

    Left parentheses are inserted according to the example in exercise 1.3.9 (full content below).
    This is NOT the only correct way.

    1.3.9

    Write a program that takes from standard input an expression without left parentheses and prints
    the equivalent infix expression with the parentheses inserted.
    For example, given the input:
        1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )
    your program should print:
        ( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) ) pierscin: my correction - expression in book was imbalanced

     Args:
        e (str): String with infix expression and without left parentheses. Every element should be separated by
            at least 1 whitespace character.

    Returns:
        str: Expression with balanced parentheses.
    """
    tokens = e.split()
    stack = []
    for t in tokens:
        if t == ')':
            r, o, l = stack.pop(), stack.pop(), stack.pop()
            stack.append(' '.join(['(', l, o, r, ')']))
        else:
            stack.append(t)
    return stack.pop()


def infix_to_postfix(e):
    """Converts infix expression to its postfix equivalent.

    Expression can contain brackets, symbols and one of the following operators:
        '*' - multiply
        '/' - divide
        '-' - subtract
        '+' - add
        '^' - power

    This method is connected to exercise 1.3.10 (full content below).

    1.3.10

    Write a filter InfixToPostfix that converts an arithmetic expression from infix to postfix.

    Args:
        e (str): String with infix expression. Every element should be separated by at least 1 whitespace character.

    Returns:
        str: Infix expression converted to its postfix form.
    """
    op_to_precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    right_associative_ops = {'^'}

    tokens = e.split()
    op_stack, output = [], []

    for t in tokens:
        if t == '(':
            op_stack.append(t)
        elif t == ')':
            while op_stack[-1] != '(':
                output.append(op_stack.pop())
            op_stack.pop()  # to get rid of '('
        elif t in op_to_precedence:
            while op_stack \
                    and op_stack[-1] != '(' \
                    and (op_to_precedence[op_stack[-1]] > op_to_precedence[t] or
                        t not in right_associative_ops and op_to_precedence[op_stack[-1]] >= op_to_precedence[t]):
                output.append(op_stack.pop())
            op_stack.append(t)
        else:
            output.append(t)
    while op_stack:
        output.append(op_stack.pop())
    return ' '.join(output)


def rpn(e):
    """Reverse Polish Notation (RPN) calculator.

    Evaluates float value of an expression string given in postfix notation.

    Implemented operators:
        'r' - reverse value (1 argument)
        '*' - multiply (2 arguments)
        '/' - divide (2 arguments)
        '-' - subtract (2 arguments)
        '+' - add (2 arguments)

    This method is connected to exercise 1.3.11 (full content below).

    1.3.11

    Write a program EvaluatePostfix that takes a postfix expression from standard input,
    evaluates it and prints the value.

    Args:
        e (str): String with postfix expression. Every element should be separated by at least 1 whitespace character.

    Returns:
        float: Evaluated value of an expression as float number.
    """
    op_to_strategy = {
        'r': (1, lambda x: -x),
        '*': (2, lambda x, y: y * x),
        '/': (2, lambda x, y: y / x),
        '-': (2, lambda x, y: y - x),
        '+': (2, lambda x, y: y + x)
    }

    tokens = e.split()
    stack = []

    for t in tokens:
        if t in op_to_strategy:
            no_of_args, strategy = op_to_strategy[t][0], op_to_strategy[t][1]
            stack.append(strategy(*[stack.pop() for _ in range(no_of_args)]))
        else:
            stack.append(float(t))

    return stack.pop()


def sorted_intersection(A, B):
    """Common elements of both iterables in sorted order.

    This method is connected to exercise 1.4.12 (full content below).

    1.4.12

    Write a program that, given two sorted arrays of N int values, prints all elements that appear in both arrays,
    in sorted order. The running time of your program should be proportional to N in the worst case.

    Args:
        A (Iterable): iterable with sortable elements
        B (Iterable): iterable with sortable elements

    Returns:
        list: sorted intersection of sequences
    """
    return sorted(set(A) & set(B))


def three_sum(iterable):
    """Count number of triples in iterable that sum to 0.

    This method is connected to exercise 1.4.15 (full content below).

    1.4.15

    Faster 3-sum. As a warm-up, develop an implementation TwoSumFaster that uses a linear algorithm to count the pairs
    that sum to zero after the array is sorted (instead of the binary-search-based linearithmic algorithm).
    Then apply a similar idea to develop a quadratic algorithm for the 3-sum problem.

    Args:
        iterable (Iterable): numbers

    Returns:
        int: number of triples in A that sum to 0
    """
    A = sorted(iterable)
    i = 0
    count = 0

    while i < len(A) - 2:
        l, r = i + 1, len(A) - 1

        while l < r:
            s = A[i] + A[l] + A[r]
            if s == 0:
                count += 1
                while l < r and A[r] == A[r - 1]: r -= 1
                while l < r and A[l] == A[l + 1]: l += 1
                l, r = l + 1, r - 1
            elif s > 0:
                r -= 1
            else:
                l += 1
        while i < len(A) - 2 and A[i] == A[i + 1]: i += 1
        i += 1

    return count


def closest_pair(iterable):
    """Returns closest (in absolute value) pair of numbers in iterable.

    This method is connected to exercise 1.4.16 (full content below).

    1.4.16

    Closest pair (in one dimension). Write a program that, given an array a[] of N double values, finds a closest pair:
    two values whose difference is no greater than the the difference of any other pair (in absolute value).
    The running time of your program should be linearithmic in the worst case.

    Args:
        iterable (Iterable): numbers

    Returns:
        tuple: pair of closest numbers
    """
    A = sorted(iterable)
    closest = abs(A[1] - A[0])
    l = 0

    for i in range(1, len(A) - 1):
        current = abs(A[i] - A[i + 1])
        if current < closest:
            closest, l = current, i
            if closest == 0: break
    return A[l], A[l + 1]


def farthest_pair(iterable):
    """Returns farthest (in absolute value) pair of numbers in iterable.

    This method is connected to exercise 1.4.17 (full content below).

    1.4.17

    Farthest pair (in one dimension). Write a program that, given an array a[] of N double values, finds a farthest pair:
    two values whose difference is no smaller than the the difference of any other pair (in absolute value).
    The running time of your program should be linear in the worst case.

    Args:
        iterable (Iterable): numbers

    Returns:
        tuple: pair of farthest numbers
    """
    return min(iterable), max(iterable)


def local_min(sequence):
    """Returns index of a local minimum of distinct numbers sequence. More assumptions in docstring.

    This method is connected to exercise 1.4.18 (full content below), but there should be one correction and another
    assumption for it in order to be solve task in logarithmic time:
     - a[i-1] < a[i] < a[i+1] -> a[i-1] > a[i] < a[i+1]
     - "first two numbers are decreasing and last two numbers are increasing".
       This deals with case e.g. [6, -1000, 5, 4, 3, 2, 1].

    1.4.18

    Local minimum of an array. Write a program that, given an array a[] of N distinct integers, finds a local minimum:
    an index i such that a[i-1] < a[i] < a[i+1]. Your program should use ~2lg N compares in the worst case.

    Args:
        sequence (Sequence): sequence of numbers

    Returns:
        int: index of a local minimum

    Raises:
        ValueError: when local minimum is not found
    """
    A = sequence

    lo, hi = 0, len(A) - 1

    while lo < hi:
        mid = (hi + lo) // 2
        if A[mid - 1] > A[mid] < A[mid + 1]: return mid

        if A[mid - 1] < A[mid + 1]:
            hi = mid - 1
        else:
            lo = mid + 1

    raise ValueError("No local minimum found - sequence doesn't fulfill all assumptions.")

