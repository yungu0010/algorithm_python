# 5430 - AC

from collections import deque
from curses.ascii import isdigit
import sys
input = sys.stdin.readline

TC = int(input().rstrip())
queue = deque()

for _ in range(TC):
    command = list(map(str, input().rstrip()))
    numCount = int(input().rstrip())
    numArray = list(input()[1:-2].split(","))

    queue.clear()
    reverseCount = 0
    noError = 1                 # error 발생 시 큐 출력하지 않도록

    for i in numArray:
        if i.isdigit():         # 숫자인 경우에만 append
            queue.append(i)

    for j in command:
        if j == 'R':
            reverseCount += 1   # reverse 횟수
        elif j == 'D':
            if len(queue) == 0:
                print('error')
                noError = 0
                break
            else:
                if reverseCount % 2 == 0:       #reverse가 짝수면 원래 자기 자신
                    queue.popleft()
                else:
                    queue.pop()
    
    if reverseCount % 2 != 0:                   # reverse가 홀수면 뒤집기
        queue.reverse()
    if noError:
            print("[" + ",".join(number for number in queue) + "]")
