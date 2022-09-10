# 10845 - 큐

# push, pop, size, empty, front, back의 6가지 명령 수행
# python의 deque 라이브러리 사용 - 리스트로 구현 가능하지만 시간복잡도를 위해 deque 사용

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())       # 받을 명령의 수
list = []                       # 명령어를 저장할 리스트
queue = deque()                 # 명령어의 결과를 저장하는 큐

for i in range(n) :
    list.append(input().split())
# print(list)
# [['push', '1'], ['push', '2'], ['front'], ['back'], ['size'], ['empty'], ['pop'], ['pop'], ['pop'], ['size'], ['empty'], ['pop'], ['push', '3'], ['empty'], ['front']]

for i in range(len(list)) :
    command = list[i][0]            # 입력한 명령어
    if command == 'push' :          # push인 경우 queue에 값을 넣음
        queue.append(list[i][1])
    elif command == 'pop' :         # 큐에서 가장 앞에 있는 정수 빼고 출력
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue.popleft())
    elif command == 'size' :        # 큐에 들어있는 정수 개수 출력
        print(len(queue))
    elif command == 'empty' :       # 큐가 비어있으면 1, 아니면 0출력
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif command == 'front' :       # 큐의 가장 앞에있는 정수 출력
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])     
    elif command == 'back' :        # 큐의 가장 마지막 원소 출력
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])
