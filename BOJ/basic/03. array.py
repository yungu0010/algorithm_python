# 2562 - 최댓값
num = []
index = 0
mx = 0
for i in range(0, 9) :
    a = int(input())
    num.append(a)
    if mx < a :
        mx = a
        index = i+1
print(mx)
print(index)


# 3052 - 나머지
remain = []         #나머지 저장할 리스트
count = 1           #나머지가 모두 같으면 다른 수가 하나이니까
for i in range(10) :
    n = int(input())
    remain.append(n % 42)
    
remain.sort()       #오름차순 정렬
for i in range(len(remain)-1) :
    if remain[i] != remain[i+1] :       #지금 수와 다음 인덱스 수 비교
        count += 1                      #다르면 결과값 +1
    
print(count)


#1526 - 평균
n = int(input())    #과목수
score = list(map(int,(input().split())))        #입력받은 숫자를 리스트로 저장
result = 0          #평균 구할 때 총점

m = max(score)      #과목의 최댓값
for i in range(n) :
    score[i] = score[i]/m*100
    result += score[i]
print(result/n)


# 8958 - OX 퀴즈
test = []               #입력받은 케이스 저장
n = int(input())        #입력할 케이스
score = 0               #케이스마다의 총점
point = 1               #가산점
case_s = []             #케이스 총점을 저장하는 리스트

for i in range(n) :
    case = list(input())
    test.append(case)
    
for i in range(n) :
    for j in range(len(test[i])) :
        if test[i][j] == 'O' :      #O이면
            score += point          #포인트만큼 더함
            point += 1              #O가 다음에 중복으로 나오면 가산점
        else :
            point = 1
    case_s.append(score)            #해당 케이스의 총점 저장
    score = 0                       #초기화
    point = 1
for i in range(n) :                 #출력
    print(case_s[i])
    

# 4344 - 평균은 넘겠지
c = int(input())        #테스트 케이스의 개수 c
score = 0               #평균 계산을 위한 총점
count = 0               #평균을 넘는 학생 수

for i in range(c) :
    test = list(map(int, input().split()))
    for j in test[1 :] :    #점수부터 순회
        score += j          #총점 계산
    avg = score / test[0]   #평균
    for j in test[1 : ] :
        if j > avg :        #평균을 넘는 학생 수 세기
            count += 1
    try :
        print("{:.3f}%".format(float(count/test[0] * 100)))     #{:.3f} 소수 셋째자리까지 출력, test[0]==0인 경우 try-except예외 처리
    except ZeroDivisionError :
        print("ZeroDivisionError")
    count, avg, score = 0, 0, 0