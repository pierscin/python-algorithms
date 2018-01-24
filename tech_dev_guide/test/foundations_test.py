from tech_dev_guide.foundations import find_longest_subsequence, string_splosion, max_span, sum_numbers, without_string, \
    can_balance, interpret, encoder, blackjack, evenly_spaced, make_bricks


def test_find_longest_subsequence():
    S, D = "abppplee", {"able", "ale", "apple", "bale", "kangaroo"}

    assert find_longest_subsequence(S, D) == 'apple'


def test_string_splosion():
    assert string_splosion('Code') == 'CCoCodCode'
    assert string_splosion('abc') == 'aababc'
    assert string_splosion('ab') == 'aab'
    assert string_splosion('x') == 'x'
    assert string_splosion('fade') == 'ffafadfade'
    assert string_splosion('There') == 'TThTheTherThere'
    assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
    assert string_splosion('Bye') == 'BByBye'
    assert string_splosion('Good') == 'GGoGooGood'
    assert string_splosion('Bad') == 'BBaBad'


def test_max_span():
    assert max_span([1, 2, 1, 1, 3]) == 4
    assert max_span([1, 4, 2, 1, 4, 1, 4]) == 6
    assert max_span([1, 4, 2, 1, 4, 4, 4]) == 6
    assert max_span([3, 3, 3]) == 3
    assert max_span([3, 9, 3]) == 3
    assert max_span([3, 9, 9]) == 2
    assert max_span([3, 9]) == 1
    assert max_span([3, 3]) == 2
    assert max_span([]) == 0
    assert max_span([1]) == 1


def test_without_string():
    assert without_string("Hello there", "llo") == "He there"
    assert without_string("Hello there", "e") == "Hllo thr"
    assert without_string("Hello there", "x") == "Hello there"
    assert without_string("abxxxxab", "xx") == "abab"
    assert without_string("abxxxab", "xx") == "abxab"
    assert without_string("abxxxab", "x") == "abab"
    assert without_string("xxx", "x") == ""
    assert without_string("xxx", "Xx") == "x"
    assert without_string("xyzzy", "Y") == "xzz"
    assert without_string("", "x") == ""
    assert without_string("abcabc", "b") == "acac"
    assert without_string("AA22bb", "2") == "AAbb"
    assert without_string("1111", "1") == ""
    assert without_string("1111", "11") == ""
    assert without_string("MkjtMkx", "Mk") == "jtx"
    assert without_string("Hi HoHo", "Ho") == "Hi "


def test_sum_numbers():
    assert sum_numbers('abc123xyz') == 123
    assert sum_numbers('aa11b33') == 44
    assert sum_numbers('7 11') == 18
    assert sum_numbers('Chocolate') == 0
    assert sum_numbers('5hoco1a1e') == 7
    assert sum_numbers('5$$1;;1!!') == 7
    assert sum_numbers('a1234bb11') == 1245
    assert sum_numbers('') == 0
    assert sum_numbers('a22bbb3') == 25


def test_can_balance():
    assert can_balance([10, 10])
    assert can_balance([1, 1, 1, 2, 1])
    assert can_balance([1, 1, 1, 1, 4])
    assert can_balance([1, 1, 1, 2, 1])
    assert can_balance([10, 0, 1, -1, 10])
    assert can_balance([1, 2, 3, 1, 0, 2, 3])

    assert not can_balance([1])
    assert not can_balance([2, 1, 1, 2, 1])
    assert not can_balance([2, 1, 1, 1, 4])
    assert not can_balance([2, 3, 4, 1, 2])
    assert not can_balance([1, 2, 3, 1, 0, 1, 3])


def test_interpret():
    assert interpret(1, ['+'], [1]) == 2
    assert interpret(4, ['-'], [2]) == 2
    assert interpret(1, ['+', '*'], [1, 3]) == 6
    assert interpret(3, ['*'], [4]) == 12
    assert interpret(0, ['?'], [4]) == -1
    assert interpret(1, ['+', '*', '-'], [1, 3, 2]) == 4


def test_encoder():
    assert encoder(['a'], ['1', '2', '3', '4']) == ['1']
    assert encoder(['a', 'b'], ['1', '2', '3', '4']) == ['1', '2']
    assert encoder(['a', 'b', 'a'], ['1', '2', '3', '4']) == ['1', '2', '1']
    assert encoder(['a', 'a'], ['1', '2', '3', '4']) == ['1', '1']
    assert encoder(['a', 'b', 'b'], ['1', '2', '3', '4']) == ['1', '2', '2']
    assert encoder(['a', 'b', 'a'], ['1', '2', '3', '4']) == ['1', '2', '1']
    assert encoder(['a', 'b', 'c'], ['1', '2', '3', '4']) == ['1', '2', '3']


def test_blackjack():
    assert blackjack(19, 21) == 21
    assert blackjack(21, 19) == 21
    assert blackjack(19, 22) == 19
    assert blackjack(22, 19) == 19
    assert blackjack(22, 50) == 0
    assert blackjack(22, 22) == 0
    assert blackjack(33, 1) == 1
    assert blackjack(1, 2) == 2
    assert blackjack(34, 33) == 0
    assert blackjack(17, 19) == 19
    assert blackjack(18, 17) == 18
    assert blackjack(16, 23) == 16
    assert blackjack(3, 4) == 4
    assert blackjack(3, 2) == 3
    assert blackjack(21, 20) == 21


def test_evenly_spaced():
    assert evenly_spaced(2, 4, 6)
    assert evenly_spaced(4, 6, 2)
    assert evenly_spaced(6, 2, 4)
    assert evenly_spaced(2, 2, 2)
    assert evenly_spaced(9, 10, 11)
    assert evenly_spaced(10, 9, 11)

    assert not evenly_spaced(4, 6, 3)
    assert not evenly_spaced(6, 2, 8)
    assert not evenly_spaced(2, 2, 3)
    assert not evenly_spaced(2, 4, 4)
    assert not evenly_spaced(2, 2, 4)
    assert not evenly_spaced(3, 6, 12)
    assert not evenly_spaced(10, 9, 9)
    assert not evenly_spaced(12, 3, 6)


def test_make_bricks():
    assert make_bricks(3, 1, 8)
    assert make_bricks(3, 2, 10)
    assert make_bricks(3, 2, 8)
    assert make_bricks(6, 1, 11)
    assert make_bricks(1, 4, 11)
    assert make_bricks(0, 3, 10)
    assert make_bricks(3, 1, 7)
    assert make_bricks(2, 1, 7)
    assert make_bricks(7, 1, 11)
    assert make_bricks(7, 1, 8)
    assert make_bricks(43, 1, 46)
    assert make_bricks(40, 2, 47)
    assert make_bricks(40, 2, 50)
    assert make_bricks(0, 2, 10)
    assert make_bricks(20, 0, 19)
    assert make_bricks(20, 4, 39)
    assert make_bricks(1000000, 1000, 1000100)

    assert not make_bricks(40, 1, 46)
    assert not make_bricks(7, 1, 13)
    assert not make_bricks(1, 1, 7)
    assert not make_bricks(1, 4, 12)
    assert not make_bricks(6, 0, 11)
    assert not make_bricks(3, 2, 9)
    assert not make_bricks(3, 1, 9)
    assert not make_bricks(20, 0, 21)
    assert not make_bricks(20, 4, 51)
    assert not make_bricks(40, 2, 52)
    assert not make_bricks(22, 2, 33)
    assert not make_bricks(2, 1000000, 100003)
