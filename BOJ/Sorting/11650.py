# 11650 - 좌표 정렬하기
n = int(input())
coordinate = []     #좌표를 저장할 리스트

for i in range(n) :
    x_y = list(map(int, input().split()))       #좌표 입력
    coordinate.append(x_y)           #리스트에 좌표 저장
coordinate = sorted(coordinate)      #⭐list.sort() = None반환, sorted(list) = 정렬된 리스트 반환

for i in range(len(coordinate)) :    #정렬된 리스트 출력
    print('{} {}'.format(int(coordinate[i][0]), int(coordinate[i][1])))
    
#🌟 sort함수에서 lanbda 사용하기
# coordinate.sort(key = lambda x : (x[0], x[1])) x[0] 순서대로 오름차순, x[1]순서대로 오름차순
# EX. 첫 번째 인자를 기준으로 오름차순, 두 번째 인자를 기준으로 내림차순 -> key = lambda x : (x[0], -x[1])
