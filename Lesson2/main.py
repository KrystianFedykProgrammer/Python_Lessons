'''
Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     "Good day <name>! <day> is a perfect day to learn some python."
Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.
'''

my_name = 'Nazar'
weekday = 'Monday'
print(f'Good day {my_name}! {weekday} is a perfect day to learn some python.'+'\n')

'''
Task 2

Manipulate strings.

Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.
'''


surname = 'Fedyk'
print(surname + ' ' + my_name + '\n')
print(f"Hello world! My name is {surname} {my_name}! And now I'm learning Python programming" + '\n')

'''
Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

Addition
Subtraction
Division
Multiplication
Exponent (Power)
Modulus
Floor division
'''

a = 4
b = 2

print(f'The result of addition is a number: {a+b}')
print(f'The result of subtraction is a number: {a-b}')
print(f'The result of division is a number: {a/b}')
print(f'The result of multiplication is a number: {a*b}')
print(f'The result of exponent (Power) is a number: {a**b}')
print(f'The result of modulus is a number: {a%b}')
print(f'The result of subtraction is a number: {a//b}' + '\n')

'''
Task 4 

Під зірочкой
на форматування. Зробіть форматування так щоб отримати ось таке
"000012 Василий 110110 32.10"
заповніть ___ , майте на увазі 110110 - це бінарний формат.
print("____________________".format(12, "Василий", 54, 32.1))
'''



print("{0:0>6} {1} {2:b} {3:5.2f}".format(12, "Василий", 54, 32.1)+'\n')



'''
Task 5
Спробуйте "зібрати" зі слова "Корован" слово "ворона". Використайте слайсінг та вашу фантазію.
s1 = "Корован"
print(s1[4]+s1[1]+s1[2] +... <-  можлиіий але не самий цікавий варіант.
'''

main_word = "Корован"
word = main_word[-3:-7:-1] + main_word[-1:-3:-1]
word = word.capitalize()
print(word)
