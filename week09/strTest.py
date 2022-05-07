str = "hello"
for i in range(len(str)):
    print(str[i]+"$",end="")
print()
a="happy python"
print(a.find('a'))
print(a.find("h"))
print(a.rfind("h"))
print(a.find("h",5))
print(a.startswith("p"))
print(a.endswith("n"))
print()
a="  파 이 썬  "
print("'"+a+"'")
print("'"+a.strip()+"'")
print("'"+a.rstrip()+"'")
print("'"+a.lstrip()+"'")
a="---파-이-썬---"
print(a)
print(a.strip("-"))
a="<<<파<<이>>썬>>>"
print(a)
print(a.strip("<>"))
a="ITCookBook for Python"
print(a)
for i in range(len(a)):
    if a[i] == 'o':
        print("$",end="")
    else:
        print(a[i],end="")
print("")
print("파이썬".join("Python"))