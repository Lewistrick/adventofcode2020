# read boarding passes
with open("day05.txt") as day05:
    bpasses = day05.read()

ids = set()
part1 = 0
let2bin = {"F": "0", "B": "1", "L": "0", "R": "1"}
for bp in bpasses.split():
    # read row as 0s and 1s
    binrow = "".join(let2bin[let] for let in bp[:7])
    # convert binary to decimal
    rowno = int(binrow, 2)

    binseat = "".join(let2bin[let] for let in bp[7:])
    seatno = int(binseat, 2)

    # Calculate seatid. This could also be done
    seatid = rowno * 8 + seatno

    part1 = max(part1, seatid)

    ids.add(seatid)

print(part1)

ids = sorted(ids)
for id1, id2 in zip(ids[:-1], ids[1:]):
    if id2 - id1 > 1:
        part2 = id1 + 1
        break

print(part2)