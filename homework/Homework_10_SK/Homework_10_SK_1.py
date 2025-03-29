def finish_me(func):
    def wrapper():
        func()
        print('finished')

    return wrapper


@finish_me
def example1():
    print('print me')


example1()
