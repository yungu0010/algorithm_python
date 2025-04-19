from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
place = [0 for _ in range(100001)]     # i 위치까지 도달하는 데 걸리는 시간
visit = [False for _ in range(100001)] # 방문 여부

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = True

    while queue:
        now = queue.popleft()

        for i in [now * 2, now-1, now+1]:
            if i < 0 or i > 100000:
                continue
            if not visit[i]:
                place[i] = place[now] + 1
                visit[i] = True
                queue.append(i)

bfs(n)
print(place[k])