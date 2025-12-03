# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".splitlines()

input = open('input.txt').read().splitlines()

count = 0

for bank in input:
    pointers = list(range(12))

    for i in range(1, len(bank)):
        for j in range(len(pointers)):
            if bank[i] > bank[pointers[j]] and i + (len(pointers) - j - 1) < len(bank) and i not in pointers[:j]:
                for ki, k in enumerate(range(j, len(pointers))):
                    pointers[k] = i + ki
                break

    number = int(''.join([bank[ptr] for ptr in pointers]))
    # number = sum(map(lambda x: int(bank[x[1]]) * 10 ** x[0], enumerate(reversed(pointers))))

    count += number

print(count)
