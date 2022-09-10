# 11050 - 이항 계수 1

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numerator = 1
denominator = 1

# 분자 구하기
for i in range(K):
    numerator *= (N-i)

# 분모 구하기
for j in range(K):
    denominator *= (K-j) 

print(int(numerator/denominator))