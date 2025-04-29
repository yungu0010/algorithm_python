# 선택하거나, 선택하지 않거나
# 집 개수 최대 100만개

# 2차원 배열로 두고, index 0은 털지 않음, index 1은 털기 로 둔다
# dp[0][0] = 0, dp[0][1] = 1
# dp[1][0] = 1, dp[1][1] = 2
# dp[2][0] = 2, dp[2][1] = 4
# dp[3][0] = 4, dp[3][1] = 3

# 원형이기 때문에 첫번째 집을 털면 마지막 집은 반드시 털면 안됨
# 마지막 집을 털면 첫번째 집을 털면 안됨 !! 

def rob_house(money):
    dp = [[0] * 2 for _ in range(len(money))]
    dp[0][1] = money[0]
    
    for i in range(1, len(money)):
        dp[i][0] = max(dp[i-1][1], dp[i-1][0])
        dp[i][1] = dp[i-1][0] + money[i]
    
    return max(dp[i])

def solution(money):
    ans1 = rob_house(money[1:])
    ans2 = rob_house(money[:-1])
    
    return max(ans1, ans2)


