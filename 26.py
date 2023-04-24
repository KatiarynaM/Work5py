'''Напишите программу, которая на вход принимает два числа A и B, и возводит число А
в целую степень B с помощью рекурсии.  *Пример:*A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''
    
def  exponentiation(a:int, b:int):
    """возводит число А в степень В"""
    exp = 1
    if b == 0:
        return exp
    return a * exponentiation(exp * a, b-1)
    
    
num_1 = int(input('Введите число:  '))
num_2 = int(input('В какую степень его возвести:  '))
print(exponentiation(num_1, num_2))
