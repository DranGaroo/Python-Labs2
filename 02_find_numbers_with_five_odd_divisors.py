# Найти числа с ровно 5 нечётными делителями.
# Перебрать все числа в диапазоне [40000; 50000].
# Для каждого числа найти все нечётные делители.
# Проверить, что количество нечётных делителей равно 5.
# Вывести подходящие числа в порядке возрастания.

def find_numbers_with_five_odd_divisors():
    result = []
    for num in range(40000, 50000+1):
        odd_divisors = 0
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i % 2 == 1:
                    odd_divisors += 1
                counterpart = num // i
                if counterpart != i and counterpart % 2 == 1:
                    odd_divisors += 1
        if odd_divisors == 5:
            result.append(num)
    return result

print(find_numbers_with_five_odd_divisors())

