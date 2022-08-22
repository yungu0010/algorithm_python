# 4948 - 베르트랑 공준

import sys, math
input = sys.stdin.readline


def primeNumber(n, m):
    count = 0
    prime = [0] * (m+1)

# 배열 초기화
    for k in range(1, m+1):
        prime[k] = k

# m의 제곱근의 배수까지만 지움
    for i in range(2, int(m**0.5) + 1):
        for j in range(i+i, m+1, i):
            prime[j] = 0
        
    for i in range(n+1, m+1):
        if prime[i] == 0 or prime[i] == 1:      # 1은 소수가 아님
            continue
        count += 1
    return count
        
while True:
    n = int(input())
    if n == 0:
        break
    print(primeNumber(n, 2*n))


