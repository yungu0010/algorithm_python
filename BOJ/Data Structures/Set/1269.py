# 대칭 차집합

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

setA = set(map(int, input().split(' ')))        # 집합 A
setB = set(map(int, input().split(' ')))        # 집합 B

result = setA ^ setB                            # 대칭 차집합
print(len(result))