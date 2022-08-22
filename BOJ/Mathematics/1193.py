# 1193 - 분수 찾기

import sys
input = sys.stdin.readline

X = int(input())

# line: 줄 수, numberCount: 숫자 인덱스
numberCount = 0
line = 0

while numberCount < X:
    line += 1
    numberCount += line

# ex) X = 14일 때 numberCount = 10
numberCount -= line

if line % 2 == 0:
    i = X - numberCount
    j = line - (X - numberCount) + 1
else:
    i = line - (X - numberCount) + 1
    j = X - numberCount

print('%d/%d' % (i, j))
