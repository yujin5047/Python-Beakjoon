import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
initial_circle = deque(range(1, n + 1))
result_lst = []

while initial_circle:
    initial_circle.rotate(-(k - 1))
    result_lst.append(initial_circle.popleft())

print("<", end="")
print(", ".join(map(str, result_lst)), end="")
print(">", end="")