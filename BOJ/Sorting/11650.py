# 11650 - 좌표 정렬하기
n = int(input())
coordinate = []     #좌표를 저장할 리스트

for i in range(n) :
    x_y = list(map(int, input().split()))       #좌표 입력
    coordinate.append(x_y)           #리스트에 좌표 저장
coordinate = sorted(coordinate)      #⭐list.sort() = None반환, sorted(list) = 정렬된 리스트 반환

for i in range(len(coordinate)) :    #정렬된 리스트 출력
    print('{} {}'.format(int(coordinate[i][0]), int(coordinate[i][1])))