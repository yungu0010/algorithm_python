# 3003 - 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

input = sys.stdin.readline

chess = list(map(int, input().split()))
result = []
chessSet = [1, 1, 2, 2, 2, 8]

for c in range(len(chess)):
    result.append(chessSet[c] - chess[c])

for i in result:
    print(i, end = " ")
