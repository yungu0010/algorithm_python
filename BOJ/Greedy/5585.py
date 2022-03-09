# 500, 100, 50, 10, 5, 1

# 물건의 금액
money = int(input())
# 타로가 받을 동전의 개수
taro = 0
result = 1000 - money
# if 1 < money < 1000 : 
#     result = 1000 - money  #거슬러줄 돈
#     print(result)
# else :
#     print("1 이상 1000미만의 정수를 입력하세요.")

coin = [500, 100, 50, 10, 5, 1]

for c in coin :
    taro += result // c   # 거스름돈을 코인으로 나눈 몫
    result %= c          # 해당 화폐로 거슬러주고 남은 돈

print(taro)