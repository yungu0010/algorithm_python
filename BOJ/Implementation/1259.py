# 1259 - 팰린드롬수

import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if int(n) == 0:
        break
    reverseNum = "".join(reversed(n))
    if n == reverseNum:
        print("yes")
    else:
        print("no")