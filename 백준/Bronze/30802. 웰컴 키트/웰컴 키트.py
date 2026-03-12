import sys
input = sys.stdin.readline

n = int(input())
size_need = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0
for need in size_need:
    if need % t == 0:
        t_cnt += need // t
    elif need > t:
        t_cnt += need // t + 1
    else:
        t_cnt += 1

p_cnt = n // p
p2_cnt = n % p
print(t_cnt)
print(p_cnt, p2_cnt)
