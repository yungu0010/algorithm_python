# 1468 - 영화감독 숌

import sys
input = sys.stdin.readline

N = int(input().rstrip())
endNum = []
testNum = '666'
while True:
    if len(endNum) >= N:
        break
    if '666' in testNum:
        endNum.append(testNum)
    testNum = str(int(testNum) + 1)     # 숫자로 변환해서 계산 후 문자열로 다시 변환

print(endNum[N-1])