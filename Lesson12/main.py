"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
"add called with 4, 5"""


def task1():

    def logger(func):
        print(func(4, 5))

    @logger
    def add(x, y):
        return x + y

    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]

"""Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def task2():
    def stop_words(words: list):
        def wrapper(func):
            nonlocal words
            a = func()
            a = a.split()
            if words in a:
                words = '*'
        return wrapper



    @stop_words(['pepsi', 'BMW'])
    def create_slogan(name: str):
        return f"{name} drinks pepsi in his brand new BMW!"

    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

def main():
    #task1()
    task2()

if __name__ == '__main__':
    main()
