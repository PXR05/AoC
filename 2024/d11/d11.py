import sys

sys.set_int_max_str_digits(10000)

input = open("input", "r").read().replace("\n", "").split(" ")
stones = {}
for num in input:
    stones[num] = stones.get(num, 0) + 1


def evolve(num, count):
    num_len = len(str(num))
    if num == 0:
        return [(1, count)]
    if num_len % 2 == 0:
        left = int(str(num)[: num_len // 2])
        right = int(str(num)[num_len // 2 :])
        return [(left, count), (right, count)]
    return [(num * 2024, count)]


n = 75
for i in range(n):
    new_stones = {}
    for num, count in stones.items():
        for new_num, new_count in evolve(num, count):
            new_stones[new_num] = new_stones.get(new_num, 0) + new_count
    stones = new_stones

print(sum(stones.values()))
