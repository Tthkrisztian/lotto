import random
lottoszamok = []
while len(lottoszamok)<5:
    kihuzott = random.randrange(1,91)
    if kihuzott not in lottoszamok:
        lottoszamok.append(kihuzott)
print(lottoszamok)# lotto
