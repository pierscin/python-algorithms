from geeks.boggle import BoggleGraph


def test_geeks_example():
    boggle = [['G', 'I', 'Z'], ['U', 'E', 'K'], ['Q', 'S', 'E']]

    bg = BoggleGraph(boggle, is_word=lambda s: s in {"GEEKS", "FOR", "QUIZ", "GO"})

    assert bg.unique_words == {'GEEKS', 'QUIZ'}
