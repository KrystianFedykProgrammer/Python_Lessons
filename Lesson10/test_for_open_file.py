def create_file(some_text):
    with open('my_file.txt', 'w') as file_object:
        file_object.write(some_text)


def depict():
    with open('my_file.txt') as file_object:
        some_text = file_object.read()
        return some_text
