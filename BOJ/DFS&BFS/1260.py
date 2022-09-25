# 1260 - DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] * 1 for _ in range(N+1)]
visited = [False] * (N+1)

# 그래프 간선 정보 저장
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(len(graph)):
    graph[i].sort()

def dfs(graph, node, visited):
    visited[node] = True
    print(node, end= " ")

    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        # pop한 노드가 방문노드가 아니라면 인접노드 큐에 삽입
        for j in graph[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = (True)

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)