# 25304 - 영수증

import sys

input = sys.stdin.readline

X = int(input().rstrip())
N = int(input().rstrip())
sum = 0

def calculate(a, b):
    global sum
    sum += a * b
    return

def compare(sum, X):
    if sum == X:
        print("YES")
    else:
        print("NO")

for _ in range(0, N):
    a, b = map(int, input().split())
    calculate(a, b)

compare(sum, X)