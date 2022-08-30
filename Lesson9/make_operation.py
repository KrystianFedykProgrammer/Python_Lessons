def make_operation1(sign, a, *args):
    if sign == '+':
        return a + sum(args)
    if sign == '*':
        for num in args:
            a *= num
        return a
    if sign == '-':
        for num in args:
            a -= num
        return a
    if sign == '/':
        for num in args:
            a /= num
        return a

