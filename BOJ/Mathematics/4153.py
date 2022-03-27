# 4153 - 직각삼각형

import sys
import math

input = sys.stdin.readline
n = []
while True :
    n = list(map(int,input().rstrip().split()))
    if n[0] == 0 and n[1] == 0 and n[2] == 0 :          # sum(n) == 0으로 더 간결하게 작성 가능
        break;
    big = max(n)
    sum = 0

    for i in n :
        if i != big :
            sum += pow(i,2)
    if math.pow(big,2) == sum :
        print("right")
    else :
        print("wrong")
        
# for문 대신 n을 정렬하여 0, 1번째 원소 제곱 == 2원소 제곱으로 if문 사용하면 시간복잡도 줄일 수 있음
    # n.sort()
    # if math.pow(big,2) == n[0]**2 + n[1]**2 :