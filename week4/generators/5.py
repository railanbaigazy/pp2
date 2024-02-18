def down_to_zero(n):
    for i in range(n, -1, -1):
        yield i

for i in down_to_zero(8):
    print(i)