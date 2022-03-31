str = input("문자 입력 : ")

for i in range(len(str)+1):
    print(str[0:i])

print()
for i in range(len(str)):
    for j in range(i):
        print(" ", end="")
    print(str[i])