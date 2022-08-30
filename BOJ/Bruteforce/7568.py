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
        if j == i:      # 나 자신과 비교
            continue
        if kg > info[j][0] and cm > info[j][1]:     # 덩치가 더 클 때
            continue
        elif kg < info[j][0] and cm < info[j][1]:   # 덩치가 더 작을 때
            level += 1
    result.append(level)

print(' '.join(str(i) for i in result))
