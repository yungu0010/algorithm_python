# 1018 - 체스판 다시 칠하기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
fixW = 0        # (0,0)이 'W'일 때 다시 칠해야하는 칸의 수
fixB = 0        # (0,0)이 'W'일 때 다시 칠해야하는 칸의 수
fix = []


for m in range(N):
    chess.append(input().rstrip())

for i in range(N - 7):
    for j in range(M - 7):
        fixW = 0
        fixB = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                # (0,0)이 'W'인 경우
                if (k+l)%2 == 0 and chess[k][l] == 'B' or (k+l)%2 !=0 and chess[k][l] == 'W':       # 연산자 우선순위 and > or
                    fixW += 1
                
                if (k+l)%2 == 0 and chess[k][l] == 'W' or (k+l)%2 !=0 and chess[k][l] == 'B':
                    fixB += 1
        if fixB > fixW:
            fix.append(fixW)
        else:
            fix.append(fixB)

print(min(fix))
