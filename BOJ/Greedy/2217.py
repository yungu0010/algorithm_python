# 2217 - 로프

import sys
input = sys.stdin.readline

n = int(input())
ropes = []                  # 로프 정보를 저장할 배열
result = []                 # 최대 중량을 구할 때 사용할 배열

for _ in range(n):
    ropes.append(int(input()))

# 내림차순 정렬
ropes.sort(reverse= True)

for i in range(n):
    # i+1은 검사한 로프의 개수(현재 검사 중인 로프 포함)
    # 내림 차순으로 정렬했기 때문에 이전에 검사한 로프는 현재 검사 중인 로프보다 더 큰 중량을 가지는 로프이다. -> 현재 검사하는 로프가 들 수 있는 중량 * 지금까지 검사한 로프의 수
    # 이전 로프까지 검사 했을 때 들어올릴 수 있는 최대 중량과 현재 검사중인 로프를 포함했을 때 가능한 최대 중량을 비교해서 result를 갱신한다. 
    result.append((i + 1) * ropes[i])

print(max(result))