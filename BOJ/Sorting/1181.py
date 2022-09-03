# 1181 - 단어 정렬 

import sys
input = sys.stdin.readline

N = int(input().rstrip())
words = []

for _ in range(N):
    words.append(input().rstrip())

words = list(set(words))        # 중복 제거
words.sort(key = lambda x: (len(x), x)) # 길이순 정렬 -> 알파벳 순 정렬

for i in words:
    print(i)