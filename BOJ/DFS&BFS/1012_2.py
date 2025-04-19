# 1012 - 유기농 배추

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(y, x, visit):
    visit[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위를 벗어나는 경우
        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        if cabbage[ny][nx] == 1 and not visit[ny][nx]:
            dfs(ny, nx, visit)

T = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(T):
    w, h, k = map(int, input().split())
    cabbage = [[0] * w for _ in range(h)]
    visit = [[False] * w for _ in range(h)]

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if cabbage[i][j] == 1 and not visit[i][j]:
                dfs(i, j, visit)
                answer += 1
    
    print(answer)