# 1976 - 여행 가자

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())        # 도시의 수
m = int(input())        # 여행 계획에 속한 도시 수

parent = list(range(0, n))

# x의 최상위 부모 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# x의 소속을 y로
def remove(x, y):
    parent[find(x)] = parent[find(y)]

for i in range(n):
    graph = list(map(int, input().split()))
    for j, g in enumerate(graph):
        if i == j:
            continue
        if g == 1:              # 연결되어있다면
            remove(i, j)        # i를 j의 집합으로 넣어줌

travel = list(map(lambda x: int(x)-1, input().split()))    # 여행 경로

# group에 모든 경로의 최상위 부모를 저장
group = set()
for t in travel:
    group.add(find(t))

# set의 크기가 1이면 모두 같은 부모를 가지고 있음
if len(group) == 1:
    print("YES")
else:
    print("NO")
