# 1712 - 손익분기점

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

n = 1

if B >= C:
    print(-1)
else:
    print(A // (C-B) + 1)