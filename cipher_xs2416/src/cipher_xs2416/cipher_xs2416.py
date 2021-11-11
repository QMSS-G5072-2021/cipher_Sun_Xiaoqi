def cipher(text, shift, encrypt=True):
    """Cipher function to encrypt and decrypt a string .

    Parameters
    ----------
    text: str
        A string variable that is a text.
    shift: int
        The number of postions we would like to shift along the alphabet string.
    encrypt: bool
        Whether to encrypt or decrypt the string text.

    Returns
    -------
    str
        The new text string after being enctypted or decrypted.

    Examples
    --------
    >>> cipher('data',1)
    'ebub'

    """

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
