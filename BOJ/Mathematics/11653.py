# 11653 - 소인수분해

import sys
input = sys.stdin.readline

n = int(input().strip())
num = 2


def divide(operand):
    global n, num
    if n % operand == 0:
        result = n / operand
        print(operand)
        n = result
        return result
    else:
        num += 1
        return n

while n != 1:
    divide(num)
