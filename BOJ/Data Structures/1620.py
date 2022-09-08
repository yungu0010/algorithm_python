# 1620 - 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
poketmonDict = {}
indexPoketmon = {}

for i in range(N):
    poketmon = input().rstrip()
    poketmonDict[poketmon] = i          # 포켓몬 : 인덱스
    indexPoketmon[i] = poketmon         # 인덱스 : 포켓몬

for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():               # 숫자인 경우
        print(indexPoketmon[int(problem)-1])    # 딕셔너리에 저장한 인덱스는 0부터 시작하므로
    else:                               # 포켓몬 이름인 경우
        print(poketmonDict[problem] + 1)        # 포켓몬 이름의 인덱스값 + 1   
