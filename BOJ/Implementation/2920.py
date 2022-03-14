# 음계
music = list(map(int,(input().split())))
ascend = 0
descend = 0

# 또는 True False 이용하기
for i in range(8) :
    if i+1 == music[i] :
        ascend += 1
    elif 8 - i == music[i] :
        descend += 1
if ascend == 8 :
    print('ascending')
elif descend == 8 :
    print('descending')
else :
    print('mixed')
    