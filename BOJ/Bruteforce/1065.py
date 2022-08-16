# 1065 - 한수

import sys
input = sys.stdin.readline

N = int(input())
digit = []
count = 0

# 각 자리수의 숫자 구하기
def getDigit(number):
    return [int(i) for i in str(number)] 

# 한수 확인
def checkSequence(i):
    global digit
    digit = getDigit(i)
    if len(digit) <=  2:
        return True
    else:
        temp = digit[0] - digit[1]
        
        for i in range(1, len(digit)-1):
            differ = digit[i] - digit[i+1]
            if temp != differ:
                return False
            
        return True

for i in range(1, N+1):
    hansu = checkSequence(i)
    if hansu:
        count += 1

print(count)