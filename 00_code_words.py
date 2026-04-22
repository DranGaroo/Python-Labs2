# Ольга составляет таблицу кодовых слов/
# 4-буквенные слова, в которых есть только буквы A, B, C, D, X, Y, Z.
# При этом первая буква кодового слова  — это буква X, Y или Z,
# Далее в кодовом слове буквы X, Y и Z не встречаются.

from itertools import product

def count_code_words():
    first_letters = ['X', 'Y', 'Z']
    other_letters = ['A', 'B', 'C', 'D']
    words = 0
    for first in first_letters:
        for other in product(other_letters, repeat=3):
            words += 1
    return words

print('Ольга может использовать', count_code_words(), 'различных кодовых слов.')
