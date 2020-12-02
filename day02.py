import re

linere = re.compile("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$")

part1 = 0
part2 = 0
with open("day02.txt") as day02:
    for line_plus_whitespace in day02:
        line = line_plus_whitespace.strip()
        nmin, nmax, let, password = linere.match(line).groups()
        nmin, nmax = int(nmin), int(nmax)

        if password.count(let) in range(nmin, nmax+1):
            part1 += 1

        if (password[nmin-1] == let) ^ (password[nmax-1] == let):
            part2 += 1

print(f"Number of valid passwords, part 1: {part1}")
print(f"Number of valid passwords, part 2: {part2}")