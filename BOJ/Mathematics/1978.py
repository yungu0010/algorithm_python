# 1978 - 소수찾기

import sys, math

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
count = 0

for i in num :
    if i >= 2 :
        for j in range(2, i) :
            print(i, j)
            if i % j != 0 :
                count+= 1
                break
            
        
print(count)