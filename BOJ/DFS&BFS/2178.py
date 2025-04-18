# 2178 - 미로탐색
# 이동하는 최소의 칸 수를 구하는 프로그램 작성

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]      # 미로 정보 저장

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위를 벗어나면 종료
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue

            if maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1       # 한 번도 방문하지 않은 경우 방문 처리
                queue.append((ny, nx))

bfs(0, 0)
print(maze[n-1][m-1])