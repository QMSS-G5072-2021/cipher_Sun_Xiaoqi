import pytest

def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

@pytest.mark.parametrize("example,shift,expected",[
    ('data',1,'ebub'),
    ('hello',1,'ifmmp'),
    ('DATA',1,'EBUB'),
    ('I love data science',1,'J mpwf ebub tdjfodf')
])

class Testgroup:
    def test_cipher_single(self, example,shift,expected ):
        actual = cipher(example, shift)
        assert actual == expected
    def test_cipher_negative(self,example,shift,expected):
        actual = cipher(example,shift)
        assert actual == expected
    def test_cipher_symbol(self,example,shift,expected):
        actual = cipher(example,shift)
        assert actual == expected
