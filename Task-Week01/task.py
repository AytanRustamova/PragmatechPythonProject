# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

a= input("Birinci eded:")
b= input("Ikinci eded:")
c= input("Ucuncu eded:")
d= input("Dorduncu eded:")

if a==b==c==d:
    kvs= a*a
    print(kvs)
else:
    prmt = a+b+c+d
    print(prmt)

# Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

arr =[]

while True:
    if len(arr) < 4:
        num = int(input("Eded daxil edin:" ))
        arr.append(num)
    else:
        break

arr.sort()
print(arr[3])



meyveler = ['alma', 'armud', 'banan', 'nar']
prices = [4, 6, 8, 10]

print(meyveler)

chooseMeyve = input('Istediyiniz meyveni secin:')
if chooseMeyve == meyveler[0]:
    print(prices[0])
elif chooseMeyve ==meyveler[1]:
    print(prices[1])
elif chooseMeyve == meyveler[2]:
    print(prices[2])
elif chooseMeyve == meyveler[3]:
    print(prices[3])
else:
    print('Sectiyiniz meyve yoxdur')


# Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın. Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır. Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır. Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır. Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin: (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin. Yəni hər şərti müvafiq mesajlar ilə userə izah edin. ============================================= Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ============================================= Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.



username = input('Adinizi Daxil Edin: ')

if 3<len(username)<11:
    surname = input('Soyadinizi Daxil Edin: ')
    if 5<len(surname)<15:
        year = input('Doguldugunuz ili daxil edin:')
        if len(year)==4:
            email = input('Emailinizi Daxil edir: ')
            if 10<len(email)<22 and email.split("@")[1] == "gmail.com":
                password= input('Parolunuzu Daxil Edin:')
                if 6<len(password)<13:
                    confirm_password = input("Parolunuzu tesdiqleyin: ")
                    if confirm_password == password:
                        print("Qeydiyyat tamamlandi!")
                        sual = input("Qeydiyyatin detallarina baxmaq isteyirsiniz?Y/N")
                        if sual == "Y" or sual == "y":
                            print(f'Adiniz: {username}, Soyadiniz: {surname}, Dogum iliniz: {year}, Emailiniz: {email}, Parolunuz: {password}')
                        else:
                            print(f'{username}, Ugurlar!')
                    else:
                        print('Parol eyni deyil!')
                else:
                    print('Parolu duzgun daxil edin')
                
            else:
                print('Email 10 herfden kicik ve ya 22 herfden cox ola bilmez')
        else:
            print('Doguldugunuz il 4 karakterden ibaret olmalidir.')
    else:
        print('Soyadinizi duzgun daxil edin. 5 ile 15 arasinda olmalidir')

else:
    print('Adiniz Duzgun deyil. 3 ile 11 herf arasinda olmlidir')




# Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

my_list = [75, 56, 77,98]
sum=0
for i in my_list:
    sum = sum + i
print(sum)


# Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

my_list = [75, 56, 77,98,144]

a= 0

for i in range(len(my_list)):
    if my_list[i] > a:
        a = my_list[i]
print(a)

# Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.

my_list = [75, 56, 77,98,144,1]

min = my_list[0]

for i in my_list:
    if i < min:
        min = i
print(min)


# Write a Python program to check a list is empty or not.

my_list = [75, 56, 77,98,144,1]

if len(my_list) == 0:
    print("List is empty")
else:
    print(my_list,"List is not empty")

# my_text = "write a python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."

word = my_text.split()
sorted_word = sorted(word)
print(" ".join(sorted_word).lower())


# Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.

num= int(input("Bir eded yazin: "))
def day(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return None

print(day(num))



