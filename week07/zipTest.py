a= ['one', 'two', 'three']
b= ['a','b','c']
for v1, v2 in zip(a, b):
    print(v1, v2)

print()

c = [(1,'a'),(2,'b')]
print(type(c[0]))

print(list(zip(a,b)))