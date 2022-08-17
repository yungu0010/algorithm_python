# 2292 - 벌집

import sys
input = sys.stdin.readline

N = int(input().rstrip())
floor = 1
room = 1

while N >= 0:
    if N == 1:              # 방이 하나 남으면 그대로 출력(floor의 기본값이 1이기 때문에 방이 하나 남아도 room을 추가해줄 필요가 없다.)
        print(room)
        break
    N = N - (6 * floor)     # 전체 방 중 한 층만큼 빼기
    room += 1
    floor += 1
    if N <= 0:
        print(room)
        break