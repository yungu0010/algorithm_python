# 11478 - 서로 다른 부분 문자열의 개수

import sys
input = sys.stdin.readline

string = input()
stringSet = set()

for i in range(len(string)):
    for j in range(1, len(string)-i):
        stringSet.add(string[i:i+j])

print(len(stringSet))