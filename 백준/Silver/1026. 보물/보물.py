N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for i in range(N):
    max_B = max(B)
    min_A = min(A)
    S += min_A * max_B
    B.remove(max_B)
    A.remove(min_A)

print(S)