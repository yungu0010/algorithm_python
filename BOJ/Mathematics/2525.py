h, m = map(int, input().split())
time = int(input())

if m + time >= 60 :
    if h + (m + time) // 60 >= 24 :     #23일 때 뿐만 아니라 시간 자체가 24를 넘기는 경우 생각해야 함
        h += (m + time) // 60 - 24
    else :
        h += (m + time) // 60
    m = (m + time) % 60
else :
    m += time
print(h, m)