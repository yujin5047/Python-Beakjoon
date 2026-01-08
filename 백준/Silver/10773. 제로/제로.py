import sys
input = sys.stdin.readline

K = int(input())
stack_lst = []
for _ in range(K):
    num = int(input())
    if num == 0:
        stack_lst.pop()
    else:
        stack_lst.append(num)
print(sum(stack_lst))