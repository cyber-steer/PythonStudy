import random
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}')
#     print("-"*15)

# for i in range(2,10,2):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}')
#     print("-"*15)

# count = 0
# number = 0
# answer = random.randint(1,100)
#
# while number != answer:
#     number = int(input("숫자 입력 : "))
#     count += 1
#     if number > answer:
#         print(f"{number}보다 낮습니다")
#     elif number <answer:
#         print(f"{number}보다 높습니다")
#     print(f"남은 시도 횟수 : {10-count}")
#     print()
#     if count >9:
#         break
#
# if answer == number:
#     print(f"{count}번만에 정답!")
# else:
#     print(f"정답은 {answer}입니다")

# a=['a','b','c','d','e']
# b=[1,2,3]
# for s in zip(a,b):
#     print(s)
#     print(list(s))

list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)