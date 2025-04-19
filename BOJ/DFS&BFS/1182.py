# 1182 - 부분 수열의 합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
def dfs(index, temp):
    global answer
    if index == n:
        if sum(temp) == s and len(temp) > 0:
            answer += 1
        return

    temp.append(nums[index])
    dfs(index+1, temp)
    temp.pop()
    dfs(index+1, temp)

# 선택하거나, 선택하지 않거나
dfs(0, [])
print(answer)