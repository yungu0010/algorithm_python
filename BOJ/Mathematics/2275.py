# 2275 - 부녀회장이 될테야

from curses import REPORT_MOUSE_POSITION
import sys
input = sys.stdin.readline

def resident(k, n):
    global human
    floor = k
    room = n

    if floor == 0 or room == 1:
        human += room
        return human

    resident(floor, room - 1) + resident(floor - 1, room)
    return human

testCase = int(input().rstrip())
human = 0

for _ in range(testCase):
    human = 0
    k = int(input().rstrip())
    n = int(input().rstrip())
    print(resident(k, n))