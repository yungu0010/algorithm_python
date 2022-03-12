# 상하좌우 문제 조건
# 첫째 줄에 공간의 크기를 나타내는 N이 주어짐
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어짐
# 3 4 와 같이 도착 지점의 좌표 출력

# 시작좌표 (1,1), LRUD에 따라 한 칸씩 이동, 범위를 벗어나는 움직임 무시

n = int(input())    #공간의 크기
plan = list(input().split())        #리스트로 문자열 저장

x, y = 1, 1         # 시작 좌표
nx, ny = 1, 1       # 다음 좌표

def move(s, x, y) :
    global nx, ny           #외부 변수 함수 내에서 이용 -> UnboundLocalError: local variable 'nx' referenced before assignment 유발
    if s == 'L' :
        nx = x - 1
    elif s == 'R':
        nx = x + 1
    elif s == 'U':
        ny = y - 1
    elif s == 'D':
        ny = y + 1
    if nx < 1 or ny < 1 or nx > n or ny > n :       #범위를 초과하는 경우, 계획 불이행
        nx = x
        ny = y
    
    # print("move 함수 안", nx, ny)
    return(nx, ny)

for i in range(len(plan)):      #입력한 계획만큼 반복(리스트 크기만큼)
    x, y = move(plan[i], x, y)  #계획과 현재 좌표를 인수로 가짐
    # print("for문 안",x, y)
    
print(x, y)