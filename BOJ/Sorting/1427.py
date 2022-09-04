# 1427 - 소트인사이드

import sys
input = sys.stdin.readline

number = list(map(int, input().rstrip()))
number.sort()

for i in range(len(number)-1, -1, -1):
    print(number[i], end= "")