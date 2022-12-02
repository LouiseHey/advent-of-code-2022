
def read_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()
        return [line.rstrip() for line in lines]


def calculate_score(strategy_guide):
    strategy_split = [i.split(" ") for i in strategy_guide]

    total_score = 0
    for strategy in strategy_split:
        my_play = decide_play(strategy[0], strategy[1])
        total_score += calculate_score_points(my_play)
        total_score += calculate_win_points(strategy[0], my_play)
    return total_score


def decide_play(opponents_play, decide_win):
    opponents_play_converted = convert(opponents_play)

    if decide_win == "Y":
        return opponents_play_converted
    if decide_win == "Z":
        if opponents_play_converted == "X":
            return "Y"
        if opponents_play_converted == "Y":
            return "Z"
        if opponents_play_converted == "Z":
            return "X"
    if decide_win == "X":
        if opponents_play_converted == "X":
            return "Z"
        if opponents_play_converted == "Y":
            return "X"
        if opponents_play_converted == "Z":
            return "Y"


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