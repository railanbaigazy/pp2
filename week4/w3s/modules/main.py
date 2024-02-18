import mymodule as mod
from mymodule import person1 as person
import platform

mod.greeting("Railan")

age = person["age"]
print(age)

print(dir(mod), "\n")
print(dir(platform))
