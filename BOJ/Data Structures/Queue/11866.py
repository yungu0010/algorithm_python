# 11866 - 요세푸스 문제0
# 원형큐를 사용하는 문제같다

import sys
from collections import deque

input = sys.stdin.readline
queue = deque()                 # 값을 저장할 큐
index = 0                       # pop할 index
result = []                     # 출력 결과를 저장할 리스트

n, k = map(int,input().split()) # n명의 사람이 원을 이루면서 앉아있고, k번째 사람을 제거

for i in range(n) :
    queue.append(i+1)           # 큐 생성
    
while len(queue) != 0 :         # 큐가 빌 때까지 반복
    index += k-1                # ex. k=3일 때 index로는 2번째 사람 제거. 그 다음 제거 대상은 5이지만, 2가 제거 되었기 때문에 k-1만큼 index 증가
    if index > len(queue) - 1 : # index 범위 초과시 처리
        index = index % len(queue)
        
    result.append(queue[index]) # 출력 리스트에 입력
    queue.remove(queue[index])  # 실제 데이터 제거

# 요구하는 형식대로 출력
print("<", end="")
for i in range(len(result)-1) :
    print("%d, " %result[i], end="")
print(result[-1], end="")
print(">")