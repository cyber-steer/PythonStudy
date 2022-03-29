a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'sakai'
print(f'My name is {name} {family}, {family} {name}')

print('-'*30)

a = 'a'
print('a is {}'.format(a))

x, y, z = 1, 2, 3
print('a is {0}, {1}, {2}'.format(x,y,z))
print('a is {0}, {1}, {2}'.format(z,y,x))

name = 'Jun'
family = 'sakai'
print('My name is {0} {1}, {1} {0}'.format(name,family))

s1 = 'aaaaaaaaaaaaaaa' \
     'aaaa'+'aaaaaaaaaaaaaa'
print(s1)