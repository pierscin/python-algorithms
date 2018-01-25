from typing import Optional, List


def find_nth(haystack: str, needle: str, n: int, start:Optional[int]=None, end:Optional[int]=None) -> int:
    offset, end = start if start else 0, end if end else len(haystack)

    i = haystack.find(needle, offset, end)
    while i != -1 and n > 1:
        i = haystack.find(needle, i + len(needle), end)
        n -= 1
    return i


def decompress(s: str) -> str:
    """
    Description:
        In this exercise, you're going to decompress a compressed string.
        Your input is a compressed string of the format number[string] and the decompressed output form should be the
        string written number times. For example:

        3[abc]4[ab]c → abcabcabcababababc

        - Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
        - One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
        - Characters allowed as input include digits, small English letters and brackets [ ].
        - Digits are only to represent amount of repetitions.
        - Letters are just letters.
        - Brackets are only part of syntax of writing repeated substring.
        - Input is always valid, so no need to check its validity.

    Link:
        https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/

    Args:
        s: compressed string.

    Returns:
        Decompressed string.
    """
    def _decompress(start: int, end: int) -> List[str]:
        left = s.find('[', start, end)
        first_right = s.find(']', start, end)

        if left == first_right == -1: return list(s[start:end])  # pierscin: only letters in []
        if s[left:first_right] == '': return []  # pierscin: empty string in []

        count_of_left = s.count('[', start, first_right)
        right = find_nth(s, ']', count_of_left, start, end)

        res = []
        for i in range(start, left):
            if s[i].isalpha(): res.append(s[i])
            else:
                number = int(s[i:left])
                break
        else:
            number = 1

        if '[' in s[left + 1: right + 1]:  # pierscin: nested expression
            res += number * _decompress(left + 1, right + 1)
        else:
            res += number * _decompress(left + 1, right) + _decompress(right + 1, end)

        # pierscin: letters after brackets
        i = right + 1
        while i < end and s[i].isalpha():
            res.append(s[i])
            i += 1

        return res

    s = '1[' + s[:] + ']'

    return ''.join(_decompress(0, len(s)))

