from array import array

def let2bin(let):
    return let == "B" or let == "R"

def calc_day05():
    # read boarding passes
    freeseats = array("B", [1] * (2 ** 10))  # maximum no. of seats = 2**10=1024
    minseat = 2 ** 10
    maxseat = 0

    with open("day05.txt") as day05:
        for bp in day05:
            binbp = (let2bin(let) for let in bp.strip())
            seatid = sum(val * (2 ** (9 - idx)) for idx, val in enumerate(binbp))

            maxseat = max(maxseat, seatid)
            minseat = min(minseat, seatid)
            freeseats[seatid] = 0  # mark as occupied

    freeseat = freeseats[minseat:].index(1) + minseat

    return maxseat, freeseat


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

    # after
    # - replacing the set of occupied seat IDs by a binary array of free seats
    # - making let2bin a function instead of a dictionary:
    # 100 loops, best of 5: 6.92 msec per loop
    # (why is this so much worse? at least it's better in memory management)
