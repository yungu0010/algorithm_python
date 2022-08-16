n = int(input())

def starPrint(len):
    if len == 3:
        return ['***','* *','***']

    arr = starPrint(len//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(len//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(starPrint(n)))