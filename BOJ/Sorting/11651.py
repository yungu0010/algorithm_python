# 11651 - 좌표 정렬하기 2

import sys
input = sys.stdin.readline

N = int(input().rstrip())
xy = []

for _ in range(N):
    coor = list(map(int, input().split()))
    xy.append(coor)

xy.sort(key = lambda x : (x[1], x[0]))

for i in range(len(xy)):
    print(xy[i][0], end = " ")
    print(xy[i][1])