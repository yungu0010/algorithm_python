# 듣보잡

import sys
input = sys.stdin.readline

n, m = map(int,input().split())         # 이름 개수

name1 = set()
name2 = set()
allName = set()

result = []

for _ in range(n):                      # 입력받은 이름을 각각의 set에 넣고 중복을 확인할 전체 allName에도 넣는다.
    name = input().rstrip()
    name1.add(name)
    allName.add(name)

for _ in range(m):
    name = input().rstrip()
    name2.add(name)
    allName.add(name)

for name in allName:                    # 중복 이름 찾기
    if name in name1:
        if name in name2:
            result.append(name)

result.sort()                           # sort는 원본을 변경한다

print(len(result))                      # 중복 이름 개수
for i in result:                        # 이름 출력
    print(i)