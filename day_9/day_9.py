"""--- Day 9: Rope Bridge ---
This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...
If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...
Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....
You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....
After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..
So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?"""
from math import fabs


class Day9():
    def __init__(self, input: str) -> None:
        self.input = self.parse_input(input)

    def parse_input(self, input: str) -> list[list]:
        input = input.split("\n")
        return [row.split() for row in input]

    def task_1(self):
        return self.visited_tiles_amount()

    def visited_tiles_amount(self) -> int:
        self.visited_tiles = [[0, 0]]
        head = [0, 0]
        tail = [0, 0]
        for command in self.input:
            command_result = self.do_command(head, tail, command)
            head = command_result[0]
            tail = command_result[1]
        return len(self.visited_tiles)

    def do_command(self, head_pos: list[int], tail_pos: list[int], command: list) -> tuple[list[int]]:
        direction = command[0]
        steps = int(command[1])
        for _ in range(steps):
            match direction.lower():
                case "r":
                    head_pos[1] += 1
                case "l":
                    head_pos[1] -= 1
                case "u":
                    head_pos[0] -= 1
                case "d":
                    head_pos[0] += 1
            tail_pos = self.move_tail(tail_pos, head_pos)
            if tail_pos not in self.visited_tiles:
                self.visited_tiles.append(tail_pos)
        return (head_pos, tail_pos)

    def move_tail(self, tail_pos: list[int], head_pos: list[int]) -> list[int]:
        r_diff = head_pos[0] - tail_pos[0]
        c_diff = head_pos[1] - tail_pos[1]
        if fabs(r_diff) <= 1 and fabs(c_diff) <= 1:
            return tail_pos
        if r_diff < -1:
            r_diff = -1
        elif r_diff > 1:
            r_diff = 1
        if c_diff < -1:
            c_diff = -1
        elif c_diff > 1:
            c_diff = 1
        return [tail_pos[0] + r_diff, tail_pos[1] + c_diff]


if __name__ == "__main__":
    with open("day_9_input.txt", "r") as file:
        input = file.read()
    task = Day9(input)
    print(task.task_1())