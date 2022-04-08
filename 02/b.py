with open('input.txt') as file:
    raw_input = file.read()

input = raw_input.split('\n')

total_paper = 0
total_ribbon = 0

for line in input:
    dimensions = line.split('x')
    for i in range(len(dimensions)):
        dimensions[i] = int(dimensions[i])

    sides = [
        dimensions[0] * dimensions[1],
        dimensions[0] * dimensions[2],
        dimensions[1] * dimensions[2]
    ]

    surface_area = 2 * (sides[0] + sides[1] + sides[2])
    ribbon_bow = dimensions[0] * dimensions[1] * dimensions[2]

    if sides[0] <= sides[1] and sides[0] <= sides[2]:
        smallest_side = sides[0]
        ribbon_wrap = dimensions[0] * 2 + dimensions[1] * 2
    elif sides[1] <= sides[0] and sides[1] <= sides[2]:
        smallest_side = sides[1]
        ribbon_wrap = dimensions[0] * 2 + dimensions[2] * 2
    elif sides[2] <= sides[0] and sides[2] <= sides[1]:
        smallest_side = sides[2]
        ribbon_wrap = dimensions[2] * 2 + dimensions[1] * 2

    total_paper += surface_area + smallest_side
    total_ribbon += ribbon_wrap + ribbon_bow

print(f'Total paper required: {total_paper}')
print(f'Total ribbon required: {total_ribbon}')