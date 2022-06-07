# # 단지번호 붙이기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input().rstrip())       # 지도 크기 입력

graph = []                      # 지도 정보를 저장할 배열
count = 0                       # 단지 수
house = 0                       # 단지 내 집 수
houseList = []                  # 단지 내 집 수를 정렬할 배열

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(y, x):          # y가 세로, x가 가로
    global house

    if y < 0 or y >= n or x < 0 or x >= n:          # 범위를 벗어나면 False 반환
        return False

    if graph[y][x] == 1:                            # 집이 있는 경우
        house += 1
        graph[y][x] = 0                            # 0으로 바꾸어서 방문했다는 표시 해줌
        for i in range(4):                          # 상하좌우 살펴봄
           dfs(y + dy[i], x + dx[i])
        return True
    return False


# 지도 정보 입력
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range(n):                  # i, y 역할로 세로 의미
    for j in range(n):              # j, x 역할로 가로 의미
        if dfs(i, j) == True:
            houseList.append(house) # 단지 내 집 개수 추가
            count += 1              # 단지 개수 추가
            house = 0               # 단지 내 집 개수 초기화

# 집 개수대로 정렬
houseList.sort()

print(count)

for i in range(len(houseList)):
    print(houseList[i])