import pdb
import re
from loguru import logger

class Bag:
    def __init__(self, color):
        self.color = color
        self.contains = []
        self.contained_by = set()

    def add_contained(self, color, number):
        self.contains.append((color, number))

    def add_containedby(self, other):
        self.contained_by.add(other)

    def count_inside(self, bags):
        if not self.contains:
            return 0
        n_inside = 0
        # pdb.set_trace()
        for (color, number) in self.contains:
            n_inside += number * (1 + bags[color].count_inside(bags))
        return n_inside


contained_re = re.compile("^([1-9][0-9]*) ([a-z]+ [a-z]+) bag[s]?$")
with open("day07.txt") as day07:
    bags = {}
    for line in day07:
        container, contained = line.strip().split(" bags contain ")
        bag = Bag(container)
        if contained == "no other bags.":
            bags[bag.color] = bag
            continue

        contained = contained.strip(".").split(", ")
        for cont_sentence in contained:
            conmatch = contained_re.match(cont_sentence)
            if not conmatch:
                logger.warning(f"No matched color: {cont_sentence}")
                continue

            number, color = int(conmatch.group(1)), conmatch.group(2)
            bag.add_contained(color, number)

        bags[bag.color] = bag

# Add contained_by info
for color, bag in bags.items():
    for cont, _ in bag.contains:
        bags[cont].add_containedby(bag)

cbags = [bags["shiny gold"]]
contains_sg = []
while cbags:
    currbag = cbags.pop()
    for subbag in currbag.contained_by:
        # logger.debug(f"{subbag.color} contains {currbag.color}")
        cbags.append(subbag)
        contains_sg.append(subbag.color)

# count the number of bags that are around a shiny gold bag
part1 = len(set(contains_sg))
logger.success(f"part 1: {part1}")

# count the number of bags inside shiny gold
part2 = bags["shiny gold"].count_inside(bags)
logger.success(f"part 2: {part2}")
