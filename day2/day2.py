
def read_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def calculate_score(strategy_guide):
    strategy_split = [i.split(" ") for i in strategy_guide]

    total_score = 0
    for strategy in strategy_split:
        total_score += calculate_score_points(strategy[1])
        total_score += calculate_win_points(strategy[0], strategy[1])
    return total_score


def calculate_score_points(my_play):
    if my_play == "X":
        return 1
    if my_play == "Y":
        return 2
    if my_play == "Z":
        return 3


def calculate_win_points(opponents_play, my_play):
    opponents_play_converted = convert(opponents_play)
    if opponents_play_converted == my_play:
        return 3
    if (opponents_play_converted == "X" and my_play == "Y") or (opponents_play_converted == "Y" and my_play == "Z") or (opponents_play_converted == "Z" and my_play == "X"):
        return 6
    else:
        return 0


def convert(play):
    if play == "A":
        return "X"
    if play == "B":
        return "Y"
    if play == "C":
        return "Z"


if __name__ == "__main__":
    filename = "day2.txt"
    lines = read_input(filename)
    score = calculate_score(lines)
    print(score)