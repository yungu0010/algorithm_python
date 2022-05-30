# 음료수 얼려먹기
# 첫 번째 줄에 얼음틀의 세로(n), 가로(m) 길이 주어짐
# 두 번째 줄부터 n + 1까지 줄까지 얼음틀 정보 주어짐
# 구멍이 뚤린 부분은 0, 막힌 부분은 1

import sys
input = sys.stdin.readline

# 특정 노드를 방문하고 연결된 다른 노드들도 방문
def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:        # 주어진 범위를 벗어나는 경우 종료
        return False
    if graph[x][y] == 0:                        # 아직 현재 노드를 방문하지 않았다면
        graph[x][y] = 1                         # 현재 노드 방문 처리
        # 인접 노드 방문
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 얼음틀 정보 입력 받기
n, m = map(int, input().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:                  # 현재 위치에서 DFS 수행
            result += 1                        # 방문처리가 됐다면 count

print(result)

