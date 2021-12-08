from functools import lru_cache

with open("in10_ex.txt") as lines:
    numbers = list(map(int, lines.read().split()))

numbers = [0] + sorted(numbers) + [max(numbers) + 3]
print(numbers)
diffs = [n2-n1 for n1, n2 in zip(numbers, numbers[1:])]
part1 = sum(1 for n in diffs if n == 1) * sum(1 for n in diffs if n == 3)
print(part1)

@lru_cache
def n_solutions_tup(numtup):
    if len(numtup) <= 2:
        return 1
    next_ids = (id + 1 for id, val in enumerate(numtup[1:4])
                if val - numtup[0] <= 3)
    return sum(n_solutions_tup(numtup[next_id:]) for next_id in next_ids)

part2 = n_solutions_tup(tuple(numbers))
print(part2)