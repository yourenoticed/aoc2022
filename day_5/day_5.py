"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

"""


class Day5():
    def __init__(self, input: str) -> None:
        self.crates, self.instructions = self.parse_input(input)

    def parse_input(self, input: str) -> tuple[list]:
        input_l = input.split("\n\n")
        crates = self.parse_crates(input_l[0])
        instructions = self.parse_instructions(input_l[1])
        return (crates, instructions)

    def parse_instructions(self, instructions: str) -> list[list[int]]:
        instructions_l = instructions.split("\n")
        instruction_list = list()
        for instruction in instructions_l:
            instruction_list.append([int(c)
                                    for c in instruction.split() if c.isdigit()])
        return instruction_list

    def parse_crates(self, crates: str) -> list[str]:
        crates_l = crates.split("\n")
        result = list()
        for i in range(len(crates_l[-1])):
            if crates_l[-1][i].isdigit():
                result.append([crates_l[x][i] for x in range(
                    len(crates_l)) if not crates_l[x][i].isdigit() and crates_l[x][i] != " "])
        return result

    def move_shit(self, instruction: list[int]) -> None:
        fr = instruction[1] - 1
        to = instruction[2] - 1
        amount = instruction[0]
        to_move = self.crates[fr][:amount]
        to_move.reverse()
        for c in to_move:
            self.crates[fr].pop(0)
            self.crates[to].insert(0, c)

    def task(self) -> str:
        result = list()
        for inst in self.instructions:
            self.move_shit(inst)
        for l in self.crates:
            result.append(l[0])
        return "".join(result).strip()


if __name__ == "__main__":
    with open("day_5_input.txt", "r") as file:
        input = file.read()
    task = Day5(input)
    print(task.task())
