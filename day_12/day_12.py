"""--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?"""


class Day12():
    def __init__(self, input: str) -> None:
        self.input = self.parse_input(input)
        self.start_pos = self.find(self.input, "S")
        self.end_pos = self.find(self.input, "E")

    def parse_input(self, input: str) -> list[list[str]]:
        input = input.split("\n")
        return [[c for c in line] for line in input]

    def task_1(self):
        pass

    def find(self, matrix: list[list], target) -> tuple[int]:
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c == target:
                    return (i, j)

    def can_climb(self, start: str, destination: str) -> bool:
        return ord(destination) - ord(start) == 0

    def check_sides(self, hill_pos: tuple[int]) -> list[tuple[int]]:
        sides = []
        curr_hill = self.input[hill_pos[0]][hill_pos[1]]
        if hill_pos[0] > 0:
            sides.append(self.input[hill_pos[0] - 1][hill_pos[1]])
        if hill_pos[0] < len(self.input) - 1:
            sides.append(self.input[hill_pos[0] + 1][hill_pos[1]])
        if hill_pos[1] > 0:
            sides.append(self.input[hill_pos[0]][hill_pos[1] - 1])
        if hill_pos[1] < len(self.input[0]) - 1:
            sides.append(self.input[hill_pos[0]][hill_pos[1] + 1])
        filter(lambda x: self.can_climb(curr_hill, x), sides)
        return sides


if __name__ == "__main__":
    with open("test_input.txt", "r") as file:
        input = file.read()
    day_12 = Day12(input)
    print(day_12.task_1())
