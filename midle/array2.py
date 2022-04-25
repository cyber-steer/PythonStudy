aa =[[1,2],[3,4],[5,6]]

for i in range(len(aa)):
    for j in range(len(aa[i])):
        print(aa[i][j],end=" ")
    print()
print("="*20)
list1 = []
list2 = []
value =1
for i in range(0,3):
    for k in range(0,4):
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0,3):
    for k in range(0,4):
        print("%3d " % list2[i][k], end="")
    print("")

print("="*20)

aa = [[1,2,3,4],[5,6],[7,8,9]]
for i in range(len(aa)):
    sum = 0
    for j in range(len(aa[i])):
        sum += aa[i][j]
    print(sum)

print("="*20)
tt1 = (10,20,30) #튜플
tt2 = 10,20,30 #튜플
tt3 = (10) # 정수
tt4 = 10 #정수
tt5 = (10,) #튜플
tt6 = 10, #튜플
print(tt1,tt2,tt3,tt4,tt5,tt6,sep="\n")
print("tt1 :",type(tt1))
print("tt2 :",type(tt2))
print("tt3 :",type(tt3))
print("tt4 :",type(tt4))
print("tt5 :",type(tt5))
print("tt6 :",type(tt6))
print("="*20)
myTuple =(10,20,30)
myList = list(myTuple)
myList.append(40)
myTuple=tuple(myList)
print(myTuple)