import sys
input = sys.stdin.readline

t = int(input())
zero_cnt, one_cnt = [0] * 41, [0] * 41
zero_cnt[0] = 1
one_cnt[1] = 1

for i in range(2, 41):
    zero_cnt[i] = zero_cnt[i - 1] + zero_cnt[i - 2]
    one_cnt[i] = one_cnt[i - 1] + one_cnt[i - 2]
for _ in range(t):
    n = int(input())
    print(zero_cnt[n], one_cnt[n])
