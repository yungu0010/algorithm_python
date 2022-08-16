# 5622 - 다이얼

import sys
input = sys.stdin.readline

dial = input().rstrip()
count = 0

for i in dial:
    num = ord(i)
    if num < 68:
        count += 3
    elif num < 71:
        count += 4
    elif num < 74:
        count += 5
    elif num < 77:
        count += 6
    elif num < 80:
        count += 7
    elif num < 84:
        count += 8
    elif num < 87:
        count += 9
    else:
        count+= 10

print(count)