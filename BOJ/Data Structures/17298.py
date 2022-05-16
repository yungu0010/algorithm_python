# 17298 - 오큰수

# 스택 사용
# 오큰수 NGE(i) = Ai의 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수를 의미
# ex A = [9, 5, 4, 8] -> NGE = [-1, 8, 8, -1]

from sys import stdin
input = stdin.readline

n = int(input().rstrip())
stack = list(map(int,input().split()))
result = []

# for i in range(len(stack)) :
#     if stack[i] > stack[i-1] :
#         result.append(stack[i+1])
#         continue
#     else :
#         result.append(-1)
for i in range(n-1) :
    result.append(-1)
    
for i in range(len(stack)-1) :
    for j in stack[i:] :
        if j > stack[i]:
            result.insert(i, j)
            break
        else :
            continue
        


# 중첩 for문이라 시간복잡도가 O(n^2)으로 시간초과 발생..
# for i in range(len(stack)) :
#     for j in stack[i :] :
#         if j > stack[i]:
#            result.append(j)
#            break
#         elif j == stack[-1]:
#             result.append(-1)
for k in result :
    print(k, end=' ')