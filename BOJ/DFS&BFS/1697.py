# 1697 - 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
visit = [False for i in range(100000 + 1)]              # 방문 정보 저장
depth = [0 for i in range(100000 + 1)]                  # 도착까지 걸리는 횟수 저장

def findBro(node):
    global K, count, depth

    queue = deque()
    queue.append(node)
    visit[node] = True


    while queue:
        checkNumber = queue.popleft()
        for i in [checkNumber-1, checkNumber+1, checkNumber*2]:     # N에서 할 수 있는 동작
            if 0 <= i <= 100000:                                    # K 범위에 의해 음수값과 100000 초과 필요없음
                if depth[i]:                                        # 이미 더 짧은 경로로 방문 했다는 뜻
                    continue
                if i == K:                                          # 정답이라면 가장 최근한 방문한 노드까지 가는 횟수 + 1
                    return depth[checkNumber] + 1
                elif depth[i] == 0:                                 # 한 번도 방문하지 않는 노드라면 queue에 넣고, 값 +1
                    queue.append(i)
                    depth[i] = depth[checkNumber] + 1

if N == K:          # 애초에 같은 값이라면 0출력
    print(0)
else:
    print(findBro(N))