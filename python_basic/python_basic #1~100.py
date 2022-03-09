#1 ~ 10 파이썬 시작하기
#1
print("#1. \n") #자동줄바꿈
print('Hello World')

#2
print("\n#2. ")
print("Mary's cosmetics")

#3
print("\n#3. ")
print("신씨가 소리질렀다. \"도둑이야\".")
print('신씨가 소리질렀다. \"도둑이야\".')

#4
print("\n#4. ")
print("\"C:\\Windows\"")

#5
print("\n#5. ")
print("안녕하세요.\n만나서\t\t반갑습니다.")
#\n : 줄바꿈
#\t : 탭

#6
print("\n#6. ")
print("오늘은", "일요일")
#오늘은 일요일
#중간 공백 생김

#7
print("\n#7. ")
print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep=";")
# print 함수의 sep 인자, 출력값들 사이에 한 칸의 공백 대신 들어갈 문자 지젖ㅇ

#8
print("\n#8. ")
print("naver/kakao/sk/samsung")
print("naver","kakao","sk","samsung", sep="/")

#9
print("\n#9. ")
print("first", end=""); print("second")
#end : 출력을 완료한 뒤 내용 수정 가능

#10
print("\n#10. ")
print(5/3)


# 파이썬 변수
#11
print("\n#11. ")
삼성전자 = 50000
print(10*삼성전자)

#12
print("\n#12. ")
시가총액 = 289
현재가 = 50000
PER = 15.79
#타입확인
print(type(시가총액))
print(type(현재가))
print(type(PER))

#13
print("\n#13. ")
s = "hello"
t = "python"
print(s+"! " + t) 
print(s+"!", t) #,는 한 칸 공백

#14
print("\n#14. ")
print(2 + 2 * 3)
#>> 8

#15
print("\n#15. ")
#type() : 데이터 타입 판별
a = 128
print(type(a))

b = "132"
print(type(b))

#16 ~ 19 타입변환
print("\n#16 ~ 19. ")
num_str = "720"
print(int(num_str))

num = 100
print(str(num))

print(float("15.79"))

year = "2021"
year = int(year) #재할당
print(year, year-1, year-2)

#20
print("\n#20. ")
price = 48584
print(48584 * 36)


# 파이썬 문자열
#21
print("\n#21. ")
letters = 'pyton'
print(letters[0], letters[2])

#22
print("\n#22. ")
license_plate = "24가 2210"
print(license_plate[-4 :])

#❔23 홀만 출력하기
print("\n#23.")
string = "홀짝홀짝홀짝"
# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋 지정 가능
print(string[::2])

#24 ❗문자열 뒤집기
print("\n#24.")
string = "PYTHON"
print(string[::-1])

#25 문자열 치환
print("\n#25.")
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))

#26 공백지우기
print("\n#26.")
print(phone_number.replace('-', ''))

#❔27 .뒤에만 출력
print("\n#27.")
url = "http://sharebook.kr"
url_split = url.split('.') #.을 기준으로 분리 가능
print(url_split[-1]) #.을 기준으로 뒷 부분 출력

#28. 문자열은 immutable
print("\n#28.")
lang = 'python'
#lang[0] = 'P'
#print(lang)
# >> Python 아님❗ 문자열은 이런식으로 일부 할당 할 수 없음

#29 replace
print("\n#29.")
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

#30
print("\n#30.")
string = 'abcd'
string.replace('b', 'B')
print(string)
#aBcd가 아님❗
#abcd가 그대로 출력, 문자열은 28번에서 볼 수 있듯이 변경할 수 없는 자료형이므로
#replace 메소드 사용시 원본은 그대로 둔 채 변경된 새로운 문자열 객체 리턴

#31
print("\n#31.")
a = "3"
b = "4"
print(a+b)
# >> 34
#34라는 새로운 문자열이 생성됨, a와 b는 각각 3, 4로 존재

#32
print("\n#32.")
print("Hi" * 3)
# >> HiHiHi

#33
print("\n#33.")
print('-'*80)

#34
print("\n#34.")
t1 = 'python'
t2 = 'java'
print((t1, t2)*4) #('python', 'java', 'python', 'java', 'python', 'java', 'python', 'java')
print((t1, t2))
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)


#35 %formatting
print("\n#35.")
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름: %s 나이: %d' %(name1, age1))
print('이름: %s 나이: %d' %(name2, age2))

#36 ❔format()메소드
# format() 메소드는 타입과 관계없이 값이 출력될 위치에 {}적어주면 됨
print("\n#36.")
print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {} 나이: {}'.format(name2, age2))

#37 ❔f-string
#파이썬 3.6부터 지원, 문자열 앞에 f가 붙은 형태로 {변수}와 같은 형태로 문자열 사이에 타입과 관계없이 출력
print("\n#37.")
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

#38
print("\n#38.")
상장주식수 = "5,969,782,550"
replace = 상장주식수.replace(',', '')
print(int(replace), type(int(replace)))

#39
print("\n#39.")
분기 = "2020/03(E) (IFRS연결)"
split = 분기.split("(")
print(split[0])
print(분기[:7])

#40 strip 공백제거
print("\n#40.")
data = "   삼성전자   "
print(data.strip())

#41 upper
print("\n#41.")
ticker = "btc_krw"
print(ticker.upper())

#42 lower
print("\n#42.")
ticker = "BTC_KRW"
print(ticker.lower())

#43 capitalize
print("\n#43.")
string = 'hello'
print(string.capitalize())

#44 endswith
print("\n#44.")
file_name = "보고서.xlsx"
print(file_name.endswith('xlsx'))

#45 endswith
print("\n#45.")
print(file_name.endswith(('xlsx', 'xls'))) #여러개 쓸 땐 ()로 감싸기

#46 startswith
print("\n#46.")
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#47
print("\n#47.")
a = "hello world"
print(a.split()) #아무것도 없을 땐 공백기준으로 분리

#48
print("\n#48.")
ticker = "btc_krw"
print(ticker.split('_'))

#49
print("\n#49.")
date = "2020-05-01"
print(date.split('-'))

#50
print("\n#50.")
data = "039490     "
print(data.rstrip())


#파이썬 리스트
#51
print("\n#51.")
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

#52
print("\n#52.")
movie_rank.append('배트맨')
print(movie_rank)

#53
print("\n#53.")
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

#54
print("\n#54.")
movie_rank.remove('럭키')
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

#del vs remove() vs pop()
#❗❗❗del은 아무것도 리턴하지 않지만 pop은 deleted list 반환 -> dic에서도 동일
#특정한 오브젝트 지우려면 remove 사용이 더 용이
#특정 location(index) 지우려면 del이나 pop이 더 용이



#55
print("\n#55.")
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
print(movie_rank)
del movie_rank[2]
print(movie_rank)
# 불가, remove()안에는 하나의 원소만 가능
# movie_rank.remove('스플릿', '배트맨')

#56
print("\n#56.")
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2 # + 연산 시 리스트 합치기 가능
print(langs)
# 중복 원소 있는 경우는 어떻게 될까?
lang1 =  ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C"]
print(lang1 + lang2)
#중복 제거 안됨

#57 min() max()
print("\n#57.")
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max: {max(nums)}\nmin: {min(nums)}')

#❗58 리스트 합 출력
print("\n#58.")
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#59
print("\n#59.")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook)) #리스트 저장 데이터 개수 구하는 메소드

#60 리스트 평균 출력
print("\n#60.")
average = sum(nums) / len(nums)
print(average) #float로 반환

#61
print("\n#61.")
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#62
print("\n#62.")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#63
print("\n#63.")
print(nums[1::2])

#64
print("\n#64.")
print(nums[::-1])

#65
print("\n#65.")
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])
print(interest[0], interest[2])

#66 ~ 68 join 메소드, 문자열 sep이랑 비슷한 듯
#join사용 : 구분자.joint(리스트)
print("\n#66 ~ 68.")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

print("/".join(interest))

print("\n".join(interest))

#69 split
print("\n#69.")
string = "삼성전자/LG전자/Naver"
print(string.split('/')) 
#split 메소드는 리스트 형태로 반환

#70
print("\n#70.")
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

data = [2, 4, 3, 1, 5, 10, 9]
print(sorted(data)) #None 출력
# sort() vs sorted() => key설정 가능, reverse(내림차순) 가능
# sort() : 원래 리스트도 변경, 반환값은 None
# sorted() : 반환값 list 새로운 변수에 할당 가능


#파이썬 튜블
#71
print("\n#71.")
my_variable = ()
print(type(my_variable)) #튜플 타입 확인
# tuple vs list => 어떤 자료형도 가능(함께 저장 가능)
# list : [], 값 생성, 삭제, 수정 가능
# tuple : (), immutable, 할당 시 괄호 생략 가능, 튜플 안에 튜플 원소로 가질 수 있음

#72
print("\n#72.")
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')
print(movie_rank)

#73
print("\n#73.")
num = (1)
num_t = (1,)

print(type(num))    #int
print(type(num_t))  #tuple
# 하나의 데이터를 저장하는 튜플에는 꼭❗ 뒤에 ,를 추가해주어야 함

#74
print("\n#74.")
print("주석  확인")
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# 튜플은 값을 변경할 수 없기 때문에 index로 값을 할당할 수 없다.

#75
print("\n#75.")
t = 1, 2, 3, 4
print(t)
# 튜플은 괄호 없이도 정의 가능

#76
print("\n#76.")
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t) #t[0] = 'A 불가, 새로 할당할 경우 기존 튜플 삭제

#❔77 tuple -> list
print("\n#77.")
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(interest, type(interest))

#❔78 list->tuple
print("\n#78.")
interest = tuple(interest)
print(interest, type(interest))

#79 튜플 언팩킹
print("\n#79.")
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# >> apple banana cake
#javascript의 비구조화 할당과 비슷

#80 ❗❗range(시작, 끝, 증가폭)
print("\n#80.")
data = tuple(range(2, 100, 2))
print(data)


#파이썬 딕셔너리
#81 star expression 사용하면 언패킹 시 좌우변 데이터 개수 달라도 됨
print("\n#81.")
a, b, *c = (0, 1, 2, 3, 4, 5)
print(f'a: {a} b: {b} c: {c}')

#좌측 8개 값 바인딩
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores #남은 두 개  _ 사용하여 생략 가능
print(valid_score)

#82 우측 8개 값 바인딩
print("\n#82.")
_, _, *valid_score = scores
print(valid_score)

#83 가운데 8개 값 바인딩
print("\n#83.")
_, *valid_score, _ = scores
print(scores)

#84
print("\n#84.")
temp = {} #딕셔너리: key - value
print(type(temp))

#85
print("\n#85.")
dic = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800}
print(dic)

#86 딕셔너리에 값 추가
print("\n#86.")
dic['죠스바'] = 1200
dic['월드콘'] = 1500
print(dic)

#87
print("\n#87.")
#print(dic('메로나')) #TypeError: 'dict' object is not callable 호출 시 []사용
print(dic["메로나"])

#88
print("\n#88.")
dic['메로나'] = 1300
print(dic)

#89
print("\n#89.")
del dic["메로나"]
print("del", dic)

#pop vs popitem vs del
#del은 아무것도 리턴하지 않음❗❗
#pop은 element 리턴
#dict.pop(key, default) // default: if the key is not available in the dict, then it will return the derault value.
#pop() is retulr element. Key isn't in dict, return default

dic = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800, '죠스바' : 1200, '월드콘' : 1500}
a = dic.pop('메로나')
print("pop():", a)

dic = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800, '죠스바' : 1200, '월드콘' : 1500}
dic.popitem()
# python 3.6 이상에서는 마지막 key-value 삭제
# python 3.5 이하에서는 임의의 key-value값 삭제
print("popitem: ", dic)

#90
print("\n#90.")
print("주석 참고")
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# key값이 존재하지 않기 때문에 에러 발생

#91
print("\n#91.")
inventory = {'메로나' : (300, 20), '비비빅' : (400, 3), '죠스바': (250, 100)}
print(inventory, type(inventory))

#92 딕셔너리 인덱싱
print("\n#92.")
print('%d 원' %(inventory["메로나"][0]))

#93
print("\n#93.")
print('%d 개' %(inventory["메로나"][1]))

#94 딕셔너리 추가
print("\n#94.")
inventory['월드콘'] = [500, 7]
print(inventory)

#95 딕셔너리 keys() 메소드
print("\n#95.")
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icekey = icecream.keys()
print(icekey, type(icekey)) #dict_keys 타입
print(list(icekey), type(list(icekey))) #dict_keys 타입

#96 ~ 97 딕셔너리 values() 메소드
print("\n#96 ~ 97.")
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icevalue = icecream.values()
print(list(icevalue), type(list(icevalue)))

sum = sum(icevalue)
print(sum)

#98 update 메소드
print("\n#98.")
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99 zip과 dict : 아래 두 개 튜플을 하나의 딕셔너리로 변환
print("\n#99.")
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals)) #dict로 변환해주어야 함
print(result, type(result))

#100 : 두 개의 리스트를 하나의 딕셔너리로 생성
print("\n#100.")
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table, type(close_table))