# The Keymaker

## Story

Thousands of human refugees are living outside the Matrix, hiding from
Sentinels and the Agents of the machines. Keeping their systems safe and
intact from the powerful enemy is an enormous task. They cannot trust
any known algorithm for storing sensitive information like names, access
codes, and passwords because the machines with their superior computing
capacity would be able to break them easily.

The access codes to the mainframe computers of the city of Zion are
stored as hashed values, with a secretly kept, custom hashing algorithm
created by a legendary figure known as the _Keymaker_. Even the user names
are stored in a hashed form. Your job is to implement this string
hashing algorithm described in the requirements.

The output of the hash function is always a 6 character long string.
Along the transformations you have to use these numeric values for the
base lowercase English characters: `0` for `a`, `1` for `b`, `2` for
`c`, and so on until `25` for `z`.

**!!! WARNING !!!**
Never ever use custom hash algorithms in any real situation!
What counts as real, you may ask. Well, never ever after this project
**!!! DON'T TRY THIS AT HOME !!!**

## What are you going to learn?

You will practice string operations as well you will improve your
algorithmic skills.

## Tasks


1. Implement `shift_characters(word, shift)` which returns the characters of the word, all shifted by `shift`. _Shifting a character_ means adding a number to the original character value. If the resulting character would step out from the `a-z` region, continue the counting from the other end. (e.g. shifting `'a'` by `5` yields `'f'`, shifting `'y'` by `5` yields `'d'`, shifting `'a'` by `-3` yields `'x'`). The function returns these shifted characters concatenated. Example: `shift_characters('abby', 5)` should return `'fggd'`.

    - The returned string's length is the same as `word`'s length.
    - The returned string contains the shifted characters of `word`.
    - Shifting works for any integer value. Shifting by `n + 26` yields the same result as shifting by `n`.

2. Implement function `pad_up_to(word, shift, n)` which returns a string of `n` characters, starting with the lowercase version of `word`, continued by the shifted variants of it as described above. A variant is the shifted version of the one before. Example: `pad_up_to('abb', 5, 11)` should return `'abbfggkllpq'` because the first couple of `5`-shifted variants of `'abb'` are `'fgg'`, `'kll'`, and `'pqq'`, and the first `11` characters of this series are returned.

    - The returned string's length is `n`.
    - The returned string starts with the original `word` (or the first `n` characters of it when it is longer than `n`).
    - The returned string continues with the shifted variant of `word` (shifted by `shift`), and then further shifts until it reaches the length `n`.

3. Implement function `abc_mirror(word)` which returns a string where each character (all lowercase) is "mirrored" to the other side of 'abc'. A character is the mirror of another when its value distance from 'z' is the same as the other's value distance from 'a'. Examples for mirrored pairs: `'a' <-> 'z'`, `'b' <-> 'y'`, `'l' <->'o'`, `'m' <->'n'`, so for example `abc_mirror('abcd')` should return `'zyxw'`, and`abc_mirror('morpheus')` should return `'nliksvfh'`.

    - The returned string's length is the same as the input's length.
    - The returned string is character-by-character the mirrored version of the input.

4. Implement function `create_matrix(word1, word2)` which returns a list of strings where the nth row is `word1` shifted by the value of the nth character of `word2`. Example: `create_matrix('mamas', 'papas')` returns `['bpbph', 'mamas', 'bpbph', 'mamas', 'esesk']` (`'bpbph'` is `'mamas`' shifted by 15, the character value of `'p'`).

    - The return value is a list of strings. The length of the strings is the length of `word1`, the length of the list is the length of `word2`
    - Each row of the list is the shifted variant of `word1`, shifted by the corresponding character value of `word2`

5. Implement function `zig_zag_concatenate(list_of_words)` which returns a single string
containing all the characters of the "matrix" like this:
```
   0  1  2
0  V  /--\
1  |  |  |
1  |  |  |
1  \--/  V
```
So start with the first "column" (i.e. the first letters of the words) from the top,
then concatenate the letters of the second column from bottom to top, then turn again
and concatenate the third column starting from the top, and so on. For example,
for an input of `['abc', 'def', 'ghi', 'jkl']` it should return `'adgjkhebcfil'`.
The incoming list of strings are always of the same length.

    - The returned string contains all the characters of the input once.
    - The characters are concatenated following the zig-zag direction described above

6. Implement function `rotate_right(word, n)` which returns a string of the same length as `word`, only the characters are rotated by `n` positions rightwards. The character "falling out" on the right side come back from the left side. Example: `rotate_right('abcdefgh', 1)` returns `'habcdefg'`, `rotate_right('abcdefgh', 3)` returns `'fghabcde'`, `rotate_right('abcdefgh', 8)` returns `'abcdefgh'`. As you see, rotating by the length of the string yields the input string unchanged. The value of `n` can be any integer.

    - The returned string is of the same length as `word`
    - The characters of `word` are rotated by `n` positions to the right, "falling out" characters appear on the left.
    - The return is identical for `n`-values differing by the length of the word. Example: `rotate_right('abcdefgh', 3)` yields the same result for other rotation values like `n=11`, `n=-5`, and `n=-13` (as the length of the string is `8`).

7. Implement function `get_square_index_chars(word)` which returns all characters of `word` laying at square number indices. Example: `get_square_index_chars('abcdefghijklm')` should return `'abej'` because these letters are picked from positions `[0, 1, 4, 9]`, and the next square number position, `16` is not in the `13`-long input.

    - The returned string's length is the number of square numbers less than the length of `word` (including zero)
    - The characters of the returned string are taken from square number positions of the input.

8. Implement function `remove_odd_blocks(word, block_length)` which breaks the input into blocks of the given length, removes every second block (i.e. keeping blocks number `0, 2, 4`, etc.), and returns the remaining blocks concatenated. Example: `remove_odd_blocks('abcdefghijklm', 3)` should return `'abcghim'` because removing every second from the blocks of length `3` (`['abc', 'def', 'ghi', 'jkl', 'm']`) yields to `['abc', 'ghi', 'm']`.

    - The returned string skips characters at positions `[3, 4, 5]`, `[9, 10, 11]`, etc. from the input as described above.

9. Implement function `reduce_to_fixed(word, n)` which cuts the first `n` characters of the input, and performs a left rotation of `n//3` and returns the result read backwards. Example: `reduce_to_fixed('abcdefghijklm', 6)` should return `'bafedc'` because left rotating `'abcdef'` (the first 6 characters) by 2 gives `'cdefab'` which should also be reversed.

    - The returned string is `n` characters long.
    - The returned string is the rotated and flipped variant of the input's first `n` characters.

10. Check your functions by using the prepared `hash_it` function! `hash_it('morpheus')` should return 'trowdo', `hash_it('trinity')` should return 'jotysy'. Check also for the hashed name of 'neo' and share the surprise of the rebels about the result!

    - The results are the same as the given examples, and Neo's true fate is revealed


## General requirements


None

## Hints

None.

## Starting repository

Follow [this link](https://journey.code.cool/v2/project/solo/keymaker-python) to create your project repository.

## Background materials

- :exclamation:
  [Strings](https://learn.code.cool/codecool-graph/#/../pages/python/strings)

## Acceptance review

You will need this only at review time, **after** completing the project.
[Use this form](https://forms.gle/YtDJ1Qdv1ETxAMUH6) to record the review you provide for your peer.

For now, you can check your (and everyone else's) results in the [summary spreadsheet](https://docs.google.com/spreadsheets/d/1otJkV-zl-Sfg3BWX1ZbFJ_e-GpLf5Jr6oSysZTfpfD4/edit#gid=31463349).