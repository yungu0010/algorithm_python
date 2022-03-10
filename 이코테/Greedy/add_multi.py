# 각 자리가 숫자로만 이뤄진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로
# 하나씩 모든 숫자를 확인하여 숫자 사이에 x, + 연산자를 넣어 가장 큰 수를 만들어라.

# 단, 모든 연산은 왼쪽에서부터 순서대로 이뤄진다고 가정
# 만들 수 있는 가장 큰 수는 항상 20억 이하의 정수

# 0이나 1인 경우 +, 2 이상인 경우 X

S = list(input())
result = 0

for s in S :
    s = int(s)
    if s <= 1 or result <= 1 :
        result += s
    else :
        result *= s

print(result)


