import sys

input = sys.stdin.readline
S = input()
tag = False
word = ""
ans = ""
for s in S:
    if s == "<":
        if word:
            ans += word[::-1]
            word = ""
        tag = True
        ans += s

    elif s == ">":
        tag = False
        ans += s
    elif s == " " or s == "\n":
        if tag:
            ans += s
        else:
            ans += word[::-1]
            ans += s
            word = ""
    else:
        if tag:
            ans += s
        else:
            word += s
print(ans)