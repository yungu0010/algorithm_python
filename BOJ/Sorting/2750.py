# 2750 - 수 정렬하기
n = int(input())
num = []

for i in range(n) :
    a = int(input())
    num.append(a)
num = sorted(num)
for i in num :
    print(i)
    
# sort를 사용하지 않고 정렬하기
#insertion
# for i in range(1,len(num)):
#     j = i - 1
#     key = nums[i]
#     while j >= 0 and (key < num[j]):     num[i] < num[i - 1] 인 경우, 즉 인덱스가 작은 값이 더 큰 경우
#         num[j+1] = num[j]                num[i] = num[i - 1] 값으로 변경
#         j = j - 1                        
#     nums[j+1] = key                      