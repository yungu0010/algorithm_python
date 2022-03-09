# A - 5분, B - 1분, C - 10초

time = int(input())

cook_t = [0, 0, 0]
array = [300, 60, 10]

for i in range(0, 3) :
    cook_t[i] = time // array[i]
    time -= array[i] * cook_t[i]
if time > 0 :
    print(-1)
else :
    print(cook_t[0], cook_t[1], cook_t[2])

    