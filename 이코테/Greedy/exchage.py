# 큰 단위가 항상 작은 단위의 배수인 경우만 최적의 해 구할 수 있음
# 500, 100, 50, 10

money = int(input("거스름돈을 입력하세요"))
count = 0  # 거슬러줄 동전의 개수

array = [500, 100, 50, 10]  #큰 단위 화폐부터 확인
for k in array :         # 화폐의 종류만큼 반복
    count += money // k  # 금액을 화폐로 나눈 몫을 더함
    money %= k               # 거슬러주고 남은 돈 저장

print(count)
