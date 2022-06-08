# 미로 탈출

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())       # N: 세로, M: 가로
graph = []
queue = deque()

# 미로 입력
for i in range(N):
    graph. append(list(map(int, input().rstrip())))

# 상하좌우 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


# bfs 함수
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상, 하, 좌, 우의 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽을 만나면 그냥 넘어가기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 괴물 만나도 그냥 넘어가기
            if graph[nx][ny] == 0:
                continue

            # 길을 만나면
            if graph[nx][ny] == 1:                  # 한 번도 방문하지 않은 길만 1의 값을 가짐
                graph[nx][ny] = graph[x][y] + 1     # 이전 노드 값에 1을 더한 값으로 바꿔줌
                queue.append((nx, ny))              # 방문한 노드를 큐에 넣어줌
            
    return graph[N - 1][M - 1]                      # 미로의 탈출구의 값을 리턴



print(bfs(0, 0))
