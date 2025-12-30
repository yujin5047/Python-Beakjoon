import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    y = n % h
    x = n // h + 1
    if y == 0:
        x -= 1
        y = h
       
    
    x = str(x)
    y = str(y)
    if len(x) == 1:
        x = '0' + x
    result = y + x
    print(result)