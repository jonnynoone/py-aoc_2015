floor = 0

with open('input.txt') as file:
    input = file.read()

for i in range(len(input)):
    if input[i] == '(':
        floor += 1
    elif input[i] == ')':
        floor -= 1

    if floor == -1:
        position = i + 1
        break

print(position)