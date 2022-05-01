#str = input("문자열을 입력하세요 : ")
str="abcde"
str2="1"
str2[0] = str[0]
print(str2)

print(str[::-1])
for i in range(len(str)-1, -1, -1):
    print(str[i],end="")
print()
for i in range(len(str)):
    print(str[len(str)-i-1],end="")
print()
