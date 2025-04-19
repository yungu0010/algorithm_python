# 2661 - 좋은수열

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
seq = []

def dfs():
    if len(seq) == n:
        print(''.join(seq))     # 최솟값 출력
        sys.exit(0)             # 즉시 종료

    for i in ['1', '2', '3']:
        seq.append(i)

        length = len(seq)       # 만든 수열의 길이
        good = True             # 좋은 수열 여부

        for k in range(1, length//2 + 1):       # 마지막 k개와 그 앞 k개가 같은지 검사
            if seq[-k:] == seq[-2*k:-k]:        # 두개가 같은 경우 -> 나쁜 수열
                good = False
                break

        if good:                # 나쁜 수열일 경우 백트레킹
            dfs()

        seq.pop()

dfs()