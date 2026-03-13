import sys
input = sys.stdin.readline
m = int(input())
S = set()

def add_x(x):
    S.add(x)

def remove_x(x):
    S.discard(x)

def check_x(x):
    if x in S:
        print(1)
    else:
        print(0)

def toggle_x(x):
    if x in S:
        S.discard(x)
    else:
        S.add(x)

def all():
    global S
    S = set(range(1, 21))

def empty():
    global S
    S.clear()

for _ in range(m):
    line = list(map(str, input().split()))
    if line[0] == "add":
        add_x(int(line[1]))
    elif line[0] == "check":
        check_x(int(line[1]))
    elif line[0] == "remove":
        remove_x(int(line[1]))
    elif line[0] == "toggle":
        toggle_x(int(line[1]))
    elif line[0] == "all":
        all()
    else:
        empty()
