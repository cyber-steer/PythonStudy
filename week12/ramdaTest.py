myList=[1,2,3,4,5]
add10 = lambda num : num +10
myList = list(map(add10,myList))
print(myList)

print("-"*20)

def genFunc(num):
    for i in range(0,num):
        yield i
        print('제너레이터 진행중')
for data in genFunc(5):
    print(data)