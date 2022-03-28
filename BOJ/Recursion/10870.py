# 10870 - 피보나치 수 5

import sys 
input = sys.stdin.readline
n = int(input().rstrip())

def fibo(n) :
    if n <= 1 :
        return n            # 0 또는 1일 때 자기자신 반환
    else :
        return fibo(n-1) + fibo(n-2)
print(fibo(n))


