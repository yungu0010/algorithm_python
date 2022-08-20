# 1929 - 소수 구하기

import sys, math
input = sys.stdin.readline

M, N = map(int, input().split())

def prime(p):
    if p < 2:
        return
    for i in range(2, int(math.sqrt(p)+1)):
        if p % i == 0:
            return
    print(p)

for i in range(M, N+1):
    prime(i)