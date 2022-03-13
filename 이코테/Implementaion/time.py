# 시각 - 완전 탐색
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 경우의 수 구하기
# 시간 제한 2초

n = int(input())
count = 0

for h in range(0, n+1) :
    for m in range(0, 60) :
        for s in range(0, 60) :
            sentence = str(h) + str(m) + str(s)
            if '3' in sentence :                #x (not) in 리스트, 튜플, 문자열 -> T/F반환
                count += 1
print(count)