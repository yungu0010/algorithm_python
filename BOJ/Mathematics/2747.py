# 2747 - 피보나치 수
# 1초(추가 시간 없음)
# 재귀함수를 사용해 코드를 작성할 경우 시간초과 -> 재귀함수를 사용하지 않고 배열 사용
import sys
input = sys.stdin.readline
n = int(input().rstrip())

num = [0, 1]                #0번째, 1번째 피보나치 수 저장
for i in range(n + 1) :
    if i <= 1 :
        continue
    else :
        num.append(num[i-1] + num[i-2])
print(num.pop())