N = int(input())
curr_length = 64
num_rod = 0
result_length = 0

while True:
    if result_length == N or curr_length == N:
        if curr_length == N:
            num_rod = 1
        print(num_rod)
        break
    curr_length = curr_length * 0.5
    if result_length + curr_length <= N:
        result_length += curr_length
        num_rod += 1