# 2869 - 달팽이는 올라가고 싶다

import sys
input = sys.stdin.readline

A, B, V = map(int,input().split())

day = (V - A) // (A - B)
if (V - A) % (A - B) == 0:
    print((V - A) // (A - B) + 1)       # V - A한 상태의 거리를 계산한 것이므로 A만큼 더 이동해야 함 -> 하루 더 추가   
else:
    print((V - A) // (A - B) + 2)       # 몫이 소수로 나오지만 소수로 나와도 하루를 이동한 것과 마찬가지기 때문