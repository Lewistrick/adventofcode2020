import re
from loguru import logger

class Passport:
    reqfields = ("byr", "iyr", "eyr", "hgt",
                 "hcl", "ecl", "pid")
    optfields = ("cid", )

    field_rx = {
        "hgt": re.compile(r"^([0-9]{2,3})(cm|in)$"),
        "hcl": re.compile(r"^#[0-9a-f]{6}$"),
        "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
        "pid": re.compile(r"^([0-9]{9})$")
    }

    def __init__(self, **kwargs):
        for kwarg, value in kwargs.items():
            setattr(self, kwarg, value)

    @classmethod
    def from_lines(cls, lines: str):
        """Read lines and return a Passport object"""
        kwargs = {}
        for field in lines.split():
            key, val = field.split(":")
            kwargs[key] = val
        return cls(**kwargs)

    def is_valid_day04_part1(self):
        """Checks validity of a passport (day 4 part 1)"""
        return all(hasattr(self, attr) for attr in self.reqfields)

    def is_valid_day04_part2(self):
        if not self.is_valid_day04_part1():
            logger.debug("Invalid: not all required fields present")
            return False
        # birth year
        if int(self.byr) not in range(1920, 2003):
            logger.debug(f"Invalid birth year {self.byr}")
            return False
        # issue year
        if int(self.iyr) not in range(2010, 2021):
            logger.debug(f"Invalid issue year {self.iyr}")
            return False
        # expiration year
        if int(self.eyr) not in range(2020, 2031):
            logger.debug(f"Invalid expiration year {self.eyr}")
            return False
        # height
        hgtmatch = self.field_rx["hgt"].match(self.hgt)
        if not hgtmatch:
            logger.debug(f"Invalid height: {self.hgt}")
            return False
        value, unit = hgtmatch.groups()
        if unit == "cm" and int(value) not in range(150, 194):
            logger.debug(f"Too short/tall: {self.hgt}")
            return False
        elif unit == "in" and int(value) not in range(59, 77):
            logger.debug(f"Too short/tall: {self.hgt}")
            return False
        elif unit not in ("cm", "in"):
            logger.debug(f"Invalid unit: {self.hgt}")
            return False
        # hair color
        hclmatch = self.field_rx["hcl"].match(self.hcl)
        if not hclmatch:
            logger.debug(f"Invalid hair color: {self.hcl}")
            return False
        # eye color
        eclmatch = self.field_rx["ecl"].match(self.ecl)
        if not eclmatch:
            logger.debug(f"Invalid eye color match: {self.ecl}")
            return False
        # passport ID
        pidmatch = self.field_rx["pid"].match(self.pid)
        if not pidmatch:
            logger.debug(f"Invalid passport ID: {self.pid}")
            return False

        logger.success("Valid!")
        return True