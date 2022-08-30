# 7568 - 덩치

import sys
input = sys.stdin.readline

N = int(input().rstrip())
info = []
result = []

for _ in range(N):
    info.append(list(map(int, input().split())))

for i in range(N):
    level = 1
    kg = info[i][0]
    cm = info[i][1]
    for j in range(N):
        if j == i:
            continue
        if kg > info[j][0] and cm > info[j][1]:
            continue
        elif kg < info[j][0] and cm < info[j][1]:
            level += 1
    result.append(level)

print(' '.join(str(i) for i in result))
