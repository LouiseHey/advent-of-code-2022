filename = "day1.txt"

with open(filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = []
temp = 0
for line in lines:
    if line != "":
        temp += int(line)
    else:
        numbers.append(temp)
        temp = 0

numbers.sort(reverse=True)
sum = numbers[0] + numbers[1] + numbers[2]

print(sum)