# 9093 - 단어 뒤집기

from audioop import reverse
import sys
input = sys.stdin.readline

TC = int(input())
strList = []

for _ in range(TC):
    strList.clear()
    strList = list(map(str, input().split()))
    for i in strList:
        print(i[::-1], end=" ")         # strList의 원소를 역순으로 출력