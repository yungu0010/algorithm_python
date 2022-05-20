# 10773 - 제로

import sys
input = sys.stdin.readline

k = int(input().rstrip())       #입력받을 수의 개수
stack = []                      #입력받은 수를 저장할 스택
result = 0                      #합계 계산

for i in range(k) :
    num = int(input().rstrip())
    if num == 0 :               #0이라 잘못 부르면 pop
        stack.pop()
    else :
        stack.append(num)
        
for i in stack :                #합계 계산 후 출력
    result += int(i)
print(result)

