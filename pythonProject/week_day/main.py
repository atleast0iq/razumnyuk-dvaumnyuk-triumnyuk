class Day:
    lessons = []
    idx = 0

    def __init__(self, Lessons: list[str]):
        self.lessons = Lessons

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.lessons):
            self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return self.lessons[self.idx - 1]


class Week:
    days = []
    idx = 0

    def __init__(self, Days: list[Day]):
        self.days = Days

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.days):
            self.idx = 0
            raise StopIteration
        else:
            self.idx += 1
            return self.days[self.idx - 1]

week = Week([
    Day([ "inf", "soc", "phys" ]),
    Day([ "maths", "bio", "chem" ]),
    Day([ "sleep" ]),
    Day([ "eat" ]),
    Day([ "get drunk" ]),
    Day([ "repeat" ]),
    Day([ "pohmelye" ]),
])

for day in week:
    print("Schedule for this day:")
    for lesson in day:
        print(lesson)