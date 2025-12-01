input = open('input.txt').readlines()

curr = 50
zeros = 0

for line in input:
    sign = -1 if line[0] == 'L' else 1
    dist = int(line[1:])

    curr = (curr + sign * dist) % 100

    if curr == 0:
        zeros += 1

print(zeros)
