from geeks.boggle import find_words


def test_geeks_example():
    boggle = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]

    assert find_words(boggle, is_word=lambda s: s in {"GEEKS", "FOR", "QUIZ", "GO"}) == {'GEEKS', 'QUIZ'}
