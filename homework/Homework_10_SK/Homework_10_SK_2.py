def repeat_me(func):
    def wrapper(*args):
        func(*args)

    return wrapper


@repeat_me
def example(text, count=2):
    for i in range(count):
        print(text)


example('print me')
