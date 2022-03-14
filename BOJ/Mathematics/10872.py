# 10872 - 팩토리얼
import sys
input = sys.stdin.readline().rstrip()
n = int(input)

def fact(num) :
    if num == 0 :
        return 1
    return fact(num - 1) * num
print(fact(n))
