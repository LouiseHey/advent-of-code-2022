from itertools import groupby


def calculate_max_calories(filename):
    return max([sum(c) for c in [[int(a) for a in b] for b in [list(g) for k, g in groupby([line.rstrip() for line in open(filename).readlines()], key=bool) if k]]])


if __name__ == "__main__":
    filename = "day1.txt"
    maxCals = calculate_max_calories(filename)
    print(maxCals)