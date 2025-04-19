# 6603 - 로또

from itertools import *
from collections import *
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

while True:
    TC = list(map(int, input().split()))

    if TC[0] == 0:
        break

    S = TC[1:]
    answer = list(map(list, combinations(S, 6)))
    answer.sort()
    for a in answer:
        print(*a)           # 언패킹(각 요소를 sep=' '한 결과를 보여줌)
    print()