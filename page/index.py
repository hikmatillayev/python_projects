# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:59:13 2022

@author: Windows 10
"""
# mevalar=['olma', 'anjir', 'shaftoli', 'orik']
# narxlar=[100, 200, 3112, 212,1212]
#
# ismlar=['Baxtiyor', 'Javlon','Maruf']
# print("Salom " + ismlar[0] + " bugun choyxona bormi?" )
# print(ismlar[1] + " choyxonaga boramizmi?" )
#
# sonlar=[12, 13.2, -24]
# print(sonlar[0]+sonlar[2])
# sonlar.insert(1, 24)
# sonlar.append(45)
# print(sonlar)
# sonlar.remove(13.2)
# del sonlar[0]
# print(sonlar)
#
# t_shaxslar=["Amir Temur", "Imom Buxoriy", "Alisher Navoiy", "Cho'lpon"]
# z_shaxslar=["Muhammadali", "Prezident", "Hokim"]
#
# shaxs=t_shaxslar.pop(2)
# lider=z_shaxslar.pop(0)
# print("Men tarixiy shaxslardan" + " " + shaxs + " " + "bilan, zamonaviy shaxslardan esa" + " " + lider + " " + "bilan suhbat qilishni istar edim")
# friends=[]
# friends.append("Baxtiyor")
# friends.append("Javlon")
# friends.append("Behruz")
# friends.append("Ma'ruf")
# friends.append("Mehroj")
# print(friends)
# friend=friends.remove("Baxtiyor")
# print(friends)
#
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)
#
# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)
#
# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
#
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxatlar o'zgarmas qoldi:", mehmonlar)
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
#
# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Ro'yxat uzunligi:", len(fruits))
#
# sonlar=list(range(0,10,2))
# print(sonlar)
#
# davlatlar=["O'zbekiston","Qozog'iston","Qirg'iziston","Turkiya"]
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
#
# juftlar=list(range(120, 1201, 2))
# print(juftlar)
# print(sum(juftlar))
# print(max(juftlar)-min(juftlar))
# print(len(juftlar))
# bosh=list(range(120, 160,2))
# print("Ro'yxat boshidan 20 ta raqam: ",bosh)
# orta=list(range(520,560,2))
# print("Ro'yxat o'rtasidan 20 ta raqam: ",orta)
# oxir=list(range(1160, 1200,2))
# print("Oxirdan 20ta raqam: ",oxir)
#
# taomlar=("manti","lavash","hotdog","osh", "sho'rva")
# print(taomlar)
# nonushta=taomlar[:]
# nonushta=list(taomlar)
# print(nonushta)
# nonushta.remove('osh')
# print(nonushta)
# print(taomlar)
# nonushta=tuple(nonushta)
# nonushta=list(nonushta)
# nonushta[0]="qaymoq va non"
# print(nonushta)


# mehmonlar=['Ali', 'Vali', 'Soli','Hasan', 'Husan']
# for mehmon in mehmonlar:
#     print(mehmon)
#     print("Hurmatli {mehmon},xush kelibsiz")
    
    
# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# ismlar=["baxtiyor","Javlon","Hasan","Bobur","Abror"]
# for ism in ismlar:
#     print("Assalomu aleykum:", ism)
# print("Kod", len(ismlar),"marta takrorlandi")
# toq_sonlar=list(range(11,100,2))
# for toq in toq_sonlar:
#     print(toq**3)
# print(list(range(11, 100, 2)))

# kinolar=[]
# print("5 ta eng sevimli kinolarizni kiriting:")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-eng sevimli kinoyizni kiriting: "))
# print(kinolar)


# cars=['toyota','mazda','gm','kia','hyundai']
# for avto in cars:
#     if avto!='gm':
#         print(avto.title())
#     else:
#         print(avto.upper())

# javob=float(input("11*6 nechchiga teng?>>>"))
# if javob!=66:
#     print("Javob xato!")

# yil=int(input("Tug'ilgan yilingizni kirititng:"))
# if 2022-yil<18:
#     print(f"Yoshinigz {2022-yil} da ekan")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibisiz!")

# # login=int(input("Loginizni kiriting:"))
# ism=input("Ismingizni kiriting:")
# if  ism.lower()=='uktam':
#     print(f"Xush kelibsiz, Admin {ism.title()}  foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz ", {ism.title()})


# first=int(input("Birinchi sonni kiriting:"))
# if first>0:
#     print(first**(1/2))
# elif first==0:
#     print("Bu son 0 ga teng")
# else:
#     print(input("Musbat son kiriting:"))



# menu=['osh','qozonkabob','shashlik','norin','somsa']
# ovqat=input("Nima ovqat yeysiz>>>")
# if ovqat in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")


# kun=input("Bugun kun nima>>>")
# harorat=float(input("Havo harorati qanday>>"))
# if kun.lower()=='yakshanba' and harorat>30:
#     print("cho'milganini ketdik")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Bugun uyda dam olamiz")

# price=15000
# choy=True
# salat=False
#
# if choy and salat:
#     price=price+1000
# elif choy or salat:
#     price=price+5000
# print(f"Jami {price} so'm")

# juft_son=float(input("Juft sin kiriting: "))
# if juft_son%2==0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas")

# age=int(input("Nechchi yoshdasiz: "))
# if age<=4 or age>60:
#     price=0
# elif age<=18:
#     price=10000
# else:
#     price=20000
# print(f"Sizga muzeyga kirish {price} so'm")

# frst_number=int(input("Birinchi sonni kiriting: "))
# scnd_number=int(input("Ikkinchi sonni kiriting: "))
# if frst_number==scnd_number:
#     print(f"Bu sonlar o'zaro teng! {frst_number}={scnd_number}")
# if frst_number>=scnd_number:
#     print(f"{frst_number}>{scnd_number}")
# if frst_number<=scnd_number:
#     print(f"{frst_number}<{scnd_number}")

# mahsulotlar=["sabzi","kartochka","sholg'om","piyoz","rediska","norin","kivi","apelsin","limon","banan"]
#
# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))
#
# bor_mahsulotlar=[]
# mavjud_emas=[]
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             bor_mahsulotlar.append(mahsulot)
#         else:
#             mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# foydalanuvchilar=[]
#
# for n in range(5):
#     foydalanuvchilar.append(input(f"{n+1}-loginni kiriting: "))
# new_login=input("Yangi login kiriting: ")
# for login in foydalanuvchilar:
#     print(login)
# if login==new_login:
#         print("Login band, yangi login tanlang!")
# else:
#         print("Xush kelibsiz, foydalanuvchi!")


# son=int(input("Butun sonni kiriting: "))
#
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} songa bo'linadi")

# car_0={'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# talaba_0={'ism':'uktam', 'yosh':20, 't_yil':2002}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-da tug'ilgan,\
#   {talaba_0['yosh']} yoshda ")
#
# talaba_0['kurs']=4
# talaba_0['fakultet']='informatika'
# print(talaba_0)
#
# talaba_1={}
#
# talaba_1['ism']='uktam hikmatillayev'
# talaba_1['yosh']=20
# talaba_1['kasb']='talaba'
# print(talaba_1)
# print(f" {talaba_1['kasb'].title()} {talaba_1['ism'].title()}, {talaba_1['yosh']} yoshda ")
#
# talaba_1['yosh']=22
# print(f"{talaba_1['kasb'].title()} {talaba_1['yosh']} yoshda")
#
# del talaba_1['ism']
# print(talaba_1)

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
#
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")
# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# phone = telefonlar.get('hasan')
# print(phone)
# otam={
#     'ism':'ravshan xodjaqulov',
#     'yil':'1970',
#     'vil':'qashqadaryo',
#     'tuman':'Kasbi',
#     'mfy':'istiqlol',
#     'kocha':'tutzor'
# }
# print(f"Otam {otam['ism'].title()}, {otam['yil']}-yilda {otam['vil'].title()} viloyati {otam['tuman'].title()} tumani {otam['mfy'].title()} mahallasi {otam['kocha'].title()} ko'chasida tugilgan")


# taomlar={
#     'otam':'osh',
#     'onam':'shorva',
#     'akam':'baliq',
#     'ukam':'manti',
#     'singlim':'sumalak'
# }
# print(f"Otamning sevimli taomi {taomlar['otam']}, onamning sevimli taomi {taomlar['onam']}, akamni sevimli taomi {taomlar['akam']}, ukamniki {taomlar['ukam']}")

# dictionary={
#     'apple':'olma',
#     'apricot':'shaftoli',
#     'banana':'banan',
#     'hand':'qo"L',
#     'car':'mashina',
#     'hair':'soch',
#     'bread':'non',
#     'phone':'telefon',
#     'notebook':'daftar',
#     'eye':'ko"z'
# }
#
# for kalit, qiymat in dictionary.items():
#     print(f"{kalit.title()} ning tarjimasi {qiymat}")
#
# kalit=input("Ixtiyoriy so'zni kiriting: ").lower()
# print(dictionary.get(kalit, "Bunday so'z mavjd emas!"))

# if new in dictionary:
#     print(f" {new.title()} so'zi {dictionary[new].title()} deb tarjima qilinadi.")
# else:
#     print("Bunday so'z mavjud emas!")


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
#
# bozorlik=['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
#
# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# dictionary={
#     'apple':'olma',
#     'apricot':'shaftoli',
#     'banana':'banan',
#     'hand':'qo"L',
#     'car':'mashina',
#     'hair':'soch',
#     'bread':'non',
#     'phone':'telefon',
#     'notebook':'daftar',
#     'eye':'ko"z'
# }
#
# for k,q in sorted(dictionary.items()):
#     print(f"{k}-{q}")


# davlatlar={
#     'uzbekistan':'tashkent',
#     'rossiya':'moskva',
#     "qirg\'isizton":"bishkek",
#     'turkiya':'anqara',
#     "qozog\'iston":"ostona"
# }
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.title())
#
#
# print("Poytaxtlar")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())


davlatlar={
    'uzbekistan':'tashkent',
    'rossiya':'moskva',
    "qirg\'isizton":"bishkek",
    'turkiya':'anqara',
    "qozog\'iston":"ostona"
}
kalit=input("Qaysi davlatning poytaxtini bilishni hohlaysiz: ").lower()

if kalit in davlatlar:
    print(f" {kalit.title()} poytaxti {davlatlar[kalit].title()} shahri")
else:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")



