# 18742 - 구현

import sys
input = sys.stdin.readline

# n = 찾아볼 시간 간격, k = 찾을 숫자
n, k = map(int,input().split())
count = 0
timeString = ""

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            timeString = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            # .find는 문자가 존재한다면 index 반환, 존재하지 않는다면 -1 반환
            if timeString.find(str(k)) != -1:
                count += 1
print(count)
