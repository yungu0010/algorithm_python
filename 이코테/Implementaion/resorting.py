# 문자열 재정렬
# 알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어짐
# 모든 알파벳을 오름차순으로 정렬하여 출력한 뒤, 모든 숫자를 더한 값을 출력
# K1KA5CB7 -> ABCKK13


#isdecimal(), isdigit(), isnumeric() : 주어진 문자열이 숫자로 되어있는지 검사하는 함수
#isdecimal() : int형으로 변환 가능한지로 판단
#isdigit() : '숫자'모양으로 생겼으면 True 반환
#isnumeric() : 숫자값 표현에 해당하는 문자열까지 인정 ex) 거듭제곱, 분수 등의 특수문자 포함
string = input()
sum = 0
result = []
for i in string :        
    if i.isdigit() :            # 숫자형태인 경우
        sum += int(i)           # 값 더함
    else :
        result.append(i)

result.sort()                   #알파벳 순서대로 정렬

if sum != 0 :
    result.append(str(sum))
    
print(''.join(result))      #(구분자).join(list) : 매개변수로 들어온 리스트에 있는 요소를 합쳐서 하나의 문자열로 변환해 반환

    
