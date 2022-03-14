#숫자의 개수
a = int(input())
b = int(input())
c = int(input())
    

result = str(a*b*c)
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(result)) :
    if result[i] == '0' :
        num[0] += 1
    elif result[i] == '1':
        num[1] += 1
    elif result[i] == '2':
        num[2] += 1
    elif result[i] == '3':
        num[3] += 1
    elif result[i] == '4':
        num[4] += 1
    elif result[i] == '5':
        num[5] += 1
    elif result[i] == '6':
        num[6] += 1
    elif result[i] == '7':
        num[7] += 1
    elif result[i] == '8':
        num[8] += 1
    elif result[i] == '9':
        num[9] += 1
        
for i in range(10) :
    print(num[i])