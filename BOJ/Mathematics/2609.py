# 2609 - 최대공약수와 최소공배수

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
result = 0

# 최대공약수
def gcd(A, B):
    while B > 0:
        A, B = B, A % B
        result = A
    return result

# 최소공배수
def lcm(A, B):
    return print(int(A * B / gcd(A, B)))

print(gcd(A, B))
lcm(A, B)