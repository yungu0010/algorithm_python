# 집 -> 학교까지의 최단경로 개수 % 1,000,000,007
# dp[i][j] = dp[i][j-1] + dp[i-1][j]

def solution(m, n, puddles):
    blocked = {(r-1, c-1) for c,r in puddles}   # puddles를 집합으로 변경하여 탐색 시간 줄임, 0-indexed로 변경
    dp = [[0] * m for i in range(n)]            # m: 가로, n: 세로
    dp[0][0] = 1
    
    # 첫 열
    for i in range(1, n):
        if (i, 0) in blocked:                   # 웅덩이 지역이면 continue
            continue
        dp[i][0] = dp[i-1][0]                   # 이전 블록까지 갈 수 있는 최단거리와 같음
    
    # 첫 행
    for j in range(1, m):
        if (0, j) in blocked:
            continue
        dp[0][j] = dp[0][j-1]
    
    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in blocked: 
                continue                    # 웅덩이라면 continue
            else:                           # 최단거리가 2개 이상일 경우
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
    return dp[n-1][m-1] % 1000000007
