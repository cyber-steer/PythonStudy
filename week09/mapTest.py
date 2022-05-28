myList = [1,2,3,4,5]
result = []
for v in myList:
    result.append(v+1)
print(result)
print()

def add_one(n):
    return n+1
result=[]
result = list(map(add_one, myList))
print(result)
print()

def dic_func(**para):
    for k in para.keys():
        print("%s -->%d명입니다."%(k,para[k]))
dic_func(트와이스=9,소녀시대=7, 걸스에디=4, 블랙핑크=4)