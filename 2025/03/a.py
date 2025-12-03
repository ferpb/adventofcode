# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111""".splitlines()

input = open('input.txt').read().splitlines()

count = 0

for bank in input:
    print(bank)
    # para cada bank, dos punteros
    # uno intenta buscar el número más grande y otro el número más grande
    # que está a la derecha de ese número
    left, right = 0, 1
    for i in range(1, len(bank)):
        if bank[i] > bank[left] and i < len(bank) - 1:
            left = i
            right = i + 1
        elif bank[i] > bank[right]:
            right = i

    number = int(bank[left]) * 10 + int(bank[right])

    print(number)

    count += number

print(count)
