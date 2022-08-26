# 10250 - ACM 호텔

import sys
input = sys.stdin.readline

def findRoom(H, N):
    if N % H != 0:
        Y = N % H
        X = N//H + 1
    else:           # 꼭대기 층일 때
        Y = H       
        X = N//H
    return X, Y

N = int(input().rstrip())

for _ in range(N):
    H, W, N = map(int, input().split())
    X, Y = findRoom(H,N)

    print("%d%02d" % (Y, X))