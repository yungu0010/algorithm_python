# A - 5분, B - 1분, C - 10초
# 300s, 60s, 10s 로 큰 단위가 작은 단위의 배수

time = int(input())

cook_t = [0, 0, 0]          # 각각 A, B, C 의미
array = [300, 60, 10]       #전자레인지 시간

for i in range(0, 3) :
    cook_t[i] = time // array[i]       
    time -= array[i] * cook_t[i]
if time > 0 :               # A, B, C 이후 시간이 남는다면
    print(-1)
else :
    print(cook_t[0], cook_t[1], cook_t[2])

    