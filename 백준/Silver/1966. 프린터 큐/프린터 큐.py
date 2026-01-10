import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for i in range(t):
    N, M = map(int, input().split())
    que = deque()
    priority = list(map(int, input().split()))
    cnt = 0
    for j in range(N):
        que.append((priority[j], j))
    while True:
        if que[0][0] != max(que, key=lambda x: x[0])[0]:
            que.rotate(-1)
        else:
            popValue = que.popleft()
            cnt += 1
            if popValue[1] == M:
                print(cnt)
                break
