# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험과 그룹에 참여해야함
# 꼭 모든 여행가가 모험을 떠나지 않아도 됨.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 구하시오.

# idea : 오름차순 정렬 후 공포도가 가장 낮은 모험가부터 확인

people = int(input())       #모험가의 수
fear = list(map(int, input().split))
fear.sort()                 #리스트 정렬

adventure = 0               #팀에 속한 모험가 수
result = 0                  #그룹 수

for f in fear :
    adventure += 1          #현재 팀에 모험가 포함시키기
    if adventure >= f :
        result += 1         #그룹 결성
        adventure = 0       #팀 초기화

print(result)