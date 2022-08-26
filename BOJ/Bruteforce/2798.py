# 2798 - 블랙잭

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cards = list(map(int, input().split()))
plusNum = 0
temp = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            print(temp)
            if temp > M:
                continue
            if plusNum < temp:
                plusNum = temp

print(plusNum)
