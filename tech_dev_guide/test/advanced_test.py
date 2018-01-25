from tech_dev_guide.advanced import decompress


def test_decompress():
    assert decompress('') == ''
    assert decompress('a') == 'a'
    assert decompress('[]') == ''
    assert decompress('a[]') == 'a'
    assert decompress('a[]b') == 'ab'
    assert decompress('10[a]') == 'a' * 10
    assert decompress('3[3[ab2[c]]]') == 3 * 3 * ('ab' + 2 * 'c')
    assert decompress('3[abc]4[ab]c') == 3 * 'abc' + 4 * 'ab' + 'c'
    assert decompress('2[3[a]b]c') == 2 * (3 * 'a' + 'b') + 'c'

    many = 100
    malicious_input = many * '[' + 'a' + ']' * many
    assert decompress(malicious_input) == 'a'
