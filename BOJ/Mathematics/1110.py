# # 더하기 사이클

# #10보다 작은 수는 앞에 0을 붙여 두 자리 수로 만듦
# #각 자리 숫자를 더한 뒤, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를
# #이어 붙이면 새로운 수를 만들 수 있음
# #Ex. 26 -> 68(2+6) -> 84(6+8) -> 42 (8+4) -> 26(4+2)  사이클 4    


n = int(input())
unit = n % 10      #일의 자리
ten = n // 10      #십의 자리
tmp = 0            #중간 덧셈
next = 0           #다음 수
cycle = 0          #사이클 횟수

while True :
    cycle += 1              #사이클 시작
    tmp = unit + ten           
    next = (tmp % 10) + unit * 10   #다음 수 구하기
    unit = next % 10
    ten = next // 10
    if n == next :          #입력한 수와 구한 수가 같을 경우 종료
        break
    else :
        continue
    
print(cycle)


# 리스트 사용해서 풀려고 했는데 시간 초과가 남..
# n = list(map(int,input()))
# first = n
# next = 0    #다음 사이클 숫자
# cycle = 0


# #다시 정리하는 map
# #list(map(함수, 리스트))
# #tuple(map(함수, 튜플))
# #map에는 리스트뿐만 아니라 모든 반복 가능한 객체를 넣을 수 있음

# while True :
#     cycle += 1
#     if len(n) < 2:
#         n.insert(0, 0)
#     temp = n[0] + n[1]
#     temp = temp % 10
#     next = 10 * n[1] + temp
#     next = list(map(int, str(next)))
#     if first == next :
#         break
#     else :
#         n = next

# print(cycle)