while True:
    n = int(input("숫자입력 0은 종료 : "))
    if n ==0:
        break;
    elif n%2==0 and n>0:
        print("짝수입니다")
    elif n%2==1 and n>0:
        print("홀수입니다")
    else:
        print("양수를 입력합니다")