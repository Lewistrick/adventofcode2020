from functools import reduce
import numpy as np

lines = []

# read the forest as a bool numpy array (True indicating a tree)
with open("day03.txt") as day3:
    for line in day3:
        newline = []
        for ch in line.strip():
            newline.append(ch == "#")
        lines.append(list(newline))
forest = np.array(lines)

ntrees_prod = 1
for speedx, speedy in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    currx, curry = 0, 0  # whoe doesn't love curry?
    ntrees = 0
    while curry < forest.shape[0] - 1:
        currx = (currx + speedx) % forest.shape[1]
        curry += speedy
        ntrees += forest[curry, currx]
    ntrees_prod *= int(ntrees)
    print(f"Speed=({speedx}, {speedy}) => number of trees = {ntrees}")

print(f"Product of ntrees: {ntrees_prod}")
