# 1541 - 잃어버린 괄호

import sys
input = sys.stdin.readline

exp = list(input().rstrip().split('-'))
result = 0

for i in range(len(exp)):
    plus = 0
    plusString = list(map(int, exp[i].split('+')))
    for j in plusString:
        plus += j
    if i == 0:
        result = plus
    else:
        result -= plus
print(result)