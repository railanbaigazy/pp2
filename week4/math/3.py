import math

def polygon_area(n, l):
    apothem = l / (2 * math.tanh(180 / n))
    return n * l * apothem / 2

n = int(input("Number of sides: "))
l = int(input("Length of one side: "))

print(polygon_area(n, l))
