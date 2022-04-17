n = int(input("1-10 범위의 수를 입력"))
if n in [2,3,5,7]:
    print("소수")
elif n<1 or n>10:
    print("잘못된 입력")
else:
    print("소수 아님")

for i in range(1000):
    for j in range(2,i):
        if i%j ==0:
            break
        if j == i-1:
            print(str(i), end=", ")