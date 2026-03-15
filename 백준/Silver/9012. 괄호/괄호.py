import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    line = input()
    stack = []
    for s in line:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")