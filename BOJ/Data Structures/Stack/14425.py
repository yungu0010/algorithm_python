# 14425 - 문자열 집합

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nList = []
count = 0

for _ in range(N):
    nList.append(input())

for _ in range(M):
    mString = input()
    if mString in nList:
        count += 1

print(count)