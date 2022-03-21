# 1874 - 스택수열

# 문제 설명
# 스택에 수를 push할 때는 반드시 오름차순으로만 push 가능
# ex.8을 push 하려면 1~7까지 모두 push 하고 8을 push 할 수 있다.
# 참고 https://hongcoding.tistory.com/39

from sys import stdin

input = stdin.readline

n = int(input().rstrip())
stack, result = [], []              # 수를 저장하는 스택, +/-를 저장하는 스택

tmp = 1

for i in range(n) :
    num = int(input().rstrip())
    
    while tmp <= num :              # 처음에는 stack이 비어있기 때문에 stack[-1]은 사용할 수 없음
        stack.append(tmp)
        result.append('+')
        tmp += 1
        
    if stack[-1] == num :           # 스택의 마지막 원소가 현재 입력값과 같은 경우
        stack.pop()                 # pop 해주고 '-' 저장
        result.append('-')
    else :                          # 스택의 마지막 수와 현재와 같지 않고 tmp 보다 큰 경우 수열을 만들 수 없음
        print('NO')
        exit()                      # 프로그램 종료

for i in result :
    print(i)