# 10815 - 숫자카드

import sys
from unittest import result
input = sys.stdin.readline

N = int(input())
NList = list(map(int, input().split()))

M = int(input())
MList = list(map(int, input().split()))

NList.sort()
result = []

def binarySearch(target, data, start, end):
    if start > end:
        return False

    mid = (start + end) // 2

    if target == data[mid]:
        return True
    elif target > data[mid]:
        start = mid + 1
    else:
        end = mid - 1
    
    return binarySearch(target, data, start, end)
        

for m in MList:
    if binarySearch(m, NList, 0, len(NList) -1):
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end = " ")