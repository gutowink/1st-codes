import random

ordem = []

for i in range(10):
    num = random.randint(1, 1000)
    ordem.append(num)

aux = len(ordem)
for i in range(len(ordem)):
    for j in range(aux - 1):
        if ordem[j] > ordem[j + 1]:
            aux2 = ordem[j]
            ordem[j] = ordem[j + 1]
            ordem[j + 1] = aux2
print(ordem)