from collections import deque

fn = "in09.txt"
with open(fn) as lines:
    numbers = [int(x.strip()) for x in lines]

windowsize = 25

# first fill the preamble
preamble = deque(numbers[:windowsize], maxlen=windowsize)
for idx in range(windowsize, len(numbers)):
    currnum = numbers[idx]
    for num in preamble:
        if (currnum - num) in preamble:
            preamble.append(currnum)
            break # breaks the inner for loop
    else: # only runs if the previous for loop didn't break
        part1 = currnum
        break # breaks the outer for loop

print(part1)

## part 2 below

part2 = None
for sidx, smallest in enumerate(numbers):
    for lidx, largest in enumerate(numbers[sidx+1:]):
        subnumbers = numbers[sidx:sidx+lidx+1]
        contsum = sum(numbers[sidx:lidx+sidx+1])
        if contsum > part1:
            break
        elif contsum == part1:
            part2 = min(subnumbers) + max(subnumbers)
            break
    if part2:
        break

print(part2)
