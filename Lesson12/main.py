"""
Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
"add called with 4, 5"""


def task1():

    def logger(func):
        def wrapper(*args):
            return f'{func.__name__} called with {args[0]}, {args[1]}'
        return wrapper

    @logger
    def add(x, y):
        return x + y

    @logger
    def square_all(*args):
        print((arg ** 2 for arg in args))

    print(add(3, 4))
    print(square_all(3, 4))


"""Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
"""


def task2():
    def stop_words(words: list):
        def changer(func):
            def wrapper(sent):
                change_word = func(sent)
                for word in words:
                    if word in change_word:
                        change_word = change_word.replace(word, '*')
                return change_word
            return wrapper
        return changer

    @stop_words(['pepsi', 'BMW', 'Drinks'])
    def create_slogan(name: str):
        return f"{name} drinks pepsi in his brand new BMW!"

    print(create_slogan('Steve'))

    #assert create_slogan("Steve") == "Steve drinks * in his brand new *!"


def main():
    #task1()
    #task2()
    pass


if __name__ == '__main__':
    main()
