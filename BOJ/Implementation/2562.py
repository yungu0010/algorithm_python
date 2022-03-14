#2562 - 최댓값

num = []
index = 0
mx = 0
for i in range(0, 9) :
    a = int(input())
    num.append(a)
    if mx < a :
        mx = a
        index = i+1
print(mx)
print(index)