"""Task 1
Write a function called oops that explicitly raises an IndexError
exception when called. Then write another function that calls oops inside
a try/except state­ment to catch the error. What happens if you change oops
to raise KeyError instead of IndexError?
"""

def oops():
    try:
        a = [1, 2, 3, 4]
        b = a[2]
        print(b)
    except IndexError:
        print('Ви помилились з індексом')

def oops2():
    try:
        oops()
    except (IndexError, KeyError):
        print('Ви помилились з індексом')

oops2()


"""Task 2
Write a function that takes in two numbers from the 
user via input(), call the numbers a and b, and then returns the value of squared a divided by b, construct a 
try-except block which raises an exception 
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero). """

a = input('Введіть будб ласка число а: ')
b = input('Введіть будб ласка число b: ')


def task2(a, b):
    try:
        a, b = int(a), int(b)
        result = (a ** 2) / b
        print(result)
    except ValueError:
        print('Ви ввели не цифрове значення!')
    except ZeroDivisionError:
        print('На нуль не ділиться')


task2(a, b)
print()


"""Task1
Додати у функцію з 3-го завдання уроку 8 (A simple calculator), обробку операції ділення. 
Врахувати можливий 0 у вхідних аргументах.
"""


from make_operation import make_operation1 as mo


def task3():
    while True:
        sign = input('Будь ласка, введіть символ операції яку ви бажаєте провести Enter:\n + : ''Додавання;\n'
                     '- : Віднімання;\n / : Ділення;\n * : Множення;\n Exit для виходу з програми\n Ваш вибір: ')

        a, b, c = input('Please enter number: '), input('Please enter number: '), input('Please enter number: ')
        try:
            a, b, c = int(a), int(b), int(c)
            result = mo(sign, a, b, c)
            print(result, end='\n\n')
        except (ZeroDivisionError, ValueError):
            print('Упс, щось не те ввели', end='\n\n')


task3()


"""Task2
Написати програму, яка на вхід приймає дату у форматі "1 January 22". 
Програма має вивести в консоль дати всіх понеділків в межах даного місяця.
"""


def task4():
    pass

