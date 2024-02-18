def trapezoid_area(h, b1, b2):
    return (b1 + b2) * h / 2

height = int(input("Height: "))
base_1 = int(input("Base, first value: "))
base_2 = int(input("Base, second value: "))

print(trapezoid_area(height, base_1, base_2))