import sys
input = sys.stdin.readline

M = 1234567891
r = 31
L = int(input())
sentence = list(input().rstrip())

def hashing(lst_S):
    for i in range(L):
        lst_S[i] = ord(lst_S[i]) - 96
        lst_S[i] = lst_S[i] * (r ** (i)) % M
    return sum(lst_S) % M

print(hashing(sentence))
