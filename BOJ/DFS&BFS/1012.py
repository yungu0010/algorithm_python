# 1012 - 유기농 배추

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

TC = int(input())
cabbageMap = []

def dfs(y, x):
    if x < 0 or x >= row or y < 0 or y >= col:        # 주어진 범위를 벗어나는 경우 종료
        return False
    if cabbageMap[y][x] == 1:                        # 배추가 심겨있다면
        cabbageMap[y][x] = 0                         # 현재 노드 방문 처리
        # 인접 노드 방문
        dfs(y - 1, x)
        dfs(y, x - 1)
        dfs(y + 1, x)
        dfs(y, x + 1)
        return True
    return False

for _ in range(TC):
    cabbageMap.clear()                              # 지도 초기화
    row, col, cabbage = map(int, input().split())
    
    # 지도 생성
    for _ in range(col):
        cabbageMap.append([0] * row)
    
    # 지도 초기화
    for _ in range(cabbage):
        x, y = map(int, input().split())
        cabbageMap[y][x] = 1

    larva = 0
    for y in range(col):
        for x in range(row):
            if dfs(y, x) == True:
                larva += 1
    print(larva)