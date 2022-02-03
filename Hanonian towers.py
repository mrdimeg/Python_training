import math

discs = 20

def solve_hanoi_tower(discs):
    count = (math.pow(2, discs) - 1)
    return int(count)


solve_hanoi_tower(discs)
print(solve_hanoi_tower(discs))
