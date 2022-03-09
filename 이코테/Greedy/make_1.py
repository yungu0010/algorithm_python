# 어떤 수 N이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

# 예시
# N이 17, K가 4라면 1, 2, 2를 수행

# 최대한 많이 나누기를 수행 - 기하급수적으로 빠르게 줄일 수 있기 때문

n, k = input().split()     #입력받은 값을 공백을 기준으로 분리

# 값이 이미 할당되어 있어도 새로운 값을 할당하면 기존 값 사라짐
n = int(n)
k = int(k)

# n, k = map(int, input().split())      map함수 이용하면 더 간결

count = 0

while n > 1 :
    if n % k == 0 :
        n = n / k
        count += 1
    else :
        n -= 1
        count += 1

print(count)


# 풀이 - O(log)
# result = 0
# while True :
#     target = (n // k) * k     N이 K로 나누어 떨어지는 수가 될 때까지 빼기
#     result += (n - target)
#     if n < k:                 N을 K로 나눌 수 없을 때 반복물 탈출
#         break
#     result += 1
#     n //= k                   K로 나누기
# result += (n - 1)             남은 수에 대해 1씩 빼기
