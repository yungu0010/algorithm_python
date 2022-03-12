#10952

result = []

while True :
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    result.append(a+b)
    
for i in range(len(result)) :
    print(result[i])
    
    
#10951 - EOF 주의
# EOF : 더 이상 읽을 수 있는 데이터가 없을 때를 의미

while True :
    try :
        a, b = map(int, input().split())            #EOF처리를 해주어야 런타임 에러가 나지 않음
        print(a + b)
    except EOFError:        #EOFError 예외처리
        break
    
# 🤔EOFError 처리 두번째 방식
# sys 라이브러리의 readlines()이용
# sys.stdin.readlines()를 사용해 파일의 끝까지 가져옴.
# 가져온 파일 내용을 줄 단위로 처리할 수 있음.