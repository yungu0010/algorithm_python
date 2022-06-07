# 단어공부

word = input().upper()
wordSet = list(set(word))

num = []
cnt = 0

for i in wordSet:
    cnt = word.count(i)
    num.append(cnt)

if num.count(max(num)) >= 2:
    print("?")
else:
    print(wordSet[num.index(max(num))])

