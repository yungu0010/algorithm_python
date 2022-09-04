# 25305 - 커트라인

import sys
input = sys.stdin.readline

N, K  = map(int, input().split())
score = []

score = list(map(int, input().split()))

score.sort()
print(score[-K])