# 2739
n = int(input())

for i in range(9) :
    print("{} * {} = {}".format(n, i+1, n*(i+1)))        #format 메소드
   
    
#10950
n = int(input())
result = []
for i in range(n) :
    a, b = map(int, input().split())
    result.append(a+b)       #index, 값

for i in range(n) :
    print(result[i])


#8393
n = int(input())
result = 0

for i in range(n) :
    result += i+1

print(result)    


#11021
n = int(input())
result = []

for i in range(n) :
    a, b = map(int, input().split())    
    result.append(a + b)                #리스트 값 append

for i in range(n) :
    print('Case #{}: {}'.format(i+1, result[i]))


#11022
n = int(input())

for i in range(n) :
    a, b = map(int, input().split())    
    print('Case #{}: {} + {} = {}'.format(i+1, a, b, a+b))


# 10871
n, x = map(int, input().split())
seq = list(input().split())
tmp = []

for i in range(len(seq)) :          #len(list) : 리스트 길이 구하기
    if int(seq[i]) < x :
        tmp.append(seq[i])
for i in range(len(tmp)) :
    print(tmp[i], end=" ")


