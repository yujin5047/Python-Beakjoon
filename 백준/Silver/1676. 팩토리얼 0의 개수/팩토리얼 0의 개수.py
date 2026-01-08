import sys
input = sys.stdin.readline

N = int(input())
number = 1
for i in range(N, 1, -1):
    number *= i
str_num = str(number)

print(len(str_num) - len(str_num.rstrip('0')))