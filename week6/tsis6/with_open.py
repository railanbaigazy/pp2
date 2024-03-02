def count_lines(filename):
    with open(filename, 'r') as file:
        lines = 0
        for line in file:
            lines += 1
    
    return lines

filename = "test.txt"

print("Lines:", count_lines(filename))
