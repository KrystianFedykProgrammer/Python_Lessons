'''Task 1
The greatest number
Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
'''


import random


def task1():
    x = []
    i = 0

    while i < 10:
        x.append(random.randint(1, 100))
        i += 1
    print(f'The maximum element of the list {x} is - {max(x)}')
    print()


'''
Task 2
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list 
containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
'''


def task2():
    first_list = []
    second_list = []
    i = 0

    while i < 10:
        first_list.append(random.randint(1, 10))
        second_list.append(random.randint(1, 10))
        i += 1

    print(first_list)
    print(second_list)
    print(list(set(first_list + second_list)))
    print()


'''
Task 3
Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers from 
the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
'''


def task3():
    big_list = [i for i in range(0, 100, 7) if i % 5 != 0]
    '''i = 1

    while i < 101:
        if i % 7 == 0 and i % 5 != 0:
            big_list.append(i)
        i += 1'''

    print(big_list)




def main():

    #task1()
    #task2()
    task3()


if __name__ == '__main__':
    main()
