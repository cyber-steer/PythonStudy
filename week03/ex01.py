print(100+100)
print("%d"%100)
print("%d %f %d %d "%(10, 20.12, 53, 12))
print()

print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)
print("%fd" % 123.45)
print("%7.1fd" % 123.45)
print("%7.3fd" % 123.45)
print("%s"%"Python")
print("%10s"%"Python")
print()
print("{2:d} {1:5} {0:05d}".format(123,1234,12345))
print("{a} {b} {c}".format(a=100, b=200, c=300))
print("{c} {a:05d} {b}".format(a=100, b=200, c=300))
print(r"\n \t \" \\를 그대로 출력")
print('''첫번째
두번째
세번때''')