"""
Task 1
A simple function.
Create a simple function called favorite_movie, which takes a string containing
the name of your favorite movie. The function should then print “My favorite movie is named {name}”.
"""


def favorite_movie(movie):
    print(f'My favorite movie is: {movie}', end='\n\n')


'''
Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name and 
capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ 
as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.
'''


def make_country(name, capitals):
    countries = dict(zip(name, capitals))
    return countries


'''Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first 
parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) 
as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42 '''


def make_operation(sign, *args):
    while True:
        if sign == 'exit' or sign == ' ':
            break
        elif sign == '+':
            return sum(args)
        elif sign == '*':
            n = 1
            for num in args:
                n *= int(num)
            return n
        elif sign == '-':
            x = args[0]
            for num in args[1:]:
                x -= num
            return x
        else:
            x = args[0]
            for num in args[1:]:
                x = x // num
            return x

'''Task4
Write a function that takes on an input random ints (between 1 and 10) and returns 
the longest consecutive run and the length of that run of elements of the list.
Ex.  def task1(1,2,3,4,4,4,4,4,4,5,6,7,4,2,2,5) -> 6, 4
 def task1(1) -> 1, 1
 def task1() -> 0, None
Then create another function which takes on input result of function from the 
previous step and prints Informative message about the longest consecutive run, something like - “Longest run is 6 of integers - 4”
'''


def task4():
    pass


'''Task 5
Create a function that takes on an input random ints (between 1 and 10) and 
returns the list, without duplicates. Try to create two versions of this function - 
first with usage set and list constructors and second only using for-in loops.
def task2(1,2,34,2,3,2,4) -> 1, 2, 34, 3, 4'''


def task5():
    pass


def main():
    """Task1"""
    movie = input("Please Enter your favorite movie: ")
    favorite_movie(movie)

    '''Task2'''

    name = ('France', 'Germany', 'Czech Republic', 'Poland')
    capitals = ('Paris', 'Berlin', 'Prague', 'Warzawa')
    print(make_country(name, capitals), end='\n\n')

    '''Task3'''

    sign = input('Будь ласка, введіть символ операції яку ви бажаєте провести Enter:\n + : ''Додавання;\n'
                 '- : Віднімання;\n / : Ділення;\n * : Множення;\n Exit для виходу з програми\n Ваш вибір: ')

    a, b, c = int(input('Please enter number: ')), int(input('Please enter number: ')), int(input('Please enter number: '))

    print(f'Result: {make_operation(sign, a, b, c)}')


if __name__ == '__main__':
    main()
