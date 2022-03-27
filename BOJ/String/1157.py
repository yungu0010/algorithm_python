# 1157 - 단어 공부
# 알파벳 대소문자가 주어지면, 이 단어에서 가장 많이 사용된 알파벳 단어 찾기
# 단, 대소문자를 구별하지 않음

import sys

input = sys.stdin.readline().rstrip()   
# 습관화 하자! 시간 제한 문제에서는 반복문 입력 시 문제 생길 수 있음
# 마지막에 개행문자(줄 바꿈 문자)를 포함하고 있어 공백 삭제 함수 함께 사용
# rstrip() : 오른쪽 공백 삭제
# lstrip() : 왼쪽 공백 삭제
# strip() : 왼쪽 오른쪽 공백 삭제

string = input
ascii = []                       # A : 65, a : 97
same_time = False
mx = 0                         # 임시 값 저장
char = ' '

for i in string :
    if ord(i) >= 97 :
        ascii.append(ord(i) - 32)
    else :
        ascii.append(ord(i))
ascii = sorted(ascii)

for i in ascii :
    if i == ord(char) :
        continue
    count = ascii.count(i)
    if mx < count :
        mx = count
        char = chr(i) 
    elif mx == count :
        same_time = True
        
if same_time :
    print("?")
else :
    print(char)
    
    