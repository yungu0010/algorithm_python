# 7562 - 나이트의 이동

import sys
from collections import *
input = sys.stdin.readline

TC = int(input())

dy = [-2, -2, -1, -1, 1, 1, 2, 2]
dx = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visit[r][c] = True

    while queue:
        y, x = queue.popleft()

        if y == endY and x == endX:
            return

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
        
            if ny < 0 or ny >= m or nx < 0 or nx >= m:
                continue

            if not visit[ny][nx]:
                visit[ny][nx] = True
                count[ny][nx] = count[y][x] + 1
                queue.append((ny, nx))

for _ in range(TC):
    m = int(input())

    visit = [[False] * m for _ in range(m)]
    count = [[0] * m for _ in range(m)]

    startY, startX = map(int, input().split())
    endY, endX = map(int, input().split())
    bfs(startY, startX)
    print(count[endY][endX])