"""
Task 1
Make a program that has some sentence (a string)
on input and returns a dict containing all unique words as keys and the number of occurrences as values.
"""


def task1(words2):
    counts = dict()
    words1 = words2.split()

    for word in words1:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


"""
Task 2
Compute the total price of the stock where
the total price is the sum of the price of an item multiplied by the quantity of this exact item.
"""


def task2():
    stock = {'banana': 6,
             'apple': 0,
             'orange': 32,
             'pear': 15
             }

    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    final_sum = {key: 0 for key in prices}
    print(final_sum)

    for i in prices:
        final_sum[i] = stock[i] * prices[i]
    return final_sum


'''
Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where `i` 
goes from 1 to 10 and `j` is corresponding to `i` squared.
'''


def task3():
    num = {i: i ** 2 for i in range(1, 11)}
    print(num)


'''
Task 4
1.Створити лист із днями тижня.
2.В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
3.Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
'''


def task4():
    weakly_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    nums = [i for i in range(1, 8)]
    week = {nums: weakly_days for (nums, weakly_days) in zip(nums, weakly_days)}

    weakly_days = {}
    for key, values in week.items():
        weakly_days[values] = key
    print(f'{week}\n\n{weakly_days}')

"""Task5"""


def task5():
    import random

    MAX_WIDTH = 8
    MAX_HIGHT = 8
    MINES = 10

    mines_list = []
    for i in range(0, MINES):
        mines_list.append((random.randint(0, MAX_WIDTH - 1),
                           random.randint(0, MAX_HIGHT - 1)))

    print(mines_list)

    user_session = []

    while True:
        print(' ', [str(i) for i in range(MAX_WIDTH)], sep=' ')
        for i in range(MAX_WIDTH):
            line = []
            for j in range(MAX_WIDTH):
                if (j, i) not in user_session:
                    line.append('*')
                else:
                    line.append(' ')
            print(i, line)

        input_value = input('Введіть координати x y: ')
        x, y = input_value.split()

        if not x.isdigit() or not y.isdigit():
            continue

        x, y = int(x), int(y)
        if (x, y) in mines_list:
            print("You lose")
            break

        user_session.append((x, y))


def main():
    '''sentences = input("Enter some text: ")
    print(task1(sentences), end='\n\n')'''
    print(f'Total sum: {task2()}\n')
    #task3()
    print()
    #task4()
    #task5()

if __name__ == '__main__':
    main()
