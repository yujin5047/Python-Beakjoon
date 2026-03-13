import sys
input = sys.stdin.readline
ISBN = list(input().rstrip())
m = ISBN[-1]
ruin_idx = ISBN.index("*")

for test_num in range(10):
    num = 0
    for idx in range(12):
        mult_num = int(ISBN[idx]) if idx != ruin_idx else test_num
        if idx % 2 == 0:
            num += mult_num
        else:
            num += 3 * mult_num
    if int(m) == (10 - num) % 10:
        print(test_num)
        break
