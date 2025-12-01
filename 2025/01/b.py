input = open('input.txt').readlines()

curr = 50
zeros = 0

for line in input:
    sign = -1 if line[0] == 'L' else 1
    dist = int(line[1:])

    # naive
    # for i in range(number):
    #     curr = (curr + sign) % 100
    #     if curr == 0:
    #         zeros += 1

    if sign == 1: # right
        # (curr + t) % 100 == 0, for 1 <= t <= dist
        t0 = 100 if curr == 0 else 100 - curr
    else: # left
        # (curr - t) % 100 == 0, for 1 <= t <= dist
        t0 = 100 if curr == 0 else curr

    if t0 <= dist:
        zeros += 1 + (dist - t0) // 100

    curr = (curr + sign * dist) % 100

print(zeros)
