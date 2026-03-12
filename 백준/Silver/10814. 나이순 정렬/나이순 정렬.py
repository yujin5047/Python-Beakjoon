import sys

input = sys.stdin.readline
info_lst = []
n = int(input())
for i in range(n):
    age, name = map(str, input().split())
    info_lst.append((int(age), name))
info_lst.sort(key=lambda x: x[0])
for i in range(n):
    print(info_lst[i][0], info_lst[i][1])
