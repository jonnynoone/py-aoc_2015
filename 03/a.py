with open('input.txt') as file:
    input = file.read()

location = {'x': 0, 'y': 0}
houses_visited = [{'x': 0, 'y': 0}]

for char in input:
    if char == '^':
        location['y'] += 1
    elif char == '>':
        location['x'] += 1
    elif char == 'v':
        location['y'] += -1
    elif char == '<':
        location['x'] += -1

    current_location = location.copy()
    if current_location not in houses_visited:
        houses_visited.append(current_location)

print(f'Number of houses visited: {len(houses_visited)}')