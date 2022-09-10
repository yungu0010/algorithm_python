# 1920 - 수 찾기

import sys
from tabnanny import check
input = sys.stdin.readline

N = int(input().rstrip())
inputList = list(map(int, input().split()))
inputList.sort()

M = int(input().rstrip())
checkList = list(map(int, input().split()))

# 이분탐색
def binarySearch(start, end, data, target):
    if start > end:
        return False
    mid = (start+end)//2

    if data[mid] == target:
        return True
    elif target > data[mid]:
        start = mid + 1
    else:
        end = mid - 1
    
    return binarySearch(start, end, data, target)

for i in checkList:
    if binarySearch(0, len(inputList)-1, inputList, i):
        print(1)
    else:
        print(0)