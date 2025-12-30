import sys
from queue import Queue
input = sys.stdin.readline

N = int(input())
que = Queue()

for _ in range(N):
    line = input().split()
    instr = line[0]
    
    if instr == "push":
        x = line[1]
        que.put(x)
    elif instr == "pop":
        if que.empty():
            print(-1)
            continue
        print(que.get())
    elif instr == "size":
        print(que.qsize())
    elif instr == "empty":
        print(1 if que.empty() else 0)
    elif instr == "front":
        if que.empty():
            print(-1)
            continue
        print(que.queue[0])
    elif instr == "back":
        if que.empty():
            print(-1)
            continue
        print(que.queue[-1])