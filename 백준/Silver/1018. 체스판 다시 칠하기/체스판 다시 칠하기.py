import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
cnt = []

for _ in range(n):
    line = input().rstrip()
    matrix.append(line)

for a in range(n - 7):
    for b in range(m - 7):
        w_start = 0
        b_start = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:  # w_start => "W", b_start => "B"
                    if matrix[i][j] == "W":
                        b_start += 1
                    else:
                        w_start += 1
                else:  # 홀수인 경우
                    if matrix[i][j] == "B":
                        b_start += 1
                    else:
                        w_start += 1
        cnt.append(w_start)
        cnt.append(b_start)
        
print(min(cnt))