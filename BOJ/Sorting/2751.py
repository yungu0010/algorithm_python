# 수 정렬하기 2

import sys
input = sys.stdin.readline
n = int(input().rstrip())
result = []

for i in range(n) :
    a = int(input().rstrip())
    result.append(a)

result.sort()
for i in result :
    print(i)