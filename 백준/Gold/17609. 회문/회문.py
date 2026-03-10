import sys
input = sys.stdin.readline

def palindrome(s):
    return s == s[::-1]

n = int(input())
for _ in range(n):
    string = input().strip()
    if palindrome(string):
        print(0)
        continue
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if palindrome(string[left + 1 : right + 1]):  # 유사회문 - 왼쪽 하나 제외
                print(1)
            elif palindrome(string[left:right]):  # 유사회문 - 오른쪽 하나 제외
                print(1)
            else:
                print(2)
            break
