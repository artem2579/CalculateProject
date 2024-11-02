def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def devide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "На ноль делить нельзя"
