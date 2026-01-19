import sys
input = sys.stdin.readline

n = int(input())
group_lst = []
result_lst = []
for _ in range(n):
    x, y = map(int, input().split())
    group_lst.append((x, y))
for i in range(n):
    cnt = 1
    for j in range(n):
        if group_lst[i][0] < group_lst[j][0]:  # x가 큼
            if group_lst[i][1] < group_lst[j][1]:  # y도 큼
                cnt += 1
    result_lst.append(cnt)
print(*result_lst)