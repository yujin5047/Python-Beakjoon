import sys

input = sys.stdin.readline

n = int(input())
default = 666
current_num = default
cnt = 0
while True:
    if "666" in str(current_num):
        cnt += 1
        if cnt == n:
            break
    current_num += 1
print(current_num)