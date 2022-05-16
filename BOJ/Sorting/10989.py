# 10989 - 수 정렬하기 3

n = int(input())
result = []

for i in range(n) :
    a = int(input())
    result.append(a)
result.sort()
for i in result :
    print(i)    