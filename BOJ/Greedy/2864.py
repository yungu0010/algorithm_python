# 5와 6의 차이

a, b = map(str, input().split())

five_a = a.replace('6', '5')
five_b = b.replace('6', '5')
five_result = int(five_a) + int(five_b)

six_a = a.replace('5', '6')
six_b = b.replace('5', '6')
six_result = int(six_a) + int(six_b)

print(five_result, six_result)



