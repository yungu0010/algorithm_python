# 4949 - 균형잡힌 세상

# (), [] 괄호는 두 종류

# 대괄호, 소괄호 스택을 같이 사용하는 경우 pop이 실행될 때 괄호의 짝이 맞는지 확인해야함.
# 한 줄 또는 여러줄이 입력된다는 것에 유의

import sys
input = sys.stdin.readline


while True :                    # .이 입력될 때까지 실행
    string = input().rstrip()
    if string == '.' :          # 종료조건인 .이 입력되는 경우 while문 빠져나옴
        break
    stack = []
    
    for i in string :           # 문자열 차례로 검사
        if i == '.':
            break
        elif i == '(' :
            stack.append(i)
        elif i == '[' :
            stack.append(i)
        elif i == ')' :
            if len(stack) > 0 and stack[-1] == '(':     # 스택이 비어있지 않고 마지막 원소가 짝을 이루는 경우
                stack.pop()
            else :
                stack.append(i)                         # 짝을 이루지 않는 경우
                break
        elif i == ']' :
            if len(stack) > 0 and stack[-1] == '[' :
                stack.pop()
            else :
                stack.append(i)
                break
    if len(stack) == 0 :                                # 현재 문자열 입력에 대한 결과 출력
        print("yes")
    else :
        print("no")