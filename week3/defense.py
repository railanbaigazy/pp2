list_dict = [
    {
        "name1": "Railan",
        "name2": "Misha",
        "name3": "Alex",
    },
    {
        "name1": "Railan",
        "name2": "Misha",
        "name3": "Alex",
    },
    {
        "name1": "Railan",
        "name2": "Misha",
        "name3": "Alex",
    },
]

x = 0

while x < len(list_dict):
    list_dict[x]["name4"] = "Azamat"
    x = x + 1

print(list_dict)


list_nums = []
n = int(input("Input n for fibbonacci: "))

for i in range(n + 1):
    if i == 0:
        list_nums.append(0)
    elif i == 1:
        list_nums.append(1)
    else:
        list_nums.append(list_nums[i-2] + list_nums[i-1])
    
print(list_nums)