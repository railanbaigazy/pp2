def even_generator(n):
    for i in range(2, n):
        if i % 2 == 0:
            yield i

n = int(input("n: "))

for i in even_generator(n):
    print(i)