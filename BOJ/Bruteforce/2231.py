# 2231 - 분해합

import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 0              # 생성자가 없을 때는 0을 출력

for i in range(1, N + 1):
    temp = i + sum(map(int, str(i)))
    if temp == N:
        result = i
        break
print(result)