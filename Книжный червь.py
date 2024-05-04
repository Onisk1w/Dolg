import sys
print("Введите данные ")
numbers = [int(x) for x in sys.stdin.readline().split()]

thinkness_of_volume = numbers[0] #толщина тома
thinkness_of_cover = numbers[1] #толщина переплета
volume_begin = numbers[2] #номер тома с первого листа
volume_end = numbers[3] #номер тома с последнего листа

if volume_end > volume_begin:
    volume_count = volume_end - volume_begin - 1
    lenght = volume_count * (thinkness_of_volume + 2 * thinkness_of_cover) + 2 * thinkness_of_cover
else:
    volume_count = volume_begin - volume_end + 1
    lenght = (volume_count - 1) * (thinkness_of_volume + 2 *thinkness_of_cover) + thinkness_of_volume

print(lenght)