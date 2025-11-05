def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

print("-" * 50)

def test():
    for i in range(1, 5):
        yield i

gen = test()
for value in gen:
    print(value)


