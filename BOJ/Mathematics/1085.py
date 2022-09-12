# 1085 - 직사각형에서 탈출

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().rstrip().split())

x1 = w - x
y1 = h - y

print(min(x, y, x1, y1))