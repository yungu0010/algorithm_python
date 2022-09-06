# 10814 - 나이순 정렬

import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    age, name = list(map(str, input().split()))
    info.append([int(age), name])               # age 타입 int로 변경

info.sort(key=lambda x : x[0])                  # 배열의 첫번째 원소를 기준으로 정렬

for i in range(len(info)):
    print(info[i][0], info[i][1])