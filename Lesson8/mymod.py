
def count_lines(name):
    list_lines = name.readlines()
    counter1 = len(list_lines)
    return counter1


def count_chars(name):
    symbols = name.read()
    number_of_ch = len(symbols)
    return number_of_ch


def test(name):
    print(count_lines(name))
    name.seek(0)
    print(count_chars(name))


'''name = open('some_text.txt')
test(name)'''






