foods = {
    "떡볶이":"보드카",
    "짜장면":"고량주",
    "라면":"소주",
    "피자":"맥주",
    "치킨":"맥주",
    "삼겹살":"소주"
}

for value in foods.values():
    print(value)
print()
for value in foods:
     print(value)
print()
for value in foods.items():
    print(value)
# while True:
#     food = input(str(list(foods.keys()))+" 중 좋아하는 읍식은?")
#     if food in foods:
#         print("<%s> 궁합 음식은 <%s>입니다."%(food, foods.get(food)))
#     elif food == "끝":
#         break
#     else:
#         print("그런 음식이 없스빈다. 확인해보세요")