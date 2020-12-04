from passport import Passport

part1 = 0
part2 = 0
with open("day04.txt") as day04:
    currlines = ""
    for line in day04:
        if line.strip():
            currlines += line
        else:
            passport = Passport.from_lines(currlines)
            part1 += passport.is_valid_day04_part1()
            part2 += passport.is_valid_day04_part2()
            currlines = ""
    # it could occur that currlinse is still filled
    if currlines:
        passport = Passport.from_lines(currlines)
        part1 += passport.is_valid_day04_part1()
        part2 += passport.is_valid_day04_part2()

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")