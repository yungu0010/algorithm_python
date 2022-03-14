# 문자열 반복

n = int(input())        #문자열 반복
case = []

for i in range(n) :
    info = list(input())        #입력받은 값 리스트로 저장
    case.append(info)           #case에 넣음

for i in range(len(case)) :     #입력받은 케이스만큼 반복
    for j in range(len(case[i]) - 1) :  #첫번째 케이스 입력 문자열 - 1 만큼 반복, print에서 j + 1하기 때문
        if case[i][j+1] == ' ':     #공백이면 프린트하지 않음
            continue
        else :
            print(int(case[i][0]) * case[i][j + 1], end='')     #입력횟수 * 입력문자, 줄바꿈 방지 위한 end j + 1은 첫번째 입력 횟수 반복 방지
    print('')                   #print는 자동 줄바꿈이기 때문에 \n 사용하지 않아도 됨