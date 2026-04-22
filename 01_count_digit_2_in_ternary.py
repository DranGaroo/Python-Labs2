# Вычислить значение выражения: 9^8 + 3^5 – 9.
# Перевести результат в троичную систему.
# Посчитать количество цифр «2» в троичной записи.

def count_digit_2_in_ternary():
    expression = (9**8) + (3**5) - 9
    ternary = ''
    while expression > 0:
        ternary = str(expression % 3) + ternary
        expression //= 3
    return ternary.count('2')

print('В троичной записи выражении 9^8+3^5-9 цифра "2" встречается', count_digit_2_in_ternary(), 'раза.')
