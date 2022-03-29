while True:
    n = input("정수를 입력하세요 종료를 원하시면 q를 입력하세요 : ")
    if n == 'q':
        break
    else:
        n = int(n)
        if n%2 ==0:
            print("짝수 입니다")
        else:
            print("홀수 입니다")
    print()