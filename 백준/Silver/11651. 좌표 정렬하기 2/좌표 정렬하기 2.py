import sys
input = sys.stdin.readline

N = int(input())
result_lst = []
for _ in range(N):
    x,y = map(int, input().split())
    result_lst.append([x,y])
result_lst.sort(key=lambda x: (x[1], x[0]))
for xy in result_lst:
    print(*xy)