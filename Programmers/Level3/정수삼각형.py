#     [0]
#    [0 1]
#   [0 1 2]
#  [0 1 2 3]
# [0 1 2 3 4]

# 규칙 dp[i][j] = max(dp[i][j], dp[i][j] + dp[i-1][j], dp[i][j] + dp[i-1][j-1])

def solution(triangle):
    height = len(triangle)
    dp = [[0] * i for i in range(1, height+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, height):
        for j in range(0, len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j + 1 == len(triangle[i]):
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i-1][j-1] + triangle[i][j])
    
    return max(dp[height-1])
