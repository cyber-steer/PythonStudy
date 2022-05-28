import random

rotto = []
while True:
    rand = random.randrange(1,46)
    if rand not in rotto:
        rotto.append(rand)
    if len(rotto) == 6:
        break
rotto.sort()
print(rotto)