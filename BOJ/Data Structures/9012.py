# 9012 - 괄호

import sys
input = sys.stdin.readline

t = int(input().rstrip())
bracket = []
stack = []

for i in range(t) :
    bracket = list(input().rstrip())            #케이스 입력
    for i in bracket :
        if i == '(' :                           #(인 경우 push
            stack.append(i)
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :       #)이면서 빈 스택이 아니라면 pop
                stack.pop()
            else :                              #빈 스택이라면 ) push
                stack.append(")")
                break
    if len(stack) == 0 :                        #스택이 비었다면 YES
        print('YES')
    else :
        print('NO')                             #스택에 뭔가 남아있다면 NO
    bracket = []
    stack = []