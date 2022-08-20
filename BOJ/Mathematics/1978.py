# 1978 - 소수 찾기

import sys, math
input = sys.stdin.readline

N = int(input())
numberList = list(map(int, input().split()))

result = 0

def prime(p):
    global result 
    
    if p < 2:
        return
    for j in range(2, p):
        if p%j == 0:
            return
    result += 1

for i in numberList:
    prime(i)

print(result)