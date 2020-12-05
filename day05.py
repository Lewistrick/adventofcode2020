import timeit

def calc_day05():
    # read boarding passes
    with open("day05.txt") as day05:
        bpasses = day05.read()

    ids = set()
    part1 = 0

    let2bin = {"F": "0", "B": "1", "L": "0", "R": "1"}
    for bp in bpasses.split():
        binbp = "".join(let2bin[let] for let in bp)
        seatid = int(binbp, 2)
        part1 = max(part1, seatid)
        ids.add(seatid)

    ids = sorted(ids)
    for id1, id2 in zip(ids[:-1], ids[1:]):
        if id2 - id1 > 1:
            part2 = id1 + 1
            break

    return part1, part2


if __name__ == "__main__":
    part1, part2 = calc_day05()

    print(part1)
    print(part2)

    # timing command:
    # python -m timeit -s "from day05 import calc_day05" "calc_day05()"

    # baseline
    # 100 loops, best of 5: 3.82 msec per loop

    # after removing the split between row and seat
    #   (because seat id is represented in binary)
    # 100 loops, best of 5: 2.05 msec per loop
