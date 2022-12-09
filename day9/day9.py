from aocd import submit, data
from math import copysign
from collections import dequeue

EMPTY = object()
solution_one, solution_two = [EMPTY, EMPTY]
# grab data (Cached)s
# puzzle_data = data

# sample data
puzzle_data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip()
# -- code below --
instructions = [i.split() for i in puzzle_data.splitlines()]
instructions = list(map(lambda x: (x[0], int(x[1])), instructions))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj2):
        if isinstance(obj2, Point):
            p = Point(self.x, self.y)
            p.x += obj2.x
            p.y += obj2.y
            return p

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Point):
            if __o.x == self.x and __o.y == self.y:
                return True
        return False

    def __hash__(self) -> int:
        return hash(str(self.x) + "," + str(self.y))

    def __repr__(self) -> str:
        return f"<Point {self.x=} {self.y=}>"


# Coords (bottom-left = 0,0)
HEAD = Point(0, 0)
TAIL = Point(0, 0)
DIRECTIONS = {"U": Point(0, 1), "D": Point(0, -1), "L": Point(-1, 0), "R": Point(1, 0)}
VISITED = set()
VISITED.add(Point(0, 0))
for letter, count in instructions:
    for _ in range(count):
        # move the head
        HEAD += DIRECTIONS[letter.upper()]
        # follow with tail
        # cases: 2 away, diagonal
        x_diff = HEAD.x - TAIL.x
        y_diff = HEAD.y - TAIL.y
        # ex: 2 up 1 right -> 1 up 1 right
        # ex: 1 up 2 right -> 1 up 1 right
        if abs(x_diff) >= 2 or abs(y_diff) >= 2:
            if x_diff != 0:
                x_diff = copysign(1, x_diff)
            if y_diff != 0:
                y_diff = copysign(1, y_diff)
            TAIL += Point(x_diff, y_diff)
            VISITED.add(TAIL)


solution_one = len(VISITED)

# Automated Submission
if solution_one != EMPTY:
    submit(solution_one, part="a")
if solution_two != EMPTY:
    submit(solution_two, part="b")
