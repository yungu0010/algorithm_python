# 2164 - 카드 2

from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
N = int(input().rstrip())
number = 0

for i in range(N):
    queue.append(i+1)

while len(queue) > 0:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    number = queue.popleft()
    queue.append(number)
