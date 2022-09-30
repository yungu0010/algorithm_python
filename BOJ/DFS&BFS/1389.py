# 1389 - 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
input = sys.stdin.readline

# N: 유저 수, M: 친구 관계 수
N, M = map(int, input().rstrip().split())
friendly = [[] for i in range(N+1)]
result = []


# # 관계 그래프
for _ in range(M):
    user1, user2 = map(int, input().rstrip().split())
    friendly[user1].append(user2)
    friendly[user2].append(user1)

# bfs
def bfs(graph, node):
    cavin = [0 for i in range(N+1)]             # 방문까지 거쳐야하는 노드 수 저장
    visit = [False * i for i in range(N+1)]     # 방문 정보 초기화
    queue = deque([node])
    visit[node] = True

    while queue:
        pair = queue.popleft()
        for i in graph[pair]:
            if not visit[i]:
                cavin[i] = cavin[pair] + 1      # 지난 노드 방문 횟수 + 1   ex) pair가 1일 때 1과 연결된 2번 노드는 1까지 방문한 횟수 + 1이다.
                visit[i] = True
                queue.append(i)

    return sum(cavin)

for i in range(N):
    result.append(bfs(friendly, i))

print(result.index(min(result[1::])))           # 인덱스를 편하게 보기 위해 1을 1번 인덱스에 저장. 0번째 인덱스 값이 0이 되므로 0번째 인덱스 제외
