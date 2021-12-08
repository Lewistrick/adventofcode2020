import re

def calc_day06():
    with open("day06.txt") as day06:
        lines = day06.read()

    answergroups = lines.split("\n\n")

    part1 = 0
    part2 = 0

    groupanswers_or = set()
    for answergroup in answergroups:
        answers = answergroup.split()
        groupanswers_or.clear()
        groupanswers_and = set(list(answers[0]))
        for answer in answers:
            groupanswers_or |= set(list(answer))
            groupanswers_and &= set(list(answer))
        part1 += len(groupanswers_or)
        part2 += len(groupanswers_and)

    return part1, part2

if __name__ == "__main__":
    part1, part2 = calc_day06()
    print(part1)  # 6291
    print(part2)  # 3052

    # python -m timeit -n 100 -s "from day06 import calc_day06" "calc_day06()"

    # baseline:
    # 100 loops, best of 5: 6.47 msec per loop

    # optimization 1: use the first answer instead of the alphabet for part 2
    # 100 loops, best of 5: 6.58 msec per loop

    # opt. 2: clearing the set instead of creating a new one for every group
    # 100 loops, best of 5: 6.48 msec per loop

