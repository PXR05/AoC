from itertools import product

lines = open("input").read().split("\n")[:-1]
equations = [[line.split(":")[0], line.split(": ")[-1].split(" ")] for line in lines]


def eval(nums, ops, p2=False):
    res = int(nums[0])
    for i in range(len(ops)):
        if p2 and ops[i] == "||":
            res = int(str(res) + str(nums[i + 1]))
        elif ops[i] == "+":
            res += int(nums[i + 1])
        else:
            res *= int(nums[i + 1])
    return res


def check(res, nums, p2=False):
    if len(nums) == 1:
        return int(nums[0]) == res

    ops = ["+", "*", "||"] if p2 else ["+", "*"]
    ops_count = len(nums) - 1
    for operators in product(ops, repeat=ops_count):
        if eval(nums, operators, p2) == int(res):
            return True
    return False


total_p1 = total_p2 = 0
for eq in equations:
    res, nums = eq
    if check(int(res), nums, False):
        total_p1 += int(res)
    if check(int(res), nums, True):
        total_p2 += int(res)

print(total_p1)
print(total_p2)
