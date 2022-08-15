# 25304 - 영수증

import sys

input = sys.stdin.readline

X = int(input().rstrip())
N = int(input().rstrip())
sum = 0

# 물건값 계산
def calculate(a, b):
    global sum
    sum += a * b
    return

# 총액과 비교
def compare(sum, X):
    if sum == X:
        print("Yes")
    else:
        print("No")

for _ in range(0, N):
    a, b = map(int, input().split())
    calculate(a, b)

compare(sum, X)