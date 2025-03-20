# Задание 2

def feb():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


gen = feb()

for num in range(4):
    next(gen)
print(next(gen))
for num in range(199):
    next(gen)
print(next(gen))
for num in range(999):
    next(gen)
print(next(gen))
for num in range(99999):
    next(gen)
print(next(gen))
