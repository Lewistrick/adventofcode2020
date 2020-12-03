from functools import reduce

forest = []

# read the forest as a bool numpy array (True indicating a tree)
with open("day03.txt") as day3:
    for line in day3:
        newline = []
        for ch in line.strip():
            newline.append(ch == "#")
        forest.append(list(newline))

height = len(forest)
width = len(forest[0])
ntrees_prod = 1
for speedx, speedy in ((1,1), (3,1), (5,1), (7,1), (1,2)):
    currx, curry = 0, 0  # whoe doesn't love curry?
    ntrees = 0
    while curry < height - 1:
        currx = (currx + speedx) % width
        curry += speedy
        ntrees += forest[curry][currx]
    ntrees_prod *= ntrees
    if speedx == 3:
        print(f"Part one: number of trees = {ntrees}")

print(f"Part two: product = {ntrees_prod}")
