'''
Task 1
String manipulation
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: 'x'
Expected Result: Empty String
Tips:
Use built-in function len() on an input string
Use positive indexing to get the first characters of a string and negative indexing to get the last characters
'''

word = 'helloworld'

if len(word) >= 2:
    print(f'{word[0:2]}{word[-2:]}\n')
else:
    print()

'''
Task 2
The valid phone number program.
Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long. 
Print a suitable message depending on the outcome of the string evaluation.
'''


cell_number = input('Введіть будь ласка ваш номер: ')
OPERATOR_CODE = [55, 67, 99, 97, 66]
count = False
i = 0

while i < len(OPERATOR_CODE):
    if len(cell_number) == 10 and cell_number.isdigit() and int(cell_number[1:3]) == OPERATOR_CODE[i]:
        count = True
        break
    i += 1

if count:
    print('Your number format is correct')
else:
    print('Your number format is incorrect')

print()

'''
Task 3
The math quiz program.
Write a program that asks the answer for a mathematical expression, checks whether the user 
is right or wrong, and then responds with a message accordingly.
'''

'''
Перша версія

print('Скільки буде 15 + 15: ')
a = int(input())

if a == 30:
    print('Ваша відповідь правильна!')
elif 25 < a < 30:
    print('Ваша відповідь не правильна, але ви були близько.')
else:
    print('Нажаль ви вказали не правильну відповідь!')'''

print('Привіт, давай зіграємо в гру. Я задаю тобі питання, а ти відповідаєш на них!')
#print('Щоб пропустити вікторону введіть 00!')
QUESTION = ['Скільки буде 15 + 15: ', 'Скільки буде 100 + 100: ', 'Скільки буде 150 + 150: ']
ANSWERS = [30, 200, 300]
i = 0

'''Ось тут додав список відповідей, і вказав його в циклі, для того щоб виключити імовірність того, 
що користувач введе одинакові значення на всі запитання'''

while i < len(QUESTION):
    print(QUESTION[i])
    a = int(input())

    if a == ANSWERS[i]:
        print('Ваша відповідь правильна!', end='\n\n')
    else:
        '''if a == 00:
            break'''
        print('Нажаль ви вказали не правильну відповідь!', end='\n\n')
    i += 1

print()

'''
Task 4
The name check.
Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
The program should check if your input is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
'''

my_name = 'nazar'
input_name = input("Введіть ваше ім'я: ")

print(input_name.lower() == my_name)

print()

'''
Вхідні дані для всіх завдань можна отримувати двома способами: функція input(), або аргументи програми sys.argv
Task1
Write a Python program to construct the following pattern, using a while loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Плюс за можливість динамічно змінити максимальну кількість зірочок в одному рядку (в прикладі 5) '''

SYMBOL = '*'
row = 5
i = 1

while i < row:
    print("* " * i)
    i += 1

i = row

while i >= 1:
    print("* " * i)
    i -= 1

print()

'''
Task2
Write a python program, which sums all digits in a python string.
Examples, input - ‘1234’, output - 10
'''


num = input('Введіть будь ласка будь-яке число: ')
final_number = 0
i = 0

while i < len(num):
    if num[i].isalpha():
        print('Ви ввели не числове значення!') #Додав перевірку для нечислового значення
        final_number = 0
        break
    else:
        final_number += int(num[i])
    i += 1
if final_number > 0:
    print(f'Сума всіх цифер вашого числа: {final_number}')

print()

'''
Task3
Write a Python program that accepts a string and calculate the number of digits, 
letters and other characters in the input string
'''

counter_digit = 0
counter_letter = 0
counter_sign = 0
sentence = input('Будь ласка введіть будь що забажаєте: ')
i = 0

while i < len(sentence):
    if sentence[i].isdigit():
        counter_digit += 1
    elif sentence[i].isalpha():
        counter_letter += 1
    elif sentence[i].isspace():
        i += 1
        continue
    else:
        counter_sign += 1
    i += 1

print(f'Кількість введених цифер:{counter_digit}')
print(f'Кількість введених літер:{counter_letter}')
print(f'Кількість введених знаків:{counter_sign}')

