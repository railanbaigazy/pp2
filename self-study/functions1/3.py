#3. Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

numheads = 35
numlegs = 94

def solve(numheads, numlegs):
    #chickens + rabbits = numheads
    #2*chickens + 4*rabbits = numlegs
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
        
print(solve(numheads, numlegs))
