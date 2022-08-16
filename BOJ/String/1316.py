# 1316 - 그룹 단어 체커

import sys
input = sys.stdin.readline

N = int(input().rstrip())
count = 0

def groupWordCheck(word):
    wordASCII = set(ord(i) for i in word)           # 문자열을 아스키값으로 변환하여 집합으로 저장(중복X)

    for i in range(len(word) - 1):                  
        if ord(word[i]) not in wordASCII:           # 아스키집합에 현재 아스키값이 없으면 같은 수 중복 -> 그룹단어 아님
            return False
        if word[i] != word[i+1]:                    # 문자가 바뀌면 집합에서 값 제거
            wordASCII.remove(ord(word[i]))
    return True

for _ in range(N):
    word = input()
    if groupWordCheck(word):
        count += 1

print(count)