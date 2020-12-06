from string import ascii_lowercase

LETTERS = set(list(ascii_lowercase))

def calc_day06():
    with open("day06.txt") as day06:
        lines = day06.read()

    answergroups = lines.split("\n\n")

    part1 = 0
    part2 = 0
    for answergroup in answergroups:
        groupanswers_or = set()
        groupanswers_and = set(LETTERS)
        for answer in answergroup.split():
            groupanswers_or |= set(list(answer))
            groupanswers_and &= set(list(answer))
        part1 += len(groupanswers_or)
        part2 += len(groupanswers_and)
        # breakpoint()

    return part1, part2

if __name__ == "__main__":
    part1, part2 = calc_day06()
    print(part1)
    print(part2)
