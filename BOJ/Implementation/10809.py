# 10809 - 알파벳 찾기

s = input()
alpha = list(range(97, 123))        #아스키코드 숫자 범위

for x in alpha :
    print(s.find(chr(x)), end=' ')           #find 함수는 문자가 없으면 -1을 출력, 있으면 index를 출력한다
                                    #chr(x)는 아스키 코드를 문자로 변환, 그 문자가 s안에 있는지 find로 판별