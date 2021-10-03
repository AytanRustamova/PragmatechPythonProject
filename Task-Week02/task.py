import math, random

# 1.Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik: Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək. Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1. Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır. Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.

def proccess(num):
    while num !=1:
        if num%2==0:
            return num/2
        else:
            num+1


# n natural ədədi verilmişdir. Əgər n ədədi hər hansı bir m natural ədədinin kvadratıdırsa, onda m ədədini çap edin, əks halda No çap edin. Məsələn: User 25 daxil etsə ekrana 5 verilsin 27 daxil etsə, NO yazılsın

n = int(input("Bir eded daxil edin: "))

if math.sqrt(n) == int(math.sqrt(n)):
    print(int(math.sqrt(n)))
else:
    print("NO")

# User bir ədəd daxil etsin həmin ədədə qədər bütün ədədləri çapa verin.

n = int(input('Eded daxil edin:'))

for i in range(n):
    print(i+1)


# İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin.

myText="In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available."

print(myText[0::2])


# Kvadrat tənliyin əmsallarını daxil etsin user. Həmin əmsallara görə tənliyin köklərini daxil edin. Aşağıdakı linkdən kvadrat tənlik haqda məlumat əldə edə bilərsiz 

print("Kvadrat tenlik: a*x*x + b*x + c = 0")

a = int(input("a emsalini daxil edin: "))
b = int(input("b emsalini daxil edin: "))
c = int(input("c emsalini daxil edin: "))
d = math.pow(b,2) - 4*a*c

if d>0:
    print("Kvadrat tenliyin 2 koku var.")
    x1 = (-b + math.sqrt(d))/(2*a)
    print(f'x1 = {x1}')
    x2 = (-b - math.sqrt(d))/(2*a)
    print(f'x2 = {x2}')
elif d == 0:
    print("Kvadrat tenliyin 1 koku var.")
    x1 = (-b)/(2*a)
    print(f'x1 = x2 = {x1}')
else:
    print("Kvadrat tenliyin heqiqi koku yoxdur.")
    x1 = (-b + math.sqrt(math.pow(-b,2) + 4*a*c))/(2*a)
    print(f'x1 = {x1}')
    x2 = (-b - math.sqrt(math.pow(-b,2) + 4*a*c))/(2*a)
    print(f'x2 = {x2}')



# 1-50 arasında ədədlərdən 3-ə bölünən ədədlərə three, 5-ə bölünən ədədlərə five, həm 3 və həm də 5-ə bölünənlərə isə ThreeFive print edin. Əgər heç birinə bölünməsə sadəcə ədədin özünü çapa verin.

for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("ThreeFive")
    elif i % 3 == 0:
        print("Three")
    elif i% 5 == 0:
        print("Five")

    else:
        print(i)


# Userdən bir ədəd daxil etməsini tələb edin. Ekrana həmin ədəddəki ədədlərin hasilini çapa verin.

a = input("Eded daxil edin: ")

arr = []
arr.append(a)
a = 1

for i in str(arr[0]):
    a*=int(i)

print(a)


