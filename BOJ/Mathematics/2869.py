# 2869 - 달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())

day = (V - A) // (A - B)
if (V - A) % (A - B) == 0:
    print((V - A) // (A - B) + 1)
else:
    print((V - A) // (A - B) + 2)