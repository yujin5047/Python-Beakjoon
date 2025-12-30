while True:
    test_input = int(input())
    if test_input == 0:
        break
    
    flag = True
    test_input = str(test_input)
    half_length = len(test_input) // 2
    
    for i in range(half_length):
        if test_input[i] != test_input[-1-i]:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")