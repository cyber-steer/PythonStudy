
def a(n):
    global money
    if money // n == 0:
        return 0;
    print("{0}원짜리 ==> {1}개".format(n,money // n))
    money %= n

while True:
    print("종료는 00000")
    money = input("교환할 돈은 얼마? : ")
    if money == '00000':
        break;
    money = int(money)
    a(50000)
    a(10000)
    a(5000)
    a(1000)
    a(500)
    a(100)
    a(50)
    a(10)
    print("바꾸지 못한 잔도 ==> {}원".format(money))
    print()