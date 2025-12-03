# input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
input = open('input.txt').read()

import textwrap

count = 0

for id_range in input.split(','):
    start, end = id_range.split('-')
    start, end = int(start), int(end)
    for number in range(start, end + 1):
        number_str = str(number)
        number_len = len(number_str)
        divisors = [i for i in range(1, number_len) if number_len % i == 0]
        for divisor in divisors:
            parts = textwrap.wrap(number_str, divisor)
            if len(set(parts)) == 1:
                count += number
                break

print(count)
