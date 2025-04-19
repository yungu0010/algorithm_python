# 1759 - 암호 만들기
# 서로 다른 L개의 알파벳 소문자로 구성
# 최소 1개의 모음, 최소 2개의 자음으로 구성
# 오름차순으로 구성

import sys
from itertools import *
input = sys.stdin.readline

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()

vowel = ['a', 'e', 'i', 'o', 'u']
answer = []
candidate = list(combinations(alpha, l))

for c in candidate:
    vowelCount = sum(char in vowel for char in c)
    if sum(char in vowel for char in c) >= 1 and len(c) - vowelCount >= 2:
        answer.append(c)

for a in answer:
    print(''.join(a))