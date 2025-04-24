def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0:                # 배열이 비어있다면 삽입
            answer.append(a)
            continue
        if answer[-1] == a: continue        # 배열의 마지막 숫자와 현재 숫자가 같으면 중복임으로 continue
        answer.append(a)                    # 같지 않은 경우 삽입
    return answer
