from pytest import approx
from algs4.exercises import insert_left_parentheses, infix_to_postfix, rpn


def test_insert_left_parentheses():
    assert insert_left_parentheses('1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )') == '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )'


def test_infix_to_postfix():
    assert infix_to_postfix('3 + 4') == '3 4 +'
    assert infix_to_postfix('3 + 4 * ( 2 - 1 )') == '3 4 2 1 - * +'
    assert infix_to_postfix('A + B * C + D') == 'A B C * + D +'
    assert infix_to_postfix('( A + B ) * ( C + D )') == 'A B + C D + *'
    assert infix_to_postfix('A * B + C * D') == 'A B * C D * +'
    assert infix_to_postfix('A + B + C + D') == 'A B + C + D +'
    assert infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3') == '3 4 2 * 1 5 - 2 3 ^ ^ / +'


def test_rpn():
    assert rpn('2 7 + 3 / 14 3 - 4 * + 2 / r') == approx(-23.5)
