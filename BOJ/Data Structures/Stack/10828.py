# 10828 - 스택


import sys
input = sys.stdin.readline
n = int(input().rstrip())
command = []
stack = []


for i in range(n) :
    com = list(input().rstrip().split())
    command.append(com)

for i in range(n) :
    if command[i][0] == 'push' :            # push X: 정수 X를 스택에 넣는 연산이다.
        stack.append(command[i][1]) 
    elif command[i][0] == 'pop' :           # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())
    elif command[i][0] == 'size' :          # size: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))
    elif command[i][0] == 'empty' :         # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif command[i][0] == 'top' :           # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])                #pop하지 않고 출력만 할 때는 [-1] 사용