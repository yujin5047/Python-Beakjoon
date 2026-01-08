
import sys
input = sys.stdin.readline

N = int(input())
number = 1
flag = False
cnt = 0
for i in range(N, 1, -1):
    number *= i
str_num = str(number)
for i in range(len(str_num) -1, 0, -1):
    if "0" in str_num[i]:
        cnt += 1
        if str_num[i-1] != "0":
            break
    
    
print(cnt)