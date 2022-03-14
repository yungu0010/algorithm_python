# 11720 - 숫자의 합

n = int(input())
num = input()
score = 0
for i in range(n) :
    score += int(num[i])        #문자열을 차례로 숫자로 변환해서 더함
print(score)