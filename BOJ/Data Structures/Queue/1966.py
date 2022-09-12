# 1966 - 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

TC = int(input())
queue = deque()         # 문서의 우선순위 저장
index = deque()         # 프린트할 문서의 인덱스 저장

for _ in range(TC):
    queue.clear()       # 초기화
    index.clear()
    count = 0
    N, M = map(int, input().rstrip().split())       # N: 문서의 개수, M: 언제 출력되는지 궁금한 문서

    priorityList = list(map(int, input().rstrip().split()))
    for i in priorityList:
        queue.append(i)
        index.append(0)

    target = queue[M]
    index[M] = 1        # 프린트 순서를 알고싶은 문서만 값을 1로 변경

    while True:
        if queue[0] < max(queue):           # 우선순위가 최대가 아니면 뒤의 순번으로
            queue.append(queue.popleft())
            index.append(index.popleft())
        else:                               # 우선순위가 최대인 경우
            count += 1
            queue.popleft()
            if index.popleft() == 1:        # 찾는 문서인 경우
                print(count)
                break
            else:                           # 찾는 문서가 아닌 경우
                continue        