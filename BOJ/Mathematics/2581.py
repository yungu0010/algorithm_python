# 2581 - 소수

import sys
input = sys.stdin.readline

M = int(input().strip())
N = int(input().strip())

arrPrime = []

# 소수 찾는 함수
def findPrime(num):
    checkPrime = 1
    for i in range(2, num):
        if num % i == 0:
            checkPrime = 0
            break
    if checkPrime == 1:
        arrPrime.append(num)

# 소수의 합 구하기
def addPrime():
    sum = 0
    for i in range(len(arrPrime)):
        sum += arrPrime[i]
    return sum

for p in range(M, N+1, 1):
    if p == 1:
        continue
    findPrime(p)

# 정답 출력
if len(arrPrime) != 0:
    print(addPrime())
    print(arrPrime[0])
else:
    print(-1)
