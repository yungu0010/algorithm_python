# 빠른 A + B
# input 대신 sys.stdin.readline 사용
# 단, 맨 긑 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶은 경우 .rstrip()추가

import sys

input = sys.stdin.readline
n = int(input())

for i in range(n) :
    a, b = map(int, input().split())
    print(a + b)

