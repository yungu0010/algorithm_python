import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] + list(range(1, n+1))

# x의 부모 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# x의 부모를 y로 변경
def remove(x, y):
    parent[find(x)] = find(y)

for _ in range(m):
    type, a, b = map(int, input().split())

    if type == 0:
        remove(a, b)
    else:
        if find(a) == find(b):
            print("yes")
        else:
            print("no")