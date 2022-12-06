def get_input(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    return lines[0]


def find_marker(data_stream):
    for i in range(len(data_stream) - 13):
        four_recent_chars = data_stream[i:i+14]
        if len(set(four_recent_chars)) == 14:
            return i + 14


if __name__ == "__main__":
    filename = "day6.txt"
    inputData = get_input(filename)
    marker = find_marker(inputData)
    print(marker)
