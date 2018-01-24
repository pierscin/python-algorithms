from tech_dev_guide.foundations import find_longest_subsequence, string_splosion, max_span


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
