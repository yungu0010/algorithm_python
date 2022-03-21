# 12605 - 단어순서 뒤집기

from sys import stdin
input = stdin.readline
n = int(input().rstrip())           # 입력받을 테스트 케이스 수 
for i in range(n) :
    string = list(input().split())
    print("Case #{}: {}".format(i+1, ' '.join(string[::-1])))       # 공백을 기준으로 역순으로 문자열 join