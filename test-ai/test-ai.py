
# bankamat


hisobdagi_pul = 100

while True:
    print("Sizning hisobingiz" , hisobdagi_pul)

    pul = int(input("qancha pul yechib olasiz: "))

    if pul > hisobdagi_pul:
        print("hisobingizda mablag' yetarli emas")

    elif pul < hisobdagi_pul:

         print(hisobdagi_pul - pul)
         break





# 1 dan 20 magacha son
    
son = 1 
while son <= 20:
    print(son)

    son += 1




# 20 dan 1 gacha teskari sanoq

son = 20
while son >1:
    son -= 1
    print(son)


# 2 ga bulinadigan

for i in range(1, 51):
    i % 2 ==0
    print(i)


# karra jadvali



for i in range(1, 71):
    i % 7 ==0
    print(f" 7 * {i} = 7 * {i}")






# parol tekshirish



kiritilgan_parol = 123

while True:
    parol = int(input("Parol kiritng: "))

    if parol == kiritilgan_parol:
        print("Togri")
        break

    else:
        print("Kiritilgan parol hato boshqa parol sinab kuring: ")





# 5 ga bulinadigan lar

for i in range(1, 101):
    if i % 5 == 0:
        print(i)



# tahminiy oyin

import random

tahminiy_son = random.randint(1,100)

urinishlar = 0

while True:
    if urinishlar == 3:
        print("urinishlar soni tugadi shuning uchun akkaunt bloklandi")
        break

    son = int(input("1 dan 100 gacha son kiriting: "))
    urinishlar += 1

    if son == tahminiy_son:
        print("barakalla topdingiz")
        break
    elif son > tahminiy_son:
        print("Kiritgan soningiz katta")
    else:
        print("Kiritgan soningiz kichik")






# 1 dan 100 gacha yigindi 
yigindi = 0

for i in range(1, 101):
    yigindi = yigindi + i
print(yigindi)

