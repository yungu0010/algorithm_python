# 2275 - 부녀회장이 될테야

import sys
input = sys.stdin.readline

testCase = int(input().rstrip())
human = []

for _ in range(testCase):
    floor = int(input().rstrip())           # 층 = k
    num = int(input().rstrip())           # 호수 = n
    arr = [x+1 for x in range(0, num)]

    for i in range(floor):                  # 층 수만큼 반복
        for j in range(1, num):             # num을 인덱스로 사용 num - 1호까지
            arr[j] += arr[j-1]              # 각 층의 호수의 사람수를 업데이트
    print(arr[-1])                          # 가장 마지막층 마지막 호수의 사람 수 출력


# def resident(k, n):
#     global human
#     floor = k
#     room = n

#     if floor == 0 or room == 1:
#         human += room
#         return human

#     resident(floor, room - 1) + resident(floor - 1, room)
#     return human

# testCase = int(input().rstrip())
# human = 0

# for _ in range(testCase):
#     human = 0
#     k = int(input().rstrip())
#     n = int(input().rstrip())
#     print(resident(k, n))