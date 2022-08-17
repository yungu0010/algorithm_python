# 1712 - 손익분기점

import sys
from tkinter import N
input = sys.stdin.readline

A, B, C = map(int, input().split())

n = 1

while True:
    if B > C:
        print(-1)
        break
    if C * n > A + B*n:
        print(n)
        break
    else:
        n += 1