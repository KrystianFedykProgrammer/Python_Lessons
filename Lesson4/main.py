'''
Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 and
lets the user guess what number was generated. The result should be sent back to the user via a print statement.
'''

import random


def task1():
    print('Ведіть будь ласка межі випадкових чисел: ')
    x = int(input('x = '))
    y = int(input('y = '))

    counter = 0
    i = 0

    while i < 5:
        z = random.randint(x, y)
        # print(z, end='')
        j = 0
        print()
        while j < 3:
            a = int(input('Введіть будь ласка число: '))
            if a == z:
                print("Ви вгадали число!")
                counter += 1
                break
            else:
                print('Спробуйте ще раз!')
                if j == 2:
                    break
            j += 1

        i += 1

    print()
    if counter >= 4:
        print("Ви надзвичайно щасливі")
    elif 2 < counter < 4:
        print('У вас хороша інтуїція')
    else:
        print('Пощастить наступного разу!')
    print()


'''Task 2
The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”  '''


def task2():
    my_name = input('Як вас звуть: ')
    age = int(input('Скільки вам років? '))

    print(f'Hello {my_name}, on your next birthday you’ll be {age + 1} years')
    print()


'''
Task 3
Words combination
Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
'''


def task3():
    word = input('Введіть будь яке слово: ')
    i = 0
    while i < 5:
        print(''.join(random.sample(word, len(word))))
        i += 1


def main():

    #task1()
    #task2()
    task3()


if __name__ == '__main__':
    main()
