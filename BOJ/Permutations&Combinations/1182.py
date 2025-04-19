# 1182 - 부분 수열의 합

import sys
from itertools import *
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
for i in range(1, n+1):
    combi = list(map(list, combinations(nums, i)))
    
    for c in combi:
        if sum(c) == s:
            answer += 1

print(answer)