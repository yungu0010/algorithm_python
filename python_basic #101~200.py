#101 ~ 130 파이썬 분기문
#101
print("#101. \n주석 참조") #자동줄바꿈
# True 혹은 False를 갖는 데이터 타입 - bool 타입

#102
print("\n#102. ")
print(3 == 5) # false

#103
print("\n#103. ")
print( 3 < 5) #true

#104
print("\n#104. ")
x = 4
print(1 < x < 5) #true

#105
print("\n#105. ")
print((3 == 3) and (4 != 4)) #true and true -> true

#106
print("\n#106. 주석참조")
#print(3 => 4) =>기호가 틀렸음, >=로 적어야 함

#107
print("\n#107. 주석참조")
if 4 < 3:
    print("Hello World")
#아무것도 출력되지 않음

#108
print("\n#108. ")
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
#Hi, there. 출력

#109
print("\n#109. ")
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
#1 2 4

#110
print("\n#110. ")
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
#3 5

#111
print("\n#111. ")
a = input(">>")
print(a*2)

#112
print("\n#112. ")
num = int(input(">> 숫자를 입력하세요: "))
print(num + 10)

#113
print("\n#113. ")
evenodd = int(input(">> "))
if evenodd%2 == 0 :
    print("짝수")
else :
    print("홀수")

#114
print("\n#114. ")
b = int(input(">> 입력값: "))
if (b + 20) > 255 :
    print(255)
else :
    print(b + 20)

#115
print("\n#115. ")
c = int(input(">> 입력값: "))
if (c - 20) < 0 :
    print(0)
else :
    print(c - 20)

#116
print("\n#116. ")
time = input(">> 현재시간: ")
split = time.split(':')
if split[1] == "00" :
    print("정각 입니다.")
else :
    print("정각이 아닙니다.")

#117
print("\n#117. ")
fruit = ["사과", "포도", "홍시"]
answer = input(">> 좋아하는 과일은? ")
if answer in fruit :
    print("정답입니다.")

#118
print("\n#118. ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
answer = input(">> ")
if answer in warn_investment_list :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")

#119 ~ 120
print("\n#119 ~ 120. ")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input(">> 제가 좋아하는 계절은: ")
if season in fruit.keys() :
    print("정답입니다.")
else : 
    print("오답입니다.")

value = input(">> 좋아하는 과일은? ")
if value in fruit.values() :
    print("정답입니다.")
else :
    print("오답입니다.")

#121
str = input(">> 문자를 입력하세요 : ")
if str.islower() :   #islower()은 문자의 소문자 여부 판별, 소문자일 경우 True
    print(str.upper())
else :
    print(str.lower())

#122
score = int(input(">> score를 입력하세요 : "))
if score > 80 and score <= 100 :
    grade = "A"
elif score > 60 and score < 80 :
    grade = "B"
elif score > 40 and score < 60 :
    grade = "C"
elif score > 20 and score < 40 :
    grade = "D"
else :
    grade = "E"
print(f"grade is {grade}")

#123
money = input(">> 돈 입력: ")
answer = money.split("")
if answer[1] == "달러" :
    result = float(money) * 1167
elif answer[1] == "엔" :
    result = float(money) * 1.096
elif answer[1] == "유로" :
    result = float(money) * 1268
elif answer[1] == "위안" :
    result = float(money) * 171
print(result, "원")

#124
number1 = input(">> input number1: ")
number2 = input(">> input number2: ")
number3 = input(">> input number3: ")
if number1 > number2 :
    if number1> number3 :
        biggest = number1
    else :
        biggest = number3
elif number1 < number2 :
    if number2 > number3 :
        biggest = number2
    else :
        biggest = number3
print(biggest)

#125
phone = input(">> 휴대전화 번호 입력: ")
phoneNum = phone.split('-')
if phoneNum[0] == "011" :
    net = "SKT"
elif phoneNum[0] == "016" :
    net = "KT"
elif phoneNum[0] == "019" :
    net = "LGU"
else :
    net = "알수없음"
print(f"당신은 {net} 사용자입니다.")

#126
office = input("우편번호: ")
if office[2] >= 0 and office[2] < 3:
    print("강북구")
elif office[2] >= 3 and office[2] < 6 :
    print("도봉구")
else :
    print("노원구")

#127
people = input(">> 주민등록번호: ")
mf = people.split("-")[1]
if int(mf) == 1 or int(mf) == 2 :
    print("남자")
else :
    print("여자")

#128


#129

#130
