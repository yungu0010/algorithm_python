# 1676 - 팩토리얼 0의 개수

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 팩토리얼 계산 함수
def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

fNum = factorial(N)
result = list(str(fNum))
countZero = 0

for _ in range(len(result)):
    if result.pop() != '0':
        break
    else:
        countZero += 1

print(countZero)
