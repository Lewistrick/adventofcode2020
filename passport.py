class Passport:
    reqfields = ("byr", "iyr", "eyr", "hgt",
                 "hcl", "ecl", "pid")
    optfields = ("cid", )

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

    def is_valid(self):
        """Checks validity of a passport (day 4 part 1)"""
        return all(hasattr(self, attr) for attr in self.reqfields)