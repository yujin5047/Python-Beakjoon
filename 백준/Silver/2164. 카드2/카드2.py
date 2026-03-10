import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
cards = deque(list(range(1, n + 1)))
while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])