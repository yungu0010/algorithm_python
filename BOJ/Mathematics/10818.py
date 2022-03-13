# 10818 - 최소, 최대

n = int(input())
num = list(map(int, input().split()))       #숫자를 받아 리스트로 저장
print(min(num), max(num))

#🤡내장 함수 이용하지 않고 풀기
min = num[0]
max = num[0]

for i in num[1:] :  #리스트 순회
    if min < i :
        min = i
    if max > i :
        max = i
print(min, max)