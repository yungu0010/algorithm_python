# 11724 - 연결 요소의 개수

from collections import *
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = True

    while queue:
        node = queue.popleft()

        for n in graph[node]:
            if not visit[n]:
                visit[n] = True
                queue.append(n)

n, m = map(int, input().split())

# 그래프 구성
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for i in range(1, n+1):
    if not visit[i]:
        bfs(i)
        answer += 1

print(answer)