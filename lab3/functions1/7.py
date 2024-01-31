#7. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    prev = nums[0]
    for i in range(1, len(nums)):
        if prev == 3 and nums[i] == 3:
            return True
        prev = nums[i]
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))