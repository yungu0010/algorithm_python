# 5532 - 방학 숙제

# 방학 : L일, 수학 : B페이지, 국어 : A페이지
# 하루 최대양 : 수학 - D페이지, 국어 - C페이지
import math

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

m = math.ceil(B/D)      #math.ceil = 반올림 함수
k = math.ceil(A/C)

study = max(m, k)
    
print(L - study)    