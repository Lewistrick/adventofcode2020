with open("day01.txt") as day01:
    nums = [int(num) for num in day01.readlines()]


# part 1
target = 2020
for idx1, num1 in enumerate(nums[:-1]):
    for num2 in nums[idx1:]:
        add = num1 + num2
        if add == target:
            print(num1 * num2)

# part 2
from itertools import combinations
from functools import reduce
for comb in combinations(nums, 3):
    if sum(comb) == 2020:
        product = reduce(int.__mul__, comb)
        print(comb, product)
        break