# 4673 - 셀프 넘버

num = []
kapreNumList = []
sum = 0

# kapre수를 구하는 함수
def d(n):
    global sum
    sum = 0
    kapreNum = 0
    kapreNum = n + digitSum(n)
    kapreNumList.append(kapreNum)

# 각 자리 수의 합을 구하는 함수
def digitSum(a):
    global sum
    if a < 10:
        sum += a
    else:
        sum += a % 10
        a = a // 10
        digitSum(a)
    return sum

for i in range(10000):
    num.append(i + 1)
    d(i)

# 셀프 넘버(set의 차집합 이용)
result = set(num) - set(kapreNumList)
result = sorted(result)

for i in result:
    print(i)