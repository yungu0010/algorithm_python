# 7576 - 토마토

from collections import *
from itertools import *
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def bfs(tomatos):
    queue = deque()
    
    for y, x in tomatos:
        queue.append((y, x))
        visit[y][x] = True

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if not visit[ny][nx] and tomato[ny][nx] == 0:
                visit[ny][nx] = True
                tomato[ny][nx] = tomato[y][x] + 1
                queue.append((ny, nx))

def findTomato(tomato):
    tomatos = []
    for r in range(n):
        for c in range(m):
            if tomato[r][c] == 1:
                tomatos.append((r, c))
    return tomatos


m, n = map(int, input().split())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 토마토 정보 구성
tomato = []
visit = [[False] * m for _ in range(n)]
for _ in range(n):
    tomato.append(list(map(int, input().split())))

bfs(findTomato(tomato))

if any(0 in row for row in tomato):             # row에 0이 하나라도 있으면 True
    print(-1)
else:
    print(max(max(row) for row in tomato)-1)