# 1541 - 잃어버린 괄호

import sys
input = sys.stdin.readline

exp = list(input().rstrip().split('-'))
result = 0

for i in range(len(exp)):
    plus = 0
    plusString = list(map(int, exp[i].split('+')))      # -를 기준으로 나눈 수식 계산
    for j in plusString:
        plus += j
    if i == 0:                                          # 첫 번째 수는 -가 오지 않기 때문
        result = plus
    else:
        result -= plus
print(result)