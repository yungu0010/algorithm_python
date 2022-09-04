# 2108 - 통계학

from itertools import count
import sys
input = sys.stdin.readline

N = int(input().rstrip())
number = []

# 최빈값 구하기
def countingSort(data):
    count = {}                          # 음수값도 있기 때문에 딕셔너리를 사용한 계수정렬 사용
    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    maxCount = max(count.values())      # value의 최댓값
    maxNum = []
    for key, val in count.items():      
        if val == maxCount:
            maxNum.append(key)

    if len(maxNum) > 1:                 # 최빈값이 여러개라면 두 번째로 작은 수 출력
        return maxNum[1]
    else:
        return maxNum[0]

# 평균 구하기
def avg(data):
    sum = 0
    for i in data:
        sum += i
    result = round(sum / len(data))
    return result

for _ in range(N):
    number.append(int(input().rstrip()))

number.sort()

print(avg(number))
print(number[int(len(number)/2)])
print(countingSort(number))
print(number[-1] - number[0])