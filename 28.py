'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
return sum(a, b) + 1 - такое использовать нельзя'''

    
def sum (a:int, b:int):
    """возводит сумму а и в"""
    if b == 0:
        return a
    return  sum(a+1, b-1)
    
    
num_1 = int(input('Введите первое число:  '))
num_2 = int(input('Введите второе число:  '))
print(sum(num_1, num_2))
