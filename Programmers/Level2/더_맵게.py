# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K 이상이 될 때 까지 반복하여 섞음
# 섞어야 하는 최소 횟수
# 2 <= scoville 길이 <= 100만, 0 <= 스코빌 원소 <= 100만
# 0 <= K <= 10억
# 불가능한 경우 -1 return

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)                             # 리스트를 힙으로 변환
    
    # 최솟값이 K미만일 때 반복
    answer = 0
    while scoville[0] < K:
        heapq.heappush(scoville, (heapq.heappop(scoville) + heapq.heappop(scoville) * 2))
        answer += 1
        if scoville[0] < K and len(scoville) == 1:      # 첫번째 값이 K 미만인데, 원소가 1개 남은 경우
            return -1
            
    return answer
