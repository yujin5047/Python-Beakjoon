import sys
input = sys.stdin.readline
n = int(input())
bee_cnt = 1
cnt = 1

while bee_cnt < n:
    bee_cnt += 6 * cnt
    cnt += 1

print(cnt)