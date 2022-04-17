dic1 = {1:'a', 2:'b',3:'c'}
dic2 = {'a':1, 'b':2, 'c':3}
student1={'학번':1000,'이름':'홍길동','학과':'컴퓨터학과'}
print(dic1)
print(dic2)

print("\n생성")
print(student1)

student1['연락처'] = '010-1111-222'
print("\n연락처 추가")
print(student1)

student1['학과']='파이썬학과'
print("\n학과 수정")
print(student1)

del(student1['학과'])
print("\n학과 삭제")
print(student1)

print()
print(student1['이름'])
print(student1.get('이름'))

print()
print(student1.keys())
print(list(student1.keys()))

print()
print(student1.items())
print(list(student1.items()))