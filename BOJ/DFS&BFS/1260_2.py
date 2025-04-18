from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

# 간선 정보 저장
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# 정점 번호가 작은 것을 먼저 방문
for g in graph:
    g.sort()

# dfs
def dfs(start, visited):
    visited[start] = True
    result = [str(start)]
    for i in graph[start]:
        if not visited[i]:
            result += dfs(i, visited)
    return result

print(' '.join(dfs(v, visited)))

# bfs
visited = [False] * (n+1)
def bfs(start):
    answer = []
    queue = deque()
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        now = queue.popleft()
        answer.append(now)

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return answer

print(' '.join(map(str, bfs(v))))