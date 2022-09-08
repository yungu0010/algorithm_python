# 18870 - 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
coordinate = list(map(int, input().split()))            # print -> [2, 4, -10, 4, -9]

sortInput = sorted(list(set(coordinate)))               # print -> [-10, -9, 2, 4]
dict = {sortInput[i] : i for i in range(len(sortInput))}    # print -> {-10: 0, -9: 1, 2: 2, 4: 3} 입력값: 축소값

for i in coordinate:
    print(dict[i], end = " ")               # 입력값에 대한 축소값 출력