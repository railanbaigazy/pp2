#2. Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
input = input()

def fahrenheitToCelcius(fahrenheit):
    return (5 / 9) * (int(fahrenheit) - 32)

print(fahrenheitToCelcius(input))