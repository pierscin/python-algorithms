

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
        e: String with infix expression. Every element should be separated by at least 1 whitespace character.

    Returns:
        Infix expression converted to its postfix form.
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
        e: String with postfix expression. Every element should be separated by at least 1 whitespace character.

    Returns:
        Evaluated value of an expression as float number.
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

