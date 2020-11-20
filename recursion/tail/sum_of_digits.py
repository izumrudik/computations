# Дано натуральное число N. Вычислите сумму его цифр.
# При решении этой задачи в функциях sum и sum_tail нельзя использовать цикл, а также строки, списки, массивы
# Оформите в виде обычной и хвостовой рекурсии
# Вариант с хвостовой рекурсией преобразуйте в цикл while

# вариант с циклом while
def sum(N):
    x = 0

    while N > 0:
        x = x + N % 10
        N = N // 10
    
    return x


# хвостовая рекурсия
def sum_tail(N, s):
    if N < 10:
        return N + s
   
    return sum_tail(N // 10, s + N % 10)


# прямая рекурсия
def sum_of_digits(N):
    if N < 10:
        return N
   
    return N % 10 + sum_of_digits(N // 10)


print (sum(987654321012345678991))
print (sum_of_digits(987654321012345678991))
print (sum_tail(987654321012345678991, 0))

