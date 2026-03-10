import sys
input = sys.stdin.readline

stack_list = []

def push(k):
    stack_list.append(k)

def pop():
    if stack_list:
        pop_num = stack_list.pop(-1)
    else:
        pop_num = -1
    print(pop_num)

def top():
    if stack_list:
        pop_num = stack_list[-1]
    else:
        pop_num = -1
    print(pop_num)

def size():
    print(len(stack_list))

def empty():
    print(int(bool(not (stack_list))))

n = int(input())
for _ in range(n):
    line = input().split()
    instr = line[0]
    if instr == "push":
        push(line[1])
    elif instr == "pop":
        pop()
    elif instr == "top":
        top()
    elif instr == "size":
        size()
    elif instr == "empty":
        empty()
