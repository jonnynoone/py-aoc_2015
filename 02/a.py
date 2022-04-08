with open('input.txt') as file:
    raw_input = file.read()

input = raw_input.split('\n')

total_paper = 0

for line in input:
    dimensions = line.split('x')
    sides = [
        int(dimensions[0]) * int(dimensions[1]),
        int(dimensions[0]) * int(dimensions[2]),
        int(dimensions[1]) * int(dimensions[2])
    ]
    surface_area = 2 * (sides[0] + sides[1] + sides[2])

    if sides[0] <= sides[1] and sides[0] <= sides[2]:
        smallest_side = sides[0]
    elif sides[1] <= sides[0] and sides[1] <= sides[2]:
        smallest_side = sides[1]
    elif sides[2] <= sides[0] and sides[2] <= sides[1]:
        smallest_side = sides[2]

    total_paper += surface_area + smallest_side

print(total_paper)