# -------------------------------------------------------------------------------------------------
#                                             Keymaker
# -------------------------------------------------------------------------------------------------
#
#       Based on lower case letters, the program use a couple of smaller algorithms to hashed given
# the word. The program refers to a custom hashing algorithm created by the legendary character
# known as Keymaker from the Matrix.
#
# -------------------------------------------------------------------------------------------------


# ---------------------------------------- main functions -----------------------------------------

def shift_characters(word: str, shift: int) -> str:
    """
    Returns the characters of the word, all shifted by shift. Shifting a character means adding
    a number to the original character value. If the resulting character would step out from
    the a-z region, continue the counting from the other end.

        shift_characters('abby', 5), returns:
        'fggd'
    """
    shifted_word = ""
    for letter in word:
        letter_index = ALPHABET.index(letter)
        shift_distance = letter_index + shift

        # values greater than the alphabet
        while shift_distance > ALPHABET_SIZE:
            shift_distance -= ALPHABET_SIZE
        # values smaller than the alphabet
        while shift_distance < 0:
            shift_distance = ALPHABET_SIZE + shift_distance

        shifted_word += ALPHABET[shift_distance]
    return shifted_word


def pad_up_to(word, shift, n):
    """
    >>> pad_up_to('abb', 5, 11)
    ... 'abbfggkllpq'
    """
    pass


def abc_mirror(word):
    """
    >>> abc_mirror('abcd')
    ... 'zyxw'
    """
    pass


def create_matrix(word1, word2):
    """
    >>> create_matrix('mamas', 'papas')
    ... ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    pass


def zig_zag_concatenate(matrix):
    """
    >>> zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
    ... 'adgjkhebcfil'
    """
    pass


def rotate_right(word, n):
    """
    >>> rotate_right('abcdefgh', 3)
    ... 'fghabcde'
    """
    pass


def get_square_index_chars(word):
    """
    >>> get_square_index_chars('abcdefghijklm')
    ... 'abej'
    """
    pass


def remove_odd_blocks(word, block_length):
    """
    >>> remove_odd_blocks('abcdefghijklm', 3)
    ... 'abcghim'
    """
    pass


def reduce_to_fixed(word, n):
    """
    >>> reduce_to_fixed('abcdefghijklm', 6)
    ... 'bafedc'
    """
    pass


def hash_it(word):
    """
    >>> hash_it('morpheus')
    ... 'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


# -------------------------------------- internal functions ---------------------------------------

def generate_letters() -> tuple:
    '''
    Creates a tuple of lowercase letters of the alphabet.

        generate_letters(), returns:
        ('a', 'b', 'c', 'd', 'e', 'f', 'g', ... 'x', 'y', 'z')
    '''
    letters = []
    for ascii_number in range(97, 123):
        letters.append(chr(ascii_number))
    return tuple(letters)

# ------------------------------------------- main code -------------------------------------------

ALPHABET= generate_letters()
ALPHABET_SIZE = len(ALPHABET)

if __name__ == '__main__':
    # name = input("Enter your name! ").lower()
    # print(f'Your key: {hash_it(name)}')

    print(shift_characters("abby", 5))
