def repeat_me(fun):
    def wrapper(text, count=2):
        for i in range(count):
            fun(text)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
