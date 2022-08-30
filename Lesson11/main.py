"""
Task 1
Write a Python program to detect the number of local variables declared in a function.
"""


def task1():
    a = 1
    b = 2
    struct = "fffff"

print(task1.__code__.co_nlocals)
print()

"""
Task 2
Write a Python program to access a function inside a 
function (Tips: use function, which returns another function)
"""


def task2():
    def make_add(x):
        print(x)

        def add_y(y):
            print(y)
            return x + y

        return add_y

    a = make_add(5)
    print(a(15))


task2()
print()

"""
Task 3
Write a function called `choose_func` which takes a list of nums and 2 
callback functions. If all nums inside the list are positive, execute the first function on that list 
and return the result of it. Otherwise, return the result of the second one"""


def task3():

    def choose_func(nums: list, func1, func2):
        a = list(filter(lambda num: num < 0, nums))
        if len(a) == 0:
            return func1(nums)
        else:
            return func2(nums)

    # Assertions
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    def square_nums(nums):
        return [num ** 2 for num in nums]

    def remove_negatives(nums):
        return [num for num in nums if num > 0]


    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


task3()
