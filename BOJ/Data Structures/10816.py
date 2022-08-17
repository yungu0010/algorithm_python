# 10816 - 숫자카드2

import sys
input = sys.stdin.readline

N = int(input().rstrip())
NList = list(map(int,input().split()))

M = int(input().rstrip())
MList = list(map(int,input().split()))

NHash = {}

for n in NList:
    if n not in NHash:
        NHash[n] = 1
    else:
        NHash[n] += 1

print(NHash)

print(' '.join(str(NHash[m]) if m in NHash else '0' for m in MList))

# for m in MList:
#     if m in NHash:
#         print(' '.join(str(NHash[m])))
#     else:
#         print(' '.join('0'))