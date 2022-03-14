# 2908 - 상수

a, b = list((input().split()))      #a, b는 타입이 str

#문자열 역순 재배치
c = int(a[::-1])        #[A:B:C] - index A부터 index B까지 C간격으로
d = int(b[::-1])
if c > d :
    print(c)
else :
    print(d)

# for문 사용 방법
# c = ''
# d = ''
# for i in range(len(a)) :
#     c += (a[2-i])
#     d += (b[2-i])

# if int(c) > int(d)  :
#     print(int(c))
# else :
#     print(int(d))
    

