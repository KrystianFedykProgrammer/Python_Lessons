'''
Task 2
Create a python program named "task2", and use the built-in function 'print' in it several times.
Try to pass "sep", "end" params and pass several parameters separated by commas.
Also, provide a comment text above each print statement, mentioned above,
with the expected output after execution of the particular print statement.
'''
#Hello world
print('Hello world', end='! \n',)

#Betroot Academy
print('Betroot Academy', end=' is the best IT Academy! \n')

#1 82 92 90
print( 1,82,92,90, sep=',', end='.')
print('\n'*3)


'''
Task 3
Write a program, which has two print statements to print the following text 
(capital letters "O" and "H", made from "#" symbols):
#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #

Pay attention that usage of spaces is forbidden, as well as creating the whole result 
text string using """ """, use '\n' and '\t' symbols instead.
'''

symbol = '#'
display_size = 10
line = symbol*display_size + '\n'
another_line = symbol + ' '*len(symbol)*(display_size-2) + symbol + '\n'
line_symbol = symbol + '\n'

print('Letter O' + '\n')
print(line + another_line*3 + line)

print('Letter H' + '\n')
print(another_line*2 + line + another_line*2)

print('Letter E' + '\n')
print(line + line_symbol*2 + line + line_symbol*2 + line)

print('Letter P' + '\n')
print(line + another_line*2 + line + line_symbol*3)

print('Letter F' + '\n')
print(line + line_symbol*2 + line + line_symbol*3)



