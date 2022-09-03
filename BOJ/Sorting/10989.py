# 10989 - 수 정렬하기 3

import sys
input = sys.stdin.readline

N = int(input().rstrip())
count = [0] * (10000+1)

for _ in range(N):
    num = int(input().rstrip())
    count[num] += 1         # 수의 개수 저장

for j in range(1, len(count)):
    while count[j] != 0:
        count[j] -= 1
        print(j)