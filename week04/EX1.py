while True:
    n = input("1.입력한 수식계산 2.두 수 사이의 합계 0.종료: ")
    if n=='0':
        break
    elif n=='1':
        str = input("***수식을 입력하세요 : ")
        result = eval(str)
        print("{} 결과는 {}입니다".format(str,result))
    elif n=='2':
        a = int(input("***첫번째 숫자를 입력하세요 : "))
        b = int(input("***두번째 숫자를 입력하세요 : "))
        sum = 0
        for i in range(a,b):
            sum += i
        print(f"{a}+...+{b}는{sum}")
    else:
        print("종료를 원하시면 0을 입력하시오")
    print()