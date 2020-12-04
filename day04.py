from passport import Passport

part1 = 0

with open("day04.txt") as day04:
    currlines = ""
    for line in day04:
        if line.strip():
            currlines += line
        else:
            passport = Passport.from_lines(currlines)
            part1 += passport.is_valid()
            currlines = ""
    # it could occur that currlinse is still filled
    if currlines:
        passport = Passport.from_lines(currlines)
        part1 += passport.is_valid()

print(f"Part 1: {part1}")