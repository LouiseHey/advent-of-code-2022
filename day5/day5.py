def convert_moves(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    lines = [l.rstrip().split(" ") for l in lines]
    lines = [[int(l) for l in a if l.isdigit()] for a in lines]

    moves = []
    for move in lines:
        moves.append(Move(move[0], move[1], move[2]))
    return moves


def convert_drawing(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    lines.reverse()

    stack_indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    stacks = []

    for i in stack_indices:
        stack = Stack()
        for line in lines:
            if line[i].isdigit():
                stack.set_id(line[i])
            elif line[i] == " ":
                break
            else:
                stack.add([line[i]])

        stacks.append(stack)

    return stacks


class Stack:
    def __init__(self):
        self.idNo = None
        self.boxes = []

    def add(self, new_boxes):
        self.boxes += new_boxes

    def set_id(self, stack_id):
        self.idNo = stack_id

    def pop(self, number_of_boxes):
        popped_boxes = []
        for i in range(number_of_boxes):
            popped_boxes.append(self.boxes.pop())
        return popped_boxes

    def get_top_box(self):
        return self.boxes[-1]


class Move:
    def __init__(self, number_of_boxes, initial_stack, end_stack):
        self.number_of_boxes = number_of_boxes
        self.initial_stack = initial_stack
        self.end_stack = end_stack


def find_final_stacks(moves, stacks):
    for move in moves:
        popped_boxes = stacks[move.initial_stack-1].pop(move.number_of_boxes)
        stacks[move.end_stack-1].add(popped_boxes)

    final_top_box = ""
    for s in stacks:
        final_top_box += s.get_top_box()
    return final_top_box


if __name__ == "__main__":
    filename = "day5.txt"
    moves = convert_moves(filename)
    stacks = convert_drawing("day5-drawing.txt")
    answer = find_final_stacks(moves, stacks)
    print(answer)
