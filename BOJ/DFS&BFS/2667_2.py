# 2667 - 단지번호붙이기

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(y, x, visit):
    visit[y][x] = True
    count = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue

        if house[ny][nx] == 1 and not visit[ny][nx]:
            count += dfs(ny, nx, visit)
    return count

n = int(input())
visit = [[False] * n for _ in range(n)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 단지 정보 구성
house = []
for _ in range(n):
    data = list(map(int, input().strip()))
    house.append(data)

answer = []
for y in range(n):
    for x in range(n):
        if not visit[y][x] and house[y][x] == 1:
            answer.append(dfs(y, x, visit))
        
answer.sort()
print(len(answer))
for i in answer:
    print(i)