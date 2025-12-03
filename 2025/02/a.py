# input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
input = open('input.txt').read()

count = 0

for id_range in input.split(','):
    start, end = id_range.split('-')
    start, end = int(start), int(end)
    for i in range(start, end + 1):
        number_str = str(i)
        number_len = len(number_str)
        if number_len > 1 and number_len % 2 == 0:
            if number_str[:number_len // 2] == number_str[number_len // 2:]:
                count += int(number_str)

print(count)
