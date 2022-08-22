# 9020 - 골드바흐의 추측

import sys
input = sys.stdin.readline

testCase = int(input())
data = 100000
def prime():
    primeList = [0] * (data+1)

    # 리스트 초기화
    for i in range(2, data+1):
        primeList[i] = i

    for i in range(2, int(data ** 0.5)+1):
        if primeList[i] != 0:
            j = 2
            while i*j < data:
                primeList[i*j] = 0
                j += 1

    return primeList

def goldbach(primeList, number):
    for i in range(0, number, 1):
        if primeList[number//2-i] + primeList[number//2+i] == number:
            print(primeList[number//2-i], primeList[number//2+i])
            return

primeList = prime()

for _ in range(testCase):
    X = int(input().rstrip())
    goldbach(primeList, X)
