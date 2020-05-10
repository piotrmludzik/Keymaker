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


def pad_up_to(word: str, shift: int, letters_number: int) -> str:
    """
    Returns a string of n characters, starting with the lowercase version of word, continued by the
    shifted variants of it as described above.

        pad_up_to('abb', 5, 11), returns:
    ... 'abbfggkllpq'
    """
    letters_number = abs(letters_number)
    iterate_number = round(letters_number / len(word))

    # operates on the whole word
    returned_string = ""
    for iterate_block in range(iterate_number):
        returned_string += shift_characters(word, iterate_block * shift)

    return returned_string[:letters_number]


def abc_mirror(word: str) -> str:
    """
    Returns a string where each character (all lowercase) is "mirrored" to the other side of 'abc'.
    A character is the mirror of another when its value distance from 'z' is the same as the
    other's value distance from 'a'.

        abc_mirror('abcd')
        'zyxw'
    """
    ALPHABET_LEFT = ALPHABET[:ALPHABET_SIZE // 2]
    ALPHABET_RIGHT = ALPHABET[ALPHABET_SIZE // 2:]

    mirrored_word = ""
    for letter in word:
        if letter in ALPHABET_LEFT:
            letter_index = ALPHABET_LEFT.index(letter)
            mirrored_word += ALPHABET_RIGHT[len(ALPHABET_RIGHT) - letter_index - 1]
        else:
            letter_index = ALPHABET_RIGHT.index(letter)
            mirrored_word += ALPHABET_LEFT[len(ALPHABET_LEFT) - letter_index - 1]

    return mirrored_word


def create_matrix(word1, word2):
    """
    Returns a list of strings where the nth row is word1 shifted by the value of the nth character
    of word2.

        create_matrix('mamas', 'papas'), returns:
        ['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']
    """
    matrix = []
    for letter in word2:
        shift = ALPHABET.index(letter)
        hashed_word = shift_characters(word1, shift)
        matrix.append(hashed_word)

    return matrix


def zig_zag_concatenate(matrix):
    """
    Returns a single string containing all the characters of the "matrix" like this:

           0  1  2
        0  V  /--\\
        1  |  |  |
        1  |  |  |
        1  \\--/  V

        zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']), returns:
        'adgjkhebcfil'
    """
    matrix_length, word_length = len(matrix), len(matrix[0])
    letters_number = matrix_length * word_length

    from_left = True
    hashed_word = ""
    word_index, letter_index = 0, 0

    while len(hashed_word) != letters_number:
        # firs word
        if word_index == 0 and hashed_word != "":
            hashed_word += matrix[word_index][letter_index:letter_index+2]  # reads the next two letters
            from_left = True
            word_index += 1
            letter_index += 1

        # last word
        elif word_index == matrix_length - 1:
            hashed_word += matrix[word_index][letter_index:letter_index+2]  # reads the next two letters
            from_left = False
            word_index -= 1
            letter_index += 1

        # middle words
        else:
            hashed_word += matrix[word_index][letter_index]
            word_index += 1 if from_left else -1

    return hashed_word


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

ALPHABET = generate_letters()
ALPHABET_SIZE = len(ALPHABET)

if __name__ == '__main__':
    # name = input("Enter your name! ").lower()
    # print(f'Your key: {hash_it(name)}')

    print(zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl']))
